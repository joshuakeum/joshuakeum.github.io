"""A small Notion API client using only the standard library."""
import json
import re
import time
import urllib.error
import urllib.request

API = "https://api.notion.com/v1"
VERSION = "2026-03-11"


def page_id(value):
    """Accept a page ID with or without dashes, or the page's full link."""
    ids = re.findall(r"[0-9a-f]{32}", (value or "").lower().replace("-", ""))
    if not ids:
        raise SystemExit("NOTION_PAGE_ID does not contain a Notion page ID.")
    return ids[-1]


class Notion:
    def __init__(self, token):
        self.token = token

    def request(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        for attempt in range(6):
            req = urllib.request.Request(API + path, data=data, method=method, headers={
                "Authorization": "Bearer " + self.token,
                "Notion-Version": VERSION,
                "Content-Type": "application/json",
            })
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return json.load(resp)
            except urllib.error.HTTPError as e:
                if e.code == 429 or e.code >= 500:
                    time.sleep(min(float(e.headers.get("Retry-After") or 2 ** attempt), 60))
                    continue
                detail = e.read().decode(errors="replace")[:500]
                raise SystemExit("Notion API %s %s failed with %d: %s" % (method, path.split("?")[0], e.code, detail))
            except urllib.error.URLError:
                time.sleep(2 ** attempt)
        raise SystemExit("Notion API %s %s kept failing; giving up." % (method, path.split("?")[0]))

    def children(self, block_id):
        out, cursor = [], None
        while True:
            query = "?page_size=100" + ("&start_cursor=" + cursor if cursor else "")
            resp = self.request("GET", "/blocks/%s/children%s" % (block_id, query))
            out += resp["results"]
            if not resp.get("has_more"):
                return out
            cursor = resp["next_cursor"]

    def tree(self, block_id):
        """All blocks under block_id, each block's children in block['children']."""
        blocks = self.children(block_id)
        for block in blocks:
            if block.get("has_children") and block["type"] not in ("child_page", "child_database"):
                block["children"] = self.tree(block["id"])
        return blocks

    def title(self, page):
        props = self.request("GET", "/pages/" + page)["properties"]
        for prop in props.values():
            if prop["type"] == "title":
                return "".join(t["plain_text"] for t in prop["title"]).strip()
        return ""

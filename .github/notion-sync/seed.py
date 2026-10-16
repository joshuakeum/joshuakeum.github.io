"""Write the published walkthrough into an empty Notion page, once.

Run by .github/workflows/notion-seed.yml with the post's HTML from render.rb:
    python seed.py POST.html
Images are linked by their URL on the site, not uploaded. Refuses to run if
the page already has content or the seed has been done (state.json), so it
cannot overwrite anything written in Notion.
"""
import json
import os
import re
import sys

from html_blocks import html_to_blocks
from notion_api import Notion, page_id
from sync import HERE, POST, ROOT, SITE, load

BATCH = 100        # blocks per append request
MAX_ELEMENTS = 900  # Notion allows 1000 block elements per request


def count(block):
    kind = block["type"]
    return 1 + sum(count(k) for k in block[kind].get("children", []))


def depth(block):
    kids = block[block["type"]].get("children", [])
    return 1 + max((depth(k) for k in kids), default=0)


def main(html_path):
    if load(HERE / "state.json", {}).get("seeded"):
        raise SystemExit("The Notion page was already seeded (state.json); not seeding again.")
    notion = Notion(os.environ["NOTION_TOKEN"])
    page = page_id(os.environ["NOTION_PAGE_ID"])
    if notion.request("GET", "/blocks/%s/children?page_size=1" % page)["results"]:
        raise SystemExit("The Notion page is not empty. Seed into a new, empty page.")

    post = (ROOT / POST).read_text(encoding="utf-8")
    title = re.search(r'^title:\s*"?(.*?)"?\s*$', post, re.M).group(1)
    blocks = html_to_blocks(open(html_path, encoding="utf-8").read(), SITE)
    if any(depth(b) > 3 for b in blocks):
        raise SystemExit("The post nests lists more deeply than one request can create.")

    notion.request("PATCH", "/pages/" + page,
                   {"properties": {"title": {"title": [{"text": {"content": title}}]}}})
    batch, size = [], 0
    for block in blocks + [None]:
        if block is None or len(batch) == BATCH or size + count(block) > MAX_ELEMENTS:
            if batch:
                notion.request("PATCH", "/blocks/%s/children" % page, {"children": batch})
            batch, size = [], 0
        if block is not None:
            batch.append(block)
            size += count(block)
    (HERE / "state.json").write_text(json.dumps({"seeded": True}, indent=2) + "\n", encoding="utf-8")
    print("Seeded %d blocks into the Notion page." % len(blocks))


if __name__ == "__main__":
    main(sys.argv[1])

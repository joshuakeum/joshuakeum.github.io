"""Pull the Bioinformatics Walkthrough from Notion and write it into the site.

Run every 15 minutes by .github/workflows/notion-sync.yml. Needs the secrets
NOTION_TOKEN and NOTION_PAGE_ID. The Notion page is the source of the post's
text: whatever differs here is overwritten. Kept from the repository:
  - front matter other than the title (date, tags, description, ...)
  - alt text for images (alt-text.json, keyed by image path)
  - images already on the site, which the Notion page links to by URL.
Images uploaded in Notion are downloaded as notion-<block id>.<ext>.

Safety: does nothing until seed.py has filled the page (state.json), stops if
the page is empty, and stops if the post would lose more than half its text,
unless run with --force.
"""
import hashlib
import io
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from notion_api import Notion, page_id
from notion_markdown import Context, render

POST = "_posts/2026-10-11-bioinformatics-walkthrough.md"
IMG_DIR = "assets/img/bioinformatics-walkthrough"
SITE = "https://joshuakeum.github.io"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TYPES = {"image/png": ".png", "image/jpeg": ".jpg", "image/gif": ".gif",
         "image/webp": ".webp", "image/svg+xml": ".svg"}


def load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def save(path, data):
    text = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def size_of(path):
    if path.suffix == ".svg":
        head = path.read_text(encoding="utf-8", errors="replace")[:4000]
        w, h = (re.search(r'\b%s="([\d.]+)' % k, head) for k in ("width", "height"))
        if w and h:
            return round(float(w.group(1))), round(float(h.group(1)))
        box = re.search(r'viewBox="[\d.\s-]+?\s([\d.]+)\s+([\d.]+)"', head)
        return (round(float(box.group(1))), round(float(box.group(2)))) if box else (0, 0)
    from PIL import Image
    with Image.open(path) as im:
        return im.size


def clean(data, ext):
    """Strip metadata from PNG and JPEG uploads; leave other formats as they are."""
    if ext not in (".png", ".jpg"):
        return data
    from PIL import Image, ImageOps
    im = Image.open(io.BytesIO(data))
    out = io.BytesIO()
    if ext == ".jpg":
        ImageOps.exif_transpose(im).convert("RGB").save(out, "JPEG", quality=90, optimize=True)
    else:
        if im.mode in ("RGBA", "LA") and im.getchannel("A").getextrema() == (255, 255):
            im = im.convert("RGB")
        im.save(out, "PNG", optimize=True)
    return out.getvalue()


class Images:
    """Resolves Notion image blocks to site paths, downloading uploads."""

    def __init__(self, manifest, alt_text, fetch=True):
        self.manifest, self.alt_text, self.fetch = manifest, alt_text, fetch
        self.seen = set()

    def __call__(self, block):
        d = block["image"]
        url = d[d["type"]]["url"]
        if d["type"] == "external" and url.startswith(SITE + "/"):
            path = urllib.parse.unquote(urllib.parse.urlsplit(url).path)
        else:
            path = self.download(block["id"], url)
        caption = "".join(r.get("plain_text", "") for r in d.get("caption") or [])
        alt = self.alt_text.get(path) or re.sub(r"^\s*Fig\.?\s*\d+[A-Za-z]?\.?\s*", "", caption) or "Figure"
        local = ROOT / path.lstrip("/")
        w, h = size_of(local) if local.exists() else (0, 0)
        return path, w, h, alt

    def download(self, block_id, url):
        self.seen.add(block_id)
        entry = self.manifest.get(block_id)
        if not self.fetch:
            return entry["path"] if entry else "/%s/notion-missing.png" % IMG_DIR
        req = urllib.request.Request(url, headers={"User-Agent": "joshuakeum.github.io notion-sync"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read(20 * 1024 * 1024 + 1)
            ctype = resp.headers.get_content_type()
        if len(data) > 20 * 1024 * 1024:
            raise SystemExit("An image in the Notion page is over 20 MB.")
        digest = hashlib.sha256(data).hexdigest()
        if entry and entry["sha256"] == digest and (ROOT / entry["path"].lstrip("/")).exists():
            return entry["path"]
        ext = TYPES.get(ctype) or Path(urllib.parse.urlsplit(url).path).suffix.lower().replace(".jpeg", ".jpg") or ".png"
        path = "/%s/notion-%s%s" % (IMG_DIR, block_id.replace("-", "")[:12], ext)
        if entry and entry["path"] != path:
            (ROOT / entry["path"].lstrip("/")).unlink(missing_ok=True)
        (ROOT / path.lstrip("/")).write_bytes(clean(data, ext))
        self.manifest[block_id] = {"path": path, "sha256": digest}
        return path

    def prune(self):
        """Delete downloaded images whose blocks are gone from the page."""
        for block_id in [b for b in self.manifest if b not in self.seen]:
            path = self.manifest.pop(block_id)["path"]
            if Path(path).name.startswith("notion-"):
                (ROOT / path.lstrip("/")).unlink(missing_ok=True)


def front_matter(current, title, uses_math):
    lines = re.match(r"\A---\n(.*?)\n---\n", current, re.S).group(1).split("\n")
    if title:
        quoted = '"%s"' % title.replace("\\", "\\\\").replace('"', '\\"')
        lines = ["title: " + quoted if l.startswith("title:") else l for l in lines]
    if uses_math and not any(l.startswith("math:") for l in lines):
        lines.append("math: true")
    return "---\n%s\n---\n" % "\n".join(lines)


def build(blocks, title, current, images):
    """The new post text, and the conversion warnings."""
    ctx = Context(images)
    body = render(blocks, ctx)
    return front_matter(current, title, ctx.uses_math) + "\n" + body + "\n", ctx.warnings


def main(argv):
    force = "--force" in argv
    token, page = os.environ.get("NOTION_TOKEN"), os.environ.get("NOTION_PAGE_ID")
    if not token or not page:
        print("NOTION_TOKEN or NOTION_PAGE_ID is not set; nothing to do.")
        return
    if not load(HERE / "state.json", {}).get("seeded"):
        print("The Notion page has not been seeded yet; run the seed workflow first.")
        return
    notion, page = Notion(token), page_id(page)
    blocks = notion.tree(page)
    if not blocks:
        raise SystemExit("The Notion page is empty; refusing to empty the post.")
    post = ROOT / POST
    current = post.read_text(encoding="utf-8")
    manifest = load(HERE / "images.json", {})
    images = Images(manifest, load(HERE / "alt-text.json", {}))
    text, warnings = build(blocks, notion.title(page), current, images)
    images.prune()
    for w in warnings:
        print("warning:", w)
    old_body = current.split("\n---\n", 1)[1]
    new_body = text.split("\n---\n", 1)[1]
    if len(new_body) < len(old_body) / 2 and not force:
        raise SystemExit("The post would shrink from %d to %d characters. If that is intended, "
                         "run the workflow by hand with force." % (len(old_body), len(new_body)))
    save(HERE / "images.json", manifest)
    if text != current:
        post.write_text(text, encoding="utf-8")
        print("Updated", POST)
    else:
        print("No change in", POST)


if __name__ == "__main__":
    main(sys.argv[1:])

"""Turn a post's kramdown HTML into Notion blocks (the shape the API accepts).

Used once, to seed the Notion page from the published post. Reading the HTML
rather than the Markdown means kramdown has already resolved escapes, smart
quotes and dashes, so the Notion text matches what readers see.

Inverse of notion_markdown.py:
  h2-h5 -> heading 1-4, blockquote.prompt-* -> callout, <p><img><em> -> image
  with caption, \\(..\\) -> inline equation, ul/ol -> list items with children.
Anything else raises, so nothing is dropped silently.
"""
import re
from html.parser import HTMLParser

HEADINGS = {"h2": "heading_1", "h3": "heading_2", "h4": "heading_3", "h5": "heading_4"}
ICONS = {"tip": "💡", "info": "ℹ️", "warning": "⚠️", "danger": "🚨"}
VOID = {"img", "br", "hr", "input", "meta", "link"}
MAX_TEXT = 2000  # Notion's limit for one rich text object


class _Node:
    def __init__(self, tag, attrs=None):
        self.tag, self.attrs, self.kids = tag, dict(attrs or {}), []


class _Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = _Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = _Node(tag, attrs)
        self.stack[-1].kids.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].kids.append(_Node(tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].kids.append(data)


def _ann(fmt):
    bold, italic, strike, code = fmt
    return {"bold": bold, "italic": italic, "strikethrough": strike,
            "underline": False, "code": code, "color": "default"}


def _inline(nodes, fmt=(False, False, False, False), href=None, runs=None):
    """Flatten inline HTML into [text, fmt, href, is_equation] runs."""
    runs = [] if runs is None else runs
    for n in nodes:
        if isinstance(n, str):
            text = re.sub(r"\s+", " ", n)
            for k, part in enumerate(re.split(r"\\\((.*?)\\\)", text)):
                if k % 2:
                    runs.append([part, fmt, None, True])
                elif part:
                    runs.append([part, fmt, href, False])
            continue
        b, i, s, c = fmt
        if n.tag in ("strong", "b"):
            _inline(n.kids, (True, i, s, c), href, runs)
        elif n.tag in ("em", "i"):
            _inline(n.kids, (b, True, s, c), href, runs)
        elif n.tag in ("del", "s"):
            _inline(n.kids, (b, i, True, c), href, runs)
        elif n.tag == "code":
            _inline(n.kids, (b, i, s, True), href, runs)
        elif n.tag == "a":
            _inline(n.kids, fmt, n.attrs.get("href"), runs)
        elif n.tag == "br":
            runs.append(["\n", fmt, href, False])
        elif n.tag in ("span", "sup", "sub", "abbr"):
            _inline(n.kids, fmt, href, runs)
        else:
            raise ValueError("unexpected inline <%s>" % n.tag)
    return runs


def _rich(nodes):
    merged = []
    for r in _inline(nodes):
        if merged and not r[3] and not merged[-1][3] and merged[-1][1:3] == r[1:3]:
            merged[-1][0] += r[0]
        else:
            merged.append(list(r))
    while merged and not merged[0][3] and not merged[0][0].lstrip():
        merged.pop(0)
    while merged and not merged[-1][3] and not merged[-1][0].rstrip():
        merged.pop()
    if merged and not merged[0][3]:
        merged[0][0] = merged[0][0].lstrip()
    if merged and not merged[-1][3]:
        merged[-1][0] = merged[-1][0].rstrip()
    out = []
    for text, fmt, href, is_eq in merged:
        if is_eq:
            out.append({"type": "equation", "equation": {"expression": text}, "annotations": _ann(fmt)})
            continue
        for k in range(0, len(text), MAX_TEXT):
            out.append({"type": "text", "annotations": _ann(fmt),
                        "text": {"content": text[k:k + MAX_TEXT], "link": {"url": href} if href else None}})
    return out


def _block(kind, rich_text, children=None, **extra):
    body = dict(rich_text=rich_text, **extra)
    if children:
        body["children"] = children
    return {"object": "block", "type": kind, kind: body}


def _elements(node):
    return [k for k in node.kids if not (isinstance(k, str) and not k.strip())]


def _list(node, site):
    kind = "bulleted_list_item" if node.tag == "ul" else "numbered_list_item"
    items = []
    for li in _elements(node):
        if isinstance(li, str) or li.tag != "li":
            raise ValueError("unexpected <%s> in a list" % getattr(li, "tag", "text"))
        inline, children = [], []
        for k in li.kids:
            if not isinstance(k, str) and k.tag in ("ul", "ol"):
                children += _list(k, site)
            elif not isinstance(k, str) and k.tag == "p":
                if inline or children:
                    children.append(_block("paragraph", _rich(k.kids)))
                else:
                    inline = k.kids
            else:
                inline.append(k)
        items.append(_block(kind, _rich(inline), children))
    return items


def _paragraph(p, site):
    imgs = [k for k in p.kids if not isinstance(k, str) and k.tag == "img"]
    if not imgs:
        return [_block("paragraph", _rich(p.kids))]
    if len(imgs) > 1:
        raise ValueError("a paragraph with more than one image")
    rest = [k for k in p.kids if k is not imgs[0] and not (isinstance(k, str) and not k.strip())]
    caption = rest[0].kids if len(rest) == 1 and getattr(rest[0], "tag", "") == "em" else rest
    src = imgs[0].attrs["src"]
    url = site + src if src.startswith("/") else src
    return [{"object": "block", "type": "image",
             "image": {"type": "external", "external": {"url": url}, "caption": _rich(caption)}}]


def html_to_blocks(html, site):
    """Notion blocks for the post's HTML. `site` turns /asset paths into URLs."""
    tree = _Tree()
    tree.feed(html)
    blocks = []
    for node in _elements(tree.root):
        if isinstance(node, str):
            blocks.append(_block("paragraph", _rich([node])))
        elif node.tag in HEADINGS:
            blocks.append(_block(HEADINGS[node.tag], _rich(node.kids), is_toggleable=False, color="default"))
        elif node.tag == "p":
            blocks += _paragraph(node, site)
        elif node.tag in ("ul", "ol"):
            blocks += _list(node, site)
        elif node.tag == "hr":
            blocks.append({"object": "block", "type": "divider", "divider": {}})
        elif node.tag == "blockquote":
            paras = [k for k in _elements(node) if not isinstance(k, str)]
            if not paras or any(k.tag != "p" for k in paras):
                raise ValueError("a blockquote that is not plain paragraphs")
            first, rest = _rich(paras[0].kids), [_block("paragraph", _rich(k.kids)) for k in paras[1:]]
            prompt = re.search(r"prompt-(\w+)", node.attrs.get("class", ""))
            if prompt:
                blocks.append(_block("callout", first, rest, color="gray_background",
                                     icon={"type": "emoji", "emoji": ICONS.get(prompt.group(1), "💡")}))
            else:
                blocks.append(_block("quote", first, rest))
        else:
            raise ValueError("unexpected block <%s>" % node.tag)
    return blocks

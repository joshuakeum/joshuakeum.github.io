"""Convert Notion blocks to the Markdown this site's posts use (kramdown + Chirpy).

The input is a list of block objects as the Notion API returns them, with each
block's children already fetched into ``block["children"]``. Image paths and
sizes come from a resolver supplied by the caller, so this module does no I/O.

Mapping (Notion -> site):
  heading 1-4          -> ## ... #####   (the post title is the page's h1)
  callout              -> > text + {: .prompt-tip } (the icon picks the prompt type)
  image + caption      -> ![alt](path){: w h } with _caption_ on the next line
  inline equation      -> $$...$$       (block equation -> $$ on its own lines)
  paragraph that is only a URL -> <URL>
Italic inside a caption is written as <i>...</i>, because kramdown does not nest
emphasis inside the caption's own _..._.
"""
import re
import textwrap

HEADINGS = {"heading_1": "##", "heading_2": "###", "heading_3": "####", "heading_4": "#####"}
PROMPTS = {"💡": "tip", "ℹ️": "info", "ℹ": "info", "⚠️": "warning", "⚠": "warning",
           "🚨": "danger", "❗": "danger", "⛔": "danger"}
LIST_TYPES = {"bulleted_list_item": "ul", "numbered_list_item": "ol", "to_do": "todo"}


class Context:
    """Collects what the caller needs back: whether math is used, and warnings."""

    def __init__(self, resolve_image):
        self.resolve_image = resolve_image  # block -> (path, width, height, alt)
        self.uses_math = False
        self.warnings = []


# ---------------------------------------------------------------- rich text --

def _runs(rich_text):
    """(text, href, (bold, italic, strike, code), is_equation) runs, neighbours merged."""
    runs = []
    for r in rich_text or []:
        ann = r.get("annotations") or {}
        fmt = (bool(ann.get("bold")), bool(ann.get("italic")),
               bool(ann.get("strikethrough")), bool(ann.get("code")))
        if r.get("type") == "equation":
            runs.append((r["equation"]["expression"], None, fmt, True))
            continue
        text = r.get("plain_text")
        if text is None:
            text = (r.get("text") or {}).get("content", "")
        href = r.get("href") or ((r.get("text") or {}).get("link") or {}).get("url")
        if runs and not runs[-1][3] and runs[-1][1] == href and runs[-1][2] == fmt:
            runs[-1] = (runs[-1][0] + text, href, fmt, False)
        else:
            runs.append((text, href, fmt, False))
    return [r for r in runs if r[0] != ""]


def _escape(text, caption):
    text = text.replace("\\", "\\\\")
    text = re.sub(r"([`*\[\]<|])", r"\\\1", text)
    text = text.replace("$$", "\\$\\$").replace("{:", "\\{:")
    if caption:  # the caption itself is wrapped in _..._
        return text.replace("_", "\\_")
    return re.sub(r"(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])", "\\_", text)


def _code_span(text):
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    fence = "`" * (longest + 1)
    pad = " " if text.startswith("`") or text.endswith("`") else ""
    return fence + pad + text + pad + fence


def _url(href):
    return href.replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def _format(runs, caption):
    """Render runs that share one link target (or none)."""
    out = []
    for i, (text, _, (bold, italic, strike, code), is_eq) in enumerate(runs):
        if is_eq:
            out.append("$$" + text + "$$")
            continue
        core = text.strip()
        if not core:
            out.append(text)
            continue
        lead, trail = text[: len(text) - len(text.lstrip())], text[len(text.rstrip()):]
        body = _code_span(core) if code else _escape(core, caption)
        before = lead[-1:] or "".join(out)[-1:]
        after = trail[:1] or (runs[i + 1][0][:1] if i + 1 < len(runs) else "")
        # ** and * only open and close at word boundaries; use HTML tags elsewhere.
        tight = any(re.match(r"[\w*]", c) for c in (before, after) if c)
        if italic:
            body = "<i>%s</i>" % body if caption or tight else "*%s*" % body
        if bold:
            body = "<strong>%s</strong>" % body if tight else "**%s**" % body
        if strike:
            body = "<del>%s</del>" % body
        out.append(lead + body + trail)
    return "".join(out)


def rich(rich_text, ctx, caption=False):
    runs = _runs(rich_text)
    if any(r[3] for r in runs):
        ctx.uses_math = True
    out, i = [], 0
    while i < len(runs):
        href = runs[i][1]
        j = i + 1
        while j < len(runs) and runs[j][1] == href:
            j += 1
        group = runs[i:j]
        text = _format(group, caption)
        if href:
            lead = text[: len(text) - len(text.lstrip())]
            trail = text[len(text.rstrip()):]
            text = "%s[%s](%s)%s" % (lead, text.strip(), _url(href), trail)
        out.append(text)
        i = j
    return "".join(out).replace("\n", "<br>")


def _only_url(rich_text):
    runs = _runs(rich_text)
    return (len(runs) == 1 and runs[0][1] and runs[0][0].strip() == runs[0][1]
            and not any(runs[0][2]) and runs[0][1])


def _block_start(text):
    """Escape text that would otherwise start a list, heading, quote, etc."""
    m = re.match(r"(\d+)([.)])(\s|$)", text)
    if m:
        return m.group(1) + "\\" + text[len(m.group(1)):]
    if text[:1] in ("#", ">", "+", "-", "=", ":"):
        return "\\" + text
    return text


# ------------------------------------------------------------------- blocks --

def _children(block, ctx, prefix):
    kids = block.get("children") or []
    if not kids:
        return ""
    return textwrap.indent(render(kids, ctx), prefix, lambda line: line.strip() != "")


def _block(block, ctx):
    """Markdown for one block, or None to skip it."""
    t = block["type"]
    d = block.get(t) or {}
    if t in HEADINGS:
        text = rich(d.get("rich_text"), ctx).strip()
        own = "%s %s" % (HEADINGS[t], text) if text else ""
        kids = render(block.get("children") or [], ctx)
        return "\n\n".join(x for x in (own, kids) if x) or None
    if t == "paragraph":
        url = _only_url(d.get("rich_text"))
        text = "<%s>" % url if url else _block_start(rich(d.get("rich_text"), ctx).strip())
        kids = _children(block, ctx, "")
        return "\n\n".join(x for x in (text, kids) if x) or None
    if t in LIST_TYPES:
        marker = {"ul": "- ", "ol": "1. ", "todo": "- [%s] " % ("x" if d.get("checked") else " ")}[LIST_TYPES[t]]
        text = marker + rich(d.get("rich_text"), ctx).strip()
        kids = block.get("children") or []
        if not kids:
            return text
        sub = _children(block, ctx, " " * (3 if t == "numbered_list_item" else 2))
        joiner = "\n" if kids[0]["type"] in LIST_TYPES else "\n\n"
        return text + joiner + sub
    if t in ("callout", "quote"):
        lines = [rich(d.get("rich_text"), ctx).strip()]
        kids = render(block.get("children") or [], ctx)
        if kids:
            lines += [""] + kids.split("\n")
        body = "\n".join(("> " + l) if l else ">" for l in lines)
        if t == "callout":
            icon = d.get("icon") or {}
            body += "\n{: .prompt-%s }" % PROMPTS.get(icon.get("emoji", ""), "tip")
        return body
    if t == "divider":
        return "---"
    if t == "image":
        path, w, h, alt = ctx.resolve_image(block)
        alt = re.sub(r'[>"\n]|\s/|\s[wh]=', " ", alt or "Figure").strip()
        size = '{: w="%d" h="%d" }' % (w, h) if w and h else ""
        line = "![%s](%s)%s" % (alt.replace("]", ")").replace("[", "("), path, size)
        cap = rich(d.get("caption"), ctx, caption=True).strip()
        return line + ("\n_%s_" % cap if cap else "")
    if t == "equation":
        ctx.uses_math = True
        return "$$\n%s\n$$" % d.get("expression", "")
    if t == "code":
        text = "".join(r.get("plain_text", (r.get("text") or {}).get("content", "")) for r in d.get("rich_text") or [])
        lang = d.get("language") or ""
        lang = "" if lang == "plain text" else lang
        fence = "```" + "`" * max(0, max((len(m) for m in re.findall(r"`{3,}", text)), default=0) - 2)
        return "%s%s\n%s\n%s" % (fence, lang, text, fence)
    if t in ("bookmark", "embed", "link_preview"):
        return "<%s>" % d["url"] if d.get("url") else None
    if t == "table":
        rows = [k for k in block.get("children") or [] if k["type"] == "table_row"]
        cells = [[rich(c, ctx) for c in r["table_row"]["cells"]] for r in rows]
        if not cells:
            return None
        lines = ["| " + " | ".join(c) + " |" for c in cells]
        if d.get("has_column_header"):
            lines.insert(1, "|" + "---|" * len(cells[0]))
        return "\n".join(lines)
    if t == "toggle":
        text = _block_start(rich(d.get("rich_text"), ctx).strip())
        kids = render(block.get("children") or [], ctx)
        return "\n\n".join(x for x in (text, kids) if x) or None
    if t in ("column_list", "column", "synced_block"):
        return render(block.get("children") or [], ctx) or None
    ctx.warnings.append("skipped a %s block (%s)" % (t, block.get("id", "?")))
    return None


def render(blocks, ctx):
    """Markdown for a list of sibling blocks."""
    out, prev = [], None
    for block in blocks:
        md = _block(block, ctx)
        if md is None:
            continue
        kind = LIST_TYPES.get(block["type"])
        if out:
            # Two different lists in a row would merge into one; ^ ends the first.
            sep = "\n" if kind and kind == prev else "\n^\n\n" if kind and prev else "\n\n"
            out.append(sep)
        out.append(md)
        prev = kind
    return "".join(out)

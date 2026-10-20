#!/usr/bin/env python3
"""Build a single, print-ready Word document from the Pro Black audit markdown."""
import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_COLOR_INDEX

SRC = "Pro-Black-Website-Audit-2026-10-20.md"
OUT = "Pro-Black-Website-Audit-2026-10-20.docx"

INK      = RGBColor(0x15, 0x14, 0x12)
INK_SOFT = RGBColor(0x3D, 0x3A, 0x35)
MUTED    = RGBColor(0x6B, 0x66, 0x5E)
GOLD     = RGBColor(0x8A, 0x5A, 0x12)
RED      = RGBColor(0xA5, 0x2A, 0x24)
AMBER    = RGBColor(0x8A, 0x53, 0x10)
GREEN    = RGBColor(0x1F, 0x6F, 0x43)
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)

BODY_FONT = "Georgia"
UI_FONT   = "Calibri"


# ---------------------------------------------------------------------------- helpers
PPR_SEQ = ["w:pStyle","w:keepNext","w:keepLines","w:pageBreakBefore","w:framePr",
           "w:widowControl","w:numPr","w:suppressLineNumbers","w:pBdr","w:shd","w:tabs",
           "w:suppressAutoHyphens","w:kinsoku","w:wordWrap","w:overflowPunct",
           "w:topLinePunct","w:autoSpaceDE","w:autoSpaceDN","w:bidi","w:adjustRightInd",
           "w:snapToGrid","w:spacing","w:ind","w:contextualSpacing","w:mirrorIndents",
           "w:suppressOverlap","w:jc","w:textDirection","w:textAlignment",
           "w:textboxTightWrap","w:outlineLvl","w:divId","w:cnfStyle","w:rPr",
           "w:sectPr","w:pPrChange"]

TCPR_SEQ = ["w:cnfStyle","w:tcW","w:gridSpan","w:hMerge","w:vMerge","w:tcBorders",
            "w:shd","w:noWrap","w:tcMar","w:textDirection","w:tcFitText","w:vAlign",
            "w:hideMark","w:headers","w:cellIns","w:cellDel","w:cellMerge","w:tcPrChange"]

TRPR_SEQ = ["w:cnfStyle","w:divId","w:gridBefore","w:gridAfter","w:wBefore","w:wAfter",
            "w:cantSplit","w:trHeight","w:tblHeader","w:tblCellSpacing","w:jc","w:hidden",
            "w:ins","w:del","w:trPrChange"]

TBLPR_SEQ = ["w:tblStyle","w:tblpPr","w:tblOverlap","w:bidiVisual",
             "w:tblStyleRowBandSize","w:tblStyleColBandSize","w:tblW","w:jc",
             "w:tblCellSpacing","w:tblInd","w:tblBorders","w:shd","w:tblLayout",
             "w:tblCellMar","w:tblLook","w:tblCaption","w:tblDescription"]

RPR_SEQ = ["w:rStyle","w:rFonts","w:b","w:bCs","w:i","w:iCs","w:caps","w:smallCaps",
           "w:strike","w:dstrike","w:outline","w:shadow","w:emboss","w:imprint",
           "w:noProof","w:snapToGrid","w:vanish","w:webHidden","w:color","w:spacing",
           "w:w","w:kern","w:position","w:sz","w:szCs","w:highlight","w:u","w:effect",
           "w:bdr","w:shd","w:fitText","w:vertAlign","w:rtl","w:cs","w:em","w:lang",
           "w:eastAsianLayout","w:specVanish","w:oMath"]


def _insert_ordered(parent, elm, seq):
    """Insert elm into parent respecting the OOXML child order given by seq."""
    tag = elm.tag.split("}")[-1]
    want = "w:" + tag
    idx = seq.index(want)
    later = seq[idx + 1:]
    parent.insert_element_before(elm, *later)


def shade(cell, hex_fill):
    tc = cell._tc if hasattr(cell, "_tc") else cell
    tcPr = tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    _insert_ordered(tcPr, shd, TCPR_SEQ)


def para_shade(p, hex_fill):
    pPr = p._p.get_or_add_pPr()
    for old in pPr.findall(qn("w:shd")):
        pPr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    _insert_ordered(pPr, shd, PPR_SEQ)


def para_border(p, edge="bottom", color="D8D2C4", size=6, space=6):
    pPr = p._p.get_or_add_pPr()
    pbdr = pPr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        _insert_ordered(pPr, pbdr, PPR_SEQ)
    existing = pbdr.find(qn(f"w:{edge}"))
    if existing is not None:
        pbdr.remove(existing)
    el = OxmlElement(f"w:{edge}")
    el.set(qn("w:val"), "single")
    el.set(qn("w:sz"), str(size))
    el.set(qn("w:space"), str(space))
    el.set(qn("w:color"), color)
    # pBdr order: top, left, bottom, right, between, bar
    order = ["top", "left", "bottom", "right", "between", "bar"]
    pbdr.insert(list(enumerate(order)).__getitem__(order.index(edge))[0], el) if False else pbdr.append(el)


def cell_margins(table, top=60, bottom=60, left=100, right=100):
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblCellMar")):
        tblPr.remove(old)
    mar = OxmlElement("w:tblCellMar")
    for name, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement(f"w:{name}")
        e.set(qn("w:w"), str(val))
        e.set(qn("w:type"), "dxa")
        mar.append(e)
    _insert_ordered(tblPr, mar, TBLPR_SEQ)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:tblHeader")) is None:
        el = OxmlElement("w:tblHeader")
        el.set(qn("w:val"), "true")
        _insert_ordered(trPr, el, TRPR_SEQ)


def no_split(row):
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:cantSplit")) is None:
        el = OxmlElement("w:cantSplit")
        el.set(qn("w:val"), "true")
        _insert_ordered(trPr, el, TRPR_SEQ)


def add_field(paragraph, instr, font_size=8, color=MUTED, bold=False):
    run = paragraph.add_run()
    run.font.size = Pt(font_size)
    run.font.color.rgb = color
    run.bold = bold
    run.font.name = UI_FONT
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), instr)
    r = OxmlElement("w:r")
    t = OxmlElement("w:t")
    t.text = "1"
    r.append(t)
    fld.append(r)
    run._r.addnext(fld)


def add_hyperlink(paragraph, text, url, size=9.5, color="8A5A12"):
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), color); rPr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rPr.append(sz)
    rf = OxmlElement("w:rFonts"); rf.set(qn("w:ascii"), UI_FONT); rf.set(qn("w:hAnsi"), UI_FONT); rPr.append(rf)
    new_run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    new_run.append(t)
    link.append(new_run)
    paragraph._p.append(link)


def _next_token(text, pos):
    """Find the earliest inline token at/after pos -> (kind, start, end, payload)."""
    best = None
    for kind, pat in (
        ("code", re.compile(r"`([^`]+)`")),
        ("link", re.compile(r"\[([^\]]*)\]\(([^)]+)\)")),
        ("bold", re.compile(r"\*\*(.+?)\*\*")),
        ("italic", re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")),
    ):
        m = pat.search(text, pos)
        if m and (best is None or m.start() < best[1]):
            best = (kind, m.start(), m.end(), m)
    return best


def add_inline(paragraph, text, size=10, color=INK_SOFT, base_bold=False, base_italic=False):
    """Recursive renderer for **bold**, *italic*, `code` and [label](url), incl. nesting."""
    pos = 0
    while True:
        tok = _next_token(text, pos)
        if tok is None:
            if pos < len(text):
                r = paragraph.add_run(text[pos:])
                r.font.size = Pt(size); r.font.color.rgb = color
                r.font.name = BODY_FONT; r.bold = base_bold; r.italic = base_italic
            return
        kind, start, end, m = tok
        if start > pos:
            r = paragraph.add_run(text[pos:start])
            r.font.size = Pt(size); r.font.color.rgb = color
            r.font.name = BODY_FONT; r.bold = base_bold; r.italic = base_italic

        if kind == "code":
            r = paragraph.add_run(m.group(1))
            r.font.name = "Consolas"; r.font.size = Pt(max(size - 0.8, 6.5))
            r.font.color.rgb = RGBColor(0x4A, 0x3A, 0x22)
            r.bold = base_bold; r.italic = base_italic
        elif kind == "link":
            label, url = m.group(1), m.group(2)
            if not label:
                label = re.sub(r"^https?://", "", url).rstrip("/")
            add_hyperlink(paragraph, label, url, size=max(size - 0.5, 7))
        elif kind == "bold":
            add_inline(paragraph, m.group(1), size=size, color=color,
                       base_bold=True, base_italic=base_italic)
        else:  # italic
            add_inline(paragraph, m.group(1), size=size, color=color,
                       base_bold=base_bold, base_italic=True)
        pos = end


# ---------------------------------------------------------------------------- document
doc = Document()

# base styles
normal = doc.styles["Normal"]
normal.font.name = BODY_FONT
normal.font.size = Pt(10)
normal.font.color.rgb = INK_SOFT
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.18

for name, size, color, before, after in (
    ("Heading 1", 19, INK, 22, 8),
    ("Heading 2", 14, INK, 16, 6),
    ("Heading 3", 11.5, GOLD, 12, 4),
    ("Heading 4", 10, INK, 10, 3),
):
    st = doc.styles[name]
    st.font.name = UI_FONT
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = color
    st.paragraph_format.space_before = Pt(before)
    st.paragraph_format.space_after = Pt(after)
    st.paragraph_format.keep_with_next = True

for nm in ("List Bullet", "List Bullet 2", "List Number"):
    st = doc.styles[nm]
    st.font.name = BODY_FONT
    st.font.size = Pt(10)
    st.font.color.rgb = INK_SOFT
    st.paragraph_format.space_after = Pt(3)

sec = doc.sections[0]
sec.top_margin = Inches(0.85)
sec.bottom_margin = Inches(0.8)
sec.left_margin = Inches(0.85)
sec.right_margin = Inches(0.85)
CONTENT_W = sec.page_width - sec.left_margin - sec.right_margin

# ------------------------------ cover
cover = doc.add_paragraph()
cover.paragraph_format.space_before = Pt(70)
cover.paragraph_format.space_after = Pt(2)
r = cover.add_run("WEBSITE & CATALOG REVIEW")
r.font.name = UI_FONT; r.font.size = Pt(9); r.bold = True
r.font.color.rgb = GOLD
r.font.all_caps = True
rpr = r._element.get_or_add_rPr()
sp = OxmlElement("w:spacing"); sp.set(qn("w:val"), "60")
_insert_ordered(rpr, sp, RPR_SEQ)

t = doc.add_paragraph()
t.paragraph_format.space_after = Pt(0)
r = t.add_run("Pro Black")
r.font.name = UI_FONT; r.font.size = Pt(46); r.bold = True; r.font.color.rgb = INK

st = doc.add_paragraph()
st.paragraph_format.space_after = Pt(4)
r = st.add_run("Full Website & Product Catalog Audit")
r.font.name = BODY_FONT; r.font.size = Pt(17); r.italic = True
r.font.color.rgb = RGBColor(0x5A, 0x53, 0x46)

site = doc.add_paragraph()
site.paragraph_format.space_after = Pt(26)
r = site.add_run("problack.co   ·   20 October 2026   ·   Independent review")
r.font.name = UI_FONT; r.font.size = Pt(9.5); r.font.color.rgb = MUTED
para_border(site, "bottom", "C9A45C", 10, 10)

# verdict callout
box = doc.add_table(rows=1, cols=1)
box.autofit = False
cell = box.rows[0].cells[0]
cell.width = CONTENT_W
shade(cell._tc, "F4EFE3")
cell.paragraphs[0].text = ""
p0 = cell.paragraphs[0]
p0.paragraph_format.space_before = Pt(8)
p0.paragraph_format.space_after = Pt(3)
r = p0.add_run("HEADLINE FINDING")
r.font.name = UI_FONT; r.font.size = Pt(8); r.bold = True; r.font.color.rgb = GOLD

p1 = cell.add_paragraph()
p1.paragraph_format.space_after = Pt(4)
r = p1.add_run(
    "The storefront looks credible, but the catalog does not support its central claim. "
    "Every product page examined sells via \u201cProBlack Team\u201d, the sampled inventory is "
    "platform- or mass-market-branded, and the 18 verified Black-owned businesses have no "
    "products in the shop."
)
r.font.name = BODY_FONT; r.font.size = Pt(10); r.font.color.rgb = INK

p2 = cell.add_paragraph()
p2.paragraph_format.space_after = Pt(8)
r = p2.add_run("Grade: D  —  not launch-ready in its current form")
r.font.name = UI_FONT; r.font.size = Pt(9.5); r.bold = True; r.font.color.rgb = RED

# meta grid
doc.add_paragraph().paragraph_format.space_after = Pt(10)
meta = [
    ("Scope", "Public site, catalog, directory, content, policies, SEO, security, apps"),
    ("Evidence", "40+ pages, 105 listings across 13 views, 8 sitemaps, 2 app stores"),
    ("Companion", "product-sample-audit.csv  ·  md and html versions of this report"),
    ("Status", "Point-in-time snapshot — prices and content change"),
]
mt = doc.add_table(rows=0, cols=2)
mt.autofit = False
for k, v in meta:
    row = mt.add_row()
    c0, c1 = row.cells
    c0.width = Inches(1.15); c1.width = CONTENT_W - Inches(1.15)
    pk = c0.paragraphs[0]; pk.paragraph_format.space_after = Pt(3)
    rk = pk.add_run(k.upper())
    rk.font.name = UI_FONT; rk.font.size = Pt(7.5); rk.bold = True
    rk.font.color.rgb = GOLD
    pv = c1.paragraphs[0]; pv.paragraph_format.space_after = Pt(3)
    add_inline(pv, v, size=9, color=INK_SOFT)

# ------------------------------ contents (manual, reliable)
doc.add_page_break()
h = doc.add_paragraph()
h.paragraph_format.space_before = Pt(6)
h.paragraph_format.space_after = Pt(10)
r = h.add_run("Contents")
r.font.name = UI_FONT; r.font.size = Pt(17); r.bold = True; r.font.color.rgb = INK
para_border(h, "bottom", "C9A45C", 8, 8)

SECTIONS = [
    "1. Executive summary",
    "2. Method, scope and limitations",
    "3. Scorecard",
    "4. Catalog audit: what is actually for sale",
    "5. Pricing and promotions",
    "6. Product page content and UX",
    "7. Category, browse and search architecture",
    "8. Claims, statistics and social proof",
    "9. Business directory and services",
    "10. Legal, policy and compliance",
    "11. SEO",
    "12. Performance and technical delivery",
    "13. Security and privacy",
    "14. Accessibility",
    "15. Mobile apps and cross-channel consistency",
    "16. Support and operations",
    "17. Content and blog",
    "18. What is working",
    "19. Prioritised remediation plan",
    "20. Appendices",
]
ct = doc.add_table(rows=0, cols=2)
ct.autofit = False
for i, name in enumerate(SECTIONS):
    row = ct.add_row()
    c0, c1 = row.cells
    c0.width = Inches(0.4); c1.width = CONTENT_W - Inches(0.4)
    pn = c0.paragraphs[0]; pn.paragraph_format.space_after = Pt(2)
    rn = pn.add_run(str(i + 1))
    rn.font.name = UI_FONT; rn.font.size = Pt(8.5); rn.bold = True; rn.font.color.rgb = GOLD
    pv = c1.paragraphs[0]; pv.paragraph_format.space_after = Pt(2)
    add_inline(pv, name.split(". ", 1)[1], size=9.5, color=INK_SOFT)

note = doc.add_paragraph()
note.paragraph_format.space_before = Pt(16)
add_inline(
    note,
    "*Prepared from public pages only. Nothing in this document is legal advice. "
    "Severity ratings reflect consumer-protection and revenue impact.*",
    size=8.5, color=MUTED,
)

# ------------------------------ body
raw = open(SRC, encoding="utf-8").read()
# strip title/meta block and manual contents
raw = re.sub(r"\A# .*?\n---\n", "", raw, flags=re.S)
raw = re.sub(r"## Contents\n.*?\n---\n", "", raw, flags=re.S)

lines = raw.split("\n")
doc.add_page_break()

i = 0
first_h2 = True
while i < len(lines):
    line = lines[i].rstrip()
    stripped = line.strip()

    # blank
    if not stripped:
        i += 1
        continue

    # horizontal rule -> section break spacer
    if stripped == "---":
        if not first_h2:
            sp = doc.add_paragraph()
            sp.paragraph_format.space_before = Pt(0)
            sp.paragraph_format.space_after = Pt(2)
            para_border(sp, "bottom", "DDD7C9", 4, 1)
        i += 1
        continue

    # fenced code
    if stripped.startswith("```"):
        i += 1
        buf = []
        while i < len(lines) and not lines[i].strip().startswith("```"):
            buf.append(lines[i])
            i += 1
        i += 1
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.12)
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing = 1.0
        para_shade(p, "1B1915")
        for j, bl in enumerate(buf):
            if j:
                p.add_run().add_break()
            r = p.add_run(bl.replace("\t", "    "))
            r.font.name = "Consolas"; r.font.size = Pt(8)
            r.font.color.rgb = RGBColor(0xEF, 0xE8, 0xDA)
        i += 1
        continue

    # headings
    m = re.match(r"^(#{2,4})\s+(.*)$", stripped)
    if m:
        level = len(m.group(1)) - 1
        text = m.group(2)
        style = {1: "Heading 1", 2: "Heading 2", 3: "Heading 3"}[level]
        if level == 1:
            if not first_h2:
                doc.add_page_break()
            first_h2 = False
        p = doc.add_paragraph(style=style)
        add_inline(p, text, size={1: 19, 2: 14, 3: 11.5}[level],
                   color={1: INK, 2: INK, 3: GOLD}[level], base_bold=True)
        for r in p.runs:
            r.bold = True
            r.font.name = UI_FONT
        if level == 1:
            para_border(p, "bottom", "C9A45C", 8, 6)
        i += 1
        continue

    # tables
    if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
        header = [c.strip() for c in stripped.strip("|").split("|")]
        i += 2
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
            i += 1
        ncol = len(header)
        table = doc.add_table(rows=1, cols=ncol)
        table.style = "Table Grid"
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell_margins(table)

        # column widths: first col narrow-ish if numeric
        base = CONTENT_W / ncol
        widths = []
        for ci in range(ncol):
            w = base
            if ncol >= 5 and ci == 0:
                w = Inches(0.32)
            elif ncol == 4 and ci == 0:
                w = Inches(0.34)
            elif ncol == 2 and ci == 0:
                w = Inches(2.05)
            elif ncol == 3 and ci == 0:
                w = Inches(1.35)
            widths.append(w)
        total = sum(widths)
        widths = [w * (CONTENT_W / total) for w in widths]

        hdr = table.rows[0]
        repeat_header(hdr); no_split(hdr)
        for ci, txt in enumerate(header):
            cell = hdr.cells[ci]
            cell.width = widths[ci]
            shade(cell._tc, "F1EADB")
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            r = p.add_run(txt)
            r.font.name = UI_FONT; r.font.size = Pt(8); r.bold = True; r.font.color.rgb = INK

        for row in rows:
            tr = table.add_row()
            no_split(tr)
            for ci in range(ncol):
                cell = tr.cells[ci]
                cell.width = widths[ci]
                txt = row[ci] if ci < len(row) else ""
                p = cell.paragraphs[0]
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                sev = txt.strip().strip("*")
                if sev in ("Critical", "High", "Medium", "Low"):
                    r = p.add_run(sev.upper())
                    r.font.name = UI_FONT; r.font.size = Pt(7.5); r.bold = True
                    r.font.color.rgb = {"Critical": RED, "High": AMBER,
                                        "Medium": MUTED, "Low": MUTED}[sev]
                elif sev in ("A", "B", "C", "C\u2212", "D", "F"):
                    r = p.add_run(sev)
                    r.font.name = UI_FONT; r.font.size = Pt(10); r.bold = True
                    r.font.color.rgb = {"A": GREEN, "B": GREEN, "C": GOLD,
                                        "C\u2212": GOLD, "D": AMBER, "F": RED}[sev]
                else:
                    add_inline(p, txt, size=8, color=INK_SOFT)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        continue

    # blockquote
    if stripped.startswith(">"):
        buf = []
        while i < len(lines) and lines[i].strip().startswith(">"):
            buf.append(lines[i].strip().lstrip(">").strip())
            i += 1
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.22)
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(8)
        para_shade(p, "F7F3E9")
        para_border(p, "left", "C9A45C", 18, 8)
        add_inline(p, " ".join(x for x in buf if x), size=9.5, color=INK_SOFT, base_italic=True)
        i += 1
        continue

    # numbered list
    m = re.match(r"^(\d+)\.\s+(.*)$", stripped)
    if m:
        p = doc.add_paragraph(style="List Number")
        add_inline(p, m.group(2), size=10)
        i += 1
        continue

    # bullets (support nesting)
    m = re.match(r"^(\s*)-\s+(.*)$", line)
    if m:
        indent = len(m.group(1))
        style = "List Bullet 2" if indent >= 2 else "List Bullet"
        p = doc.add_paragraph(style=style)
        add_inline(p, m.group(2), size=10)
        i += 1
        continue

    # paragraph (join wrapped lines)
    buf = [stripped]
    i += 1
    while i < len(lines):
        nxt = lines[i].strip()
        if (not nxt or nxt.startswith(("#", "|", ">", "-", "```", "---"))
                or re.match(r"^\d+\.\s", nxt)):
            break
        buf.append(nxt)
        i += 1
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    add_inline(p, " ".join(buf), size=10)

# ------------------------------ header & footer
body_sec = doc.sections[0]
body_sec.different_first_page_header_footer = True   # clean cover page
hdr = body_sec.header
hp = hdr.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
rp = hp.add_run("Pro Black  ·  Website & Product Catalog Audit  ·  20 October 2026")
rp.font.name = UI_FONT; rp.font.size = Pt(7.5); rp.font.color.rgb = MUTED
para_border(hp, "bottom", "E2DCCC", 4, 4)

ftr = body_sec.footer
fp = ftr.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r1 = fp.add_run("Page ")
r1.font.name = UI_FONT; r1.font.size = Pt(8); r1.font.color.rgb = MUTED
add_field(fp, "PAGE", 8)
r2 = fp.add_run(" of ")
r2.font.name = UI_FONT; r2.font.size = Pt(8); r2.font.color.rgb = MUTED
add_field(fp, "NUMPAGES", 8)

# core properties
doc.core_properties.title = "Pro Black — Full Website & Product Catalog Audit"
doc.core_properties.subject = "Independent audit of problack.co, 20 October 2026"
doc.core_properties.author = "Independent review"
doc.core_properties.category = "Website & catalog audit"
doc.core_properties.comments = "Companion dataset: product-sample-audit.csv"

doc.save(OUT)
print("saved", OUT)

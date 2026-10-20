#!/usr/bin/env python3
"""Build a print-ready PDF of the Pro Black audit from the Markdown source.

Design mirrors the DOCX/HTML editions: dark cover, gold rules, shaded table
headers, severity badges, running header and "Page X of Y" footer.
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, PageBreak, Table, TableStyle, KeepTogether,
                                Preformatted, HRFlowable, NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "assets", "fonts")
SRC = os.path.join(HERE, "Pro-Black-Website-Audit-2026-10-20.md")
OUT = os.path.join(HERE, "Pro-Black-Website-Audit-2026-10-20.pdf")

# ------------------------------------------------------------------ palette
INK      = colors.HexColor("#151412")
INK_2    = colors.HexColor("#3D3A35")
MUTED    = colors.HexColor("#6B665E")
RULE     = colors.HexColor("#DDD7C9")
GOLD     = colors.HexColor("#8A5A12")
GOLD_2   = colors.HexColor("#C9A45C")
PAPER    = colors.HexColor("#FFFFFF")
CREAM    = colors.HexColor("#F4EFE3")
CREAM_2  = colors.HexColor("#F7F3E9")
HDR_FILL = colors.HexColor("#F1EADB")
RED      = colors.HexColor("#A52A24")
AMBER    = colors.HexColor("#8A5310")
GREEN    = colors.HexColor("#1F6F43")

PAGE_W, PAGE_H = A4
LM = RM = 52
TM, BM = 56, 52
CONTENT_W = PAGE_W - LM - RM

# ------------------------------------------------------------------ fonts
def reg(name, file):
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, file)))

reg("Serif", "IBMPlexSerif-Regular.ttf")
reg("Serif-It", "IBMPlexSerif-Italic.ttf")
reg("Serif-Bold", "IBMPlexSerif-Bold.ttf")
reg("Serif-BoldIt", "IBMPlexSerif-BoldItalic.ttf")
reg("Serif-Semi", "IBMPlexSerif-SemiBold.ttf")
reg("Sans", "IBMPlexSans-Regular.ttf")
reg("Sans-It", "IBMPlexSans-Italic.ttf")
reg("Sans-Med", "IBMPlexSans-Medium.ttf")
reg("Sans-Semi", "IBMPlexSans-SemiBold.ttf")
reg("Sans-Bold", "IBMPlexSans-Bold.ttf")
reg("Mono", "IBMPlexMono-Regular.ttf")
reg("Mono-Bold", "IBMPlexMono-Bold.ttf")
reg("Star", "DejaVuSans.ttf") if os.path.exists(os.path.join(FONTS, "DejaVuSans.ttf")) else None
if not os.path.exists(os.path.join(FONTS, "DejaVuSans.ttf")):
    pdfmetrics.registerFont(TTFont("Star", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))

pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold",
                              italic="Serif-It", boldItalic="Serif-BoldIt")
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold",
                              italic="Sans-It", boldItalic="Sans-Bold")
pdfmetrics.registerFontFamily("Mono", normal="Mono", bold="Mono-Bold",
                              italic="Mono", boldItalic="Mono-Bold")

# ------------------------------------------------------------------ styles
S = {}
S["body"] = ParagraphStyle("body", fontName="Serif", fontSize=9.6, leading=14.2,
                           textColor=INK_2, spaceAfter=6, alignment=TA_LEFT)
S["body_first"] = ParagraphStyle("body_first", parent=S["body"])
S["h1"] = ParagraphStyle("h1", fontName="Serif-Bold", fontSize=19, leading=23,
                         textColor=INK, spaceBefore=0, spaceAfter=4, keepWithNext=1)
S["h2"] = ParagraphStyle("h2", fontName="Sans-Semi", fontSize=11.6, leading=15,
                         textColor=INK, spaceBefore=13, spaceAfter=4, keepWithNext=1)
S["h3"] = ParagraphStyle("h3", fontName="Sans-Semi", fontSize=9.6, leading=13,
                         textColor=GOLD, spaceBefore=9, spaceAfter=3, keepWithNext=1)
S["bullet"] = ParagraphStyle("bullet", parent=S["body"], leftIndent=13, bulletIndent=3,
                             spaceAfter=3.2, bulletFontName="Serif", bulletFontSize=9.6)
S["bullet2"] = ParagraphStyle("bullet2", parent=S["body"], leftIndent=27, bulletIndent=17,
                              spaceAfter=3.2, bulletFontName="Serif", bulletFontSize=9.6)
S["cell"] = ParagraphStyle("cell", fontName="Sans", fontSize=7.2, leading=9.4, textColor=INK_2)
S["cellh"] = ParagraphStyle("cellh", fontName="Sans-Semi", fontSize=7.2, leading=9.4, textColor=INK)
S["quote"] = ParagraphStyle("quote", fontName="Serif-It", fontSize=9.2, leading=13.4,
                            textColor=INK_2)
S["codelbl"] = ParagraphStyle("codelbl", fontName="Mono", fontSize=7.4, leading=10.2,
                              textColor=colors.HexColor("#EFE8DA"))
S["toc0"] = ParagraphStyle("toc0", fontName="Sans", fontSize=9.2, leading=17,
                           textColor=INK_2, leftIndent=0, firstLineIndent=0)
S["toc0n"] = ParagraphStyle("toc0n", fontName="Sans-Semi", fontSize=9.2, leading=17,
                            textColor=INK, leftIndent=0, firstLineIndent=0)
S["toc_title"] = ParagraphStyle("toc_title", fontName="Serif-Bold", fontSize=18, leading=22,
                                textColor=INK, spaceAfter=14)

# ------------------------------------------------------------------ inline markup
def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


TOKEN = re.compile(r"`([^`]+)`|\[([^\]]*)\]\(([^)]+)\)|\*\*(.+?)\*\*|(?<!\*)\*([^*\n]+)\*(?!\*)")


def rich(text, size=None, color=None):
    """Markdown inline -> ReportLab markup (recursive, handles nesting)."""
    out = []
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            out.append(esc(text[pos:m.start()]))
        code, label, url, bold, ital = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
        if code is not None:
            out.append(f'<font name="Mono" color="#4A3A22">{esc(code)}</font>')
        elif url is not None:
            lab = label or re.sub(r"^https?://", "", url).rstrip("/")
            out.append(f'<link href="{esc(url)}"><font color="#8A5A12">{esc(lab)}</font></link>')
        elif bold is not None:
            out.append(f"<b>{rich(bold, size, color)}</b>")
        else:
            out.append(f"<i>{rich(ital, size, color)}</i>")
        pos = m.end()
    if pos < len(text):
        out.append(esc(text[pos:]))
    s = "".join(out)
    s = s.replace("\u2605", '<font name="Star">\u2605</font>')
    if size or color:
        attrs = []
        if size:
            attrs.append(f'size="{size}"')
        if color:
            attrs.append(f'color="{color}"')
        s = f"<font {' '.join(attrs)}>{s}</font>"
    return s



def tracked(c, x, y, text, font, size, color, tracking=0.0):
    """Draw text with letter-spacing, then reset Tc so later text is unaffected."""
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setCharSpace(tracking)
    t.setFillColor(color)
    t.textOut(text)
    t.setCharSpace(0)          # emit a trailing Tc 0 so the state does not leak
    c.drawText(t)
    c._charSpace = 0           # keep reportlab's own bookkeeping in sync


# ------------------------------------------------------------------ doc template
class AuditDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, **kw)
        frame = Frame(LM, BM, CONTENT_W, PAGE_H - TM - BM, id="body",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cover", frames=[frame], onPage=self.cover),
                               PageTemplate(id="body", frames=[frame], onPage=self.deco)])

    # -- page furniture ---------------------------------------------------
    def cover(self, c, doc):
        c.saveState()
        band_h = PAGE_H - 250
        c.setFillColor(colors.HexColor("#17150F"))
        c.rect(0, PAGE_H - 268, PAGE_W, 268, stroke=0, fill=1)
        c.setFillColor(GOLD_2)
        c.rect(0, PAGE_H - 271, PAGE_W, 3, stroke=0, fill=1)

        tracked(c, LM, PAGE_H - 92, "WEBSITE & CATALOG REVIEW", "Sans-Semi", 7.6,
                colors.HexColor("#C9A45C"), 2.6)

        c.setFillColor(colors.white)
        c.setFont("Serif-Bold", 44)
        c.drawString(LM, PAGE_H - 146, "Pro Black")

        c.setFillColor(colors.HexColor("#E4D9C4"))
        c.setFont("Serif-It", 16.5)
        c.drawString(LM, PAGE_H - 172, "Full Website & Product Catalog Audit")

        c.setFillColor(colors.HexColor("#B8AE9C"))
        c.setFont("Sans", 8.2)
        c.drawString(LM, PAGE_H - 200, "problack.co    ·    20 October 2026    ·    Independent review")

        # verdict box
        top = PAGE_H - 320
        box_h = 118
        c.setFillColor(CREAM)
        c.rect(LM, top - box_h, CONTENT_W, box_h, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(LM, top - box_h, 3, box_h, stroke=0, fill=1)

        tracked(c, LM + 16, top - 20, "HEADLINE FINDING", "Sans-Semi", 7.2, GOLD, 1.8)

        txt = ("The storefront looks credible, but the catalog does not support its central claim. "
               "Every product page examined sells via \u201cProBlack Team\u201d, the sampled inventory is "
               "platform- or mass-market-branded, and the 18 verified Black-owned businesses have no "
               "products in the shop.")
        p = Paragraph(f'<font name="Serif" size="9.6" color="#151412">{esc(txt)}</font>',
                      ParagraphStyle("cv", fontName="Serif", fontSize=9.6, leading=13.6))
        w, h = p.wrap(CONTENT_W - 34, box_h)
        p.drawOn(c, LM + 16, top - 34 - h)

        c.setFillColor(RED)
        c.setFont("Sans-Bold", 9)
        c.drawString(LM + 16, top - box_h + 14, "GRADE: D   —   NOT LAUNCH-READY IN ITS CURRENT FORM")

        # meta block
        y = top - box_h - 34
        rows = [("SCOPE", "Public site, catalog, directory, content, policies, SEO, security, apps"),
                ("EVIDENCE", "40+ pages · 105 listings · 8 sitemaps · 2 app-store listings"),
                ("STATUS", "Point-in-time snapshot, 20 October 2026 — prices and content change"),
                ("NOTE", "Prepared from public pages only. Not legal advice.")]
        for k, v in rows:
            tracked(c, LM, y, k, "Sans-Semi", 6.8, GOLD, 1.2)
            c.setFillColor(INK_2)
            c.setFont("Serif", 8.8)
            c.drawString(LM + 78, y, v)
            y -= 17

        c.setStrokeColor(RULE)
        c.setLineWidth(0.5)
        c.line(LM, BM + 16, PAGE_W - RM, BM + 16)
        c.setFillColor(MUTED)
        c.setFont("Sans", 7)
        c.drawString(LM, BM + 2, "Pro Black — Full Website & Product Catalog Audit")
        c.drawRightString(PAGE_W - RM, BM + 2, "problack.co")
        c.restoreState()

    def deco(self, c, doc):
        c.saveState()
        # header
        c.setFont("Sans", 6.9)
        c.setFillColor(MUTED)
        c.drawString(LM, PAGE_H - 34, "PRO BLACK")
        c.drawRightString(PAGE_W - RM, PAGE_H - 34, "WEBSITE & PRODUCT CATALOG AUDIT  ·  20 OCT 2026")
        c.setStrokeColor(RULE)
        c.setLineWidth(0.5)
        c.line(LM, PAGE_H - 39, PAGE_W - RM, PAGE_H - 39)
        # footer
        c.setStrokeColor(RULE)
        c.line(LM, BM - 18, PAGE_W - RM, BM - 18)
        c.setFont("Sans", 6.9)
        c.setFillColor(MUTED)
        c.drawString(LM, BM - 31, "Independent audit · prepared from public pages only · not legal advice")
        c.drawRightString(PAGE_W - RM, BM - 31, f"{doc.page - 1}")
        c.restoreState()

    # -- TOC ---------------------------------------------------------------
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name == "h1":
            txt = re.sub(r"<[^>]+>", "", flowable.getPlainText())
            self.notify("TOCEntry", (0, txt, self.page - 1))


# ------------------------------------------------------------------ parsing
def build_story(md_text):
    md_text = re.sub(r"\A# .*?\n---\n", "", md_text, flags=re.S)
    md_text = re.sub(r"## Contents\n.*?\n---\n", "", md_text, flags=re.S)
    lines = md_text.split("\n")
    story = []
    i, first_h1 = 0, True

    def para(text, style="body"):
        return Paragraph(rich(text), S[style])

    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()

        if not s:
            i += 1
            continue

        if s == "---":
            i += 1
            continue

        # code fence
        if s.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            pre = Preformatted("\n".join(buf), S["codelbl"], maxLineLength=118)
            box = Table([[pre]], colWidths=[CONTENT_W])
            box.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1B1915")),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]))
            story += [box, Spacer(1, 7)]
            continue

        # headings
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            level = len(m.group(1)) - 1
            text = m.group(2)
            if level == 1:
                story.append(PageBreak())
                first_h1 = False
                story.append(Paragraph(rich(text), S["h1"]))
                story.append(HRFlowable(width="100%", thickness=1.6, color=GOLD_2,
                                        spaceBefore=1, spaceAfter=9, hAlign="LEFT"))
            elif level == 2:
                story.append(Paragraph(rich(text), S["h2"]))
            else:
                story.append(Paragraph(rich(text), S["h3"]))
            i += 1
            continue

        # table
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            story += [build_table(header, rows), Spacer(1, 8)]
            continue

        # blockquote
        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            txt = " ".join(x for x in buf if x)
            q = Paragraph(rich(txt), S["quote"])
            box = Table([[q]], colWidths=[CONTENT_W])
            box.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), CREAM_2),
                ("LINEBEFORE", (0, 0), (0, -1), 3, GOLD_2),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]))
            story += [box, Spacer(1, 7)]
            continue

        # numbered list
        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m:
            story.append(Paragraph(rich(m.group(2)), S["bullet"], bulletText=f"{m.group(1)}."))
            i += 1
            continue

        # bullets
        m = re.match(r"^(\s*)-\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            style = "bullet2" if lvl >= 2 else "bullet"
            story.append(Paragraph(rich(m.group(2)), S[style], bulletText="•" if lvl < 2 else "–"))
            i += 1
            continue

        # paragraph
        buf = [s]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith(("#", "|", ">", "-", "```", "---"))
                    or re.match(r"^\d+\.\s", nxt)):
                break
            buf.append(nxt)
            i += 1
        story.append(para(" ".join(buf)))

    return story


BADGES = {"Critical", "High", "Medium", "Low", "A", "B", "C", "C\u2212", "D", "F"}


def col_weights(header, rows, ncol):
    lens, fixed = [], {}
    for ci in range(ncol):
        vals = [r[ci] for r in rows if ci < len(r)]
        vals = [re.sub(r"[*`\[\]()]", "", v).strip() for v in vals if v.strip()]
        if vals and all(v in BADGES for v in vals):
            fixed[ci] = 34.0          # badge / grade column
            lens.append(0)
            continue
        vals.sort(key=len)
        med = vals[len(vals) // 2] if vals else ""
        L = max(len(header[ci]) if ci < len(header) else 8, len(med), 6)
        lens.append(min(L, 90) ** 0.72)

    # widen badge columns just enough for the header text
    for ci, w in list(fixed.items()):
        if ci < len(header):
            need = pdfmetrics.stringWidth(header[ci], "Sans-Semi", 7.2) + 14
            fixed[ci] = max(w, need)

    remaining = CONTENT_W - sum(fixed.values())
    total = sum(lens) or 1
    out = []
    for ci in range(ncol):
        if ci in fixed:
            out.append(fixed[ci])
        else:
            out.append(max(28.0, min(remaining * 0.62, remaining * lens[ci] / total)))
    # normalise non-fixed columns to exactly fill the remainder
    flex = [i for i in range(ncol) if i not in fixed]
    used = sum(fixed.values())
    fsum = sum(out[i] for i in flex) or 1
    for i in flex:
        out[i] = out[i] / fsum * (CONTENT_W - used)
    return out


def build_table(header, rows):
    ncol = len(header)
    widths = col_weights(header, rows, ncol)

    data = [[Paragraph(rich(h), S["cellh"]) for h in header]]
    sev_style = {}
    for ri, r in enumerate(rows, start=1):
        cells = []
        for ci in range(ncol):
            raw = r[ci] if ci < len(r) else ""
            key = raw.strip().strip("*")
            if key in ("Critical", "High", "Medium", "Low"):
                colr = {"Critical": "#A52A24", "High": "#8A5310",
                        "Medium": "#6B665E", "Low": "#6B665E"}[key]
                cells.append(Paragraph(
                    f'<font name="Sans-Semi" size="6.9" color="{colr}">{key}</font>',
                    S["cell"]))
            elif key in ("A", "B", "C", "C\u2212", "D", "F"):
                colr = {"A": "#1F6F43", "B": "#1F6F43", "C": "#8A5A12",
                        "C\u2212": "#8A5A12", "D": "#8A5310", "F": "#A52A24"}[key]
                cells.append(Paragraph(
                    f'<font name="Sans-Bold" size="9" color="{colr}">{esc(key)}</font>', S["cell"]))
            else:
                cells.append(Paragraph(rich(raw), S["cell"]))
        data.append(cells)

    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), HDR_FILL),
        ("TEXTCOLOR", (0, 0), (-1, 0), INK),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, colors.HexColor("#D6CCB8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
    ]
    for ri in range(1, len(data)):
        if ri % 2 == 0:
            style.append(("BACKGROUND", (0, ri), (-1, ri), colors.HexColor("#FBF9F4")))
    t.setStyle(TableStyle(style))
    return t


# ------------------------------------------------------------------ build
md = open(SRC, encoding="utf-8").read()

doc = AuditDoc(OUT, pagesize=A4,
               leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
               title="Pro Black — Full Website & Product Catalog Audit",
               author="Independent review",
               subject="Audit of problack.co, 20 October 2026",
               creator="build_pdf.py")

story = [NextPageTemplate("body"), PageBreak()]
story.append(Paragraph("Contents", S["toc_title"]))
story.append(HRFlowable(width="100%", thickness=1.6, color=GOLD_2, spaceAfter=12, hAlign="LEFT"))

toc = TableOfContents()
toc.levelStyles = [ParagraphStyle("toc0", fontName="Sans", fontSize=9.2, leading=17.5,
                                  textColor=INK_2, leftIndent=6, firstLineIndent=-6)]
toc.dotsMinLevel = 0
story.append(toc)

story += build_story(md)

doc.multiBuild(story)
try:
    for e in toc._lastEntries:
        print("TOC", e)
except Exception as ex:
    print("no entry dump:", ex)
print("saved", OUT)

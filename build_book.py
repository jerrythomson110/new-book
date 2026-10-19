# -*- coding: utf-8 -*-
"""Build 'Old, Old Tales Retold — Restored Edition' (A4, print-ready PDF)."""
import re
from pathlib import Path
from PIL import Image as PILImage

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, PageBreak, NextPageTemplate,
                                KeepTogether, Flowable, Table, TableStyle, HRFlowable)

from book_content import (BOOK_TITLE, BOOK_SUBTITLE, ILLUSTRATOR, DEDICATION,
                          DEDICATION_TO, INTRO_TITLE, INTRO_PAGES, STORIES,
                          LINE_ART_PAGES)

ROOT = Path(__file__).parent
AST = ROOT / "book_assets"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
FONTS = ROOT / "fonts"

PAGE_W, PAGE_H = A4
CREAM = colors.HexColor("#FBF6E9")
INK = colors.HexColor("#2B2118")
BROWN = colors.HexColor("#8A5A2B")
LIGHT_BROWN = colors.HexColor("#B98A4E")
BLUE = colors.HexColor("#24465E")
BLUE_DARK = colors.HexColor("#1C364A")
GOLD = colors.HexColor("#D9A441")
CREAM_TEXT = colors.HexColor("#F5EDD6")

pdfmetrics.registerFont(TTFont("Fell", str(FONTS / "im-fell-english-latin-400-normal.ttf")))
pdfmetrics.registerFont(TTFont("Fell-Italic", str(FONTS / "im-fell-english-latin-400-italic.ttf")))
pdfmetrics.registerFont(TTFont("FellSC", str(FONTS / "im-fell-english-sc-latin-400-normal.ttf")))
pdfmetrics.registerFont(TTFont("Garamond", str(FONTS / "eb-garamond-latin-400-normal.ttf")))
pdfmetrics.registerFont(TTFont("Garamond-Medium", str(FONTS / "eb-garamond-latin-500-normal.ttf")))
pdfmetrics.registerFont(TTFont("Garamond-SemiBold", str(FONTS / "eb-garamond-latin-600-normal.ttf")))
pdfmetrics.registerFont(TTFont("Garamond-Italic", str(FONTS / "eb-garamond-latin-400-italic.ttf")))

FRAME_X, FRAME_Y = 54, 58
FRAME_W = PAGE_W - 2 * FRAME_X
FRAME_H = PAGE_H - FRAME_Y - 52


# ---------------- styles ----------------
def st(name, **kw):
    base = dict(name=name, fontName="Garamond-Medium", textColor=INK, fontSize=14.8, leading=20.5)
    base.update(kw)
    return ParagraphStyle(**base)


S = {
    "RunHead": st("RunHead", fontName="FellSC", fontSize=10.5, leading=13, alignment=TA_CENTER,
                  textColor=BROWN, spaceAfter=8),
    "Body": st("Body", alignment=TA_LEFT, firstLineIndent=16, spaceAfter=7),
    "BodyFirst": st("BodyFirst", alignment=TA_LEFT, firstLineIndent=0, spaceAfter=7),
    "Dialogue": st("Dialogue", alignment=TA_LEFT, firstLineIndent=0, leftIndent=10, spaceAfter=7),
    "Verse": st("Verse", alignment=TA_LEFT, leftIndent=52, firstLineIndent=-16, spaceAfter=1.5, leading=20),
    "BodyD": st("BodyD", alignment=TA_LEFT, firstLineIndent=15, spaceAfter=5, fontSize=13.4, leading=18.2),
    "BodyFirstD": st("BodyFirstD", alignment=TA_LEFT, firstLineIndent=0, spaceAfter=5, fontSize=13.4, leading=18.2),
    "DialogueD": st("DialogueD", alignment=TA_LEFT, firstLineIndent=0, leftIndent=9, spaceAfter=5, fontSize=13.4, leading=18.2),
    "VerseD": st("VerseD", alignment=TA_LEFT, leftIndent=48, firstLineIndent=-15, spaceAfter=1, fontSize=13.4, leading=17.8),
    "IntroHead": st("IntroHead", fontName="FellSC", fontSize=19, leading=23, alignment=TA_CENTER, spaceAfter=14),
    "Intro": st("Intro", alignment=TA_JUSTIFY, firstLineIndent=16, spaceAfter=8, fontSize=13.8, leading=19.5),
    "IntroFirst": st("IntroFirst", alignment=TA_JUSTIFY, firstLineIndent=0, spaceAfter=8, fontSize=13.8, leading=19.5),
    "StoryKicker": st("StoryKicker", fontName="FellSC", fontSize=11, leading=14, alignment=TA_CENTER,
                      textColor=BROWN, spaceAfter=16),
    "StoryTitle": st("StoryTitle", fontName="FellSC", fontSize=27, leading=31, alignment=TA_CENTER, spaceBefore=18),
    "EndTitle": st("EndTitle", fontName="FellSC", fontSize=30, leading=34, alignment=TA_CENTER, spaceAfter=16),
    "Center": st("Center", alignment=TA_CENTER, firstLineIndent=0, spaceAfter=7),
    "CenterItalic": st("CenterItalic", fontName="Garamond-Italic", alignment=TA_CENTER, fontSize=14.5, leading=20, spaceAfter=7),
    "Small": st("Small", alignment=TA_CENTER, fontSize=10.5, leading=15, textColor=colors.HexColor("#5A4A38"), spaceAfter=5),
    "SmallLeft": st("SmallLeft", alignment=TA_LEFT, fontSize=10.5, leading=15.5, textColor=colors.HexColor("#5A4A38"), spaceAfter=6),
    "ContentsTitle": st("ContentsTitle", fontName="FellSC", fontSize=24, leading=28, alignment=TA_CENTER, spaceAfter=6),
    "TOCItem": st("TOCItem", fontName="Fell", fontSize=15.5, leading=20, textColor=INK),
    "TOCPage": st("TOCPage", fontName="Garamond-Medium", fontSize=13, leading=20, textColor=BROWN, alignment=1),
    "Dedication": st("Dedication", fontName="Fell-Italic", fontSize=16.5, leading=24, alignment=TA_CENTER),
    "DedicationTo": st("DedicationTo", fontName="FellSC", fontSize=20, leading=26, alignment=TA_CENTER, spaceBefore=14),
    "BackHead": st("BackHead", fontName="FellSC", fontSize=22, leading=27, alignment=TA_CENTER, textColor=GOLD, spaceAfter=12),
    "BackBody": st("BackBody", fontName="Garamond-Medium", fontSize=13.5, leading=19.5, alignment=TA_CENTER,
                   textColor=CREAM_TEXT, spaceAfter=8),
    "BackList": st("BackList", fontName="Fell", fontSize=14.5, leading=21, alignment=TA_CENTER, textColor=CREAM_TEXT),
}


class Ornament(Flowable):
    """— ◆ — rule drawn as lines + diamond (font-glyph safe)."""
    def __init__(self, width=150, color=BROWN, space_after=10, space_before=4):
        super().__init__()
        self.w, self.color = width, color
        self.space_after, self.space_before = space_after, space_before
        self.height = 10 + space_after + space_before

    def wrap(self, aw, ah):
        return aw, self.height

    def draw(self):
        c = self.canv
        y = self.space_after + 4
        cx = (FRAME_W) / 2 if self.width else 0
        # flowable is drawn at frame x=0..FRAME_W locally? ReportLab translates to x; use available width stored
        total = getattr(self, "_aw", FRAME_W)
        cx = total / 2
        half = self.w / 2
        c.saveState()
        c.setStrokeColor(self.color); c.setFillColor(self.color); c.setLineWidth(0.7)
        c.line(cx - half, y, cx - 12, y)
        c.line(cx + 12, y, cx + half, y)
        p = c.beginPath()
        p.moveTo(cx, y + 4.5); p.lineTo(cx + 4.5, y); p.lineTo(cx, y - 4.5); p.lineTo(cx - 4.5, y); p.close()
        c.drawPath(p, stroke=0, fill=1)
        c.circle(cx - 20, y, 1.4, stroke=0, fill=1)
        c.circle(cx + 20, y, 1.4, stroke=0, fill=1)
        c.restoreState()

    def wrap(self, aw, ah):  # noqa: D102 (override keeping aw)
        self._aw = aw
        return aw, self.height


# ---------------- page drawing ----------------
def draw_border(c, inset=27):
    c.saveState()
    c.setStrokeColor(LIGHT_BROWN)
    c.setLineWidth(0.8)
    c.rect(inset, inset, PAGE_W - 2 * inset, PAGE_H - 2 * inset, stroke=1, fill=0)
    c.setLineWidth(0.35)
    c.rect(inset + 3.5, inset + 3.5, PAGE_W - 2 * inset - 7, PAGE_H - 2 * inset - 7, stroke=1, fill=0)
    c.setFillColor(BROWN)
    for x in (inset, PAGE_W - inset):
        for y in (inset, PAGE_H - inset):
            p = c.beginPath()
            p.moveTo(x, y + 4); p.lineTo(x + 4, y); p.lineTo(x, y - 4); p.lineTo(x - 4, y); p.close()
            c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def on_front(c, doc):
    c.saveState(); c.setFillColor(CREAM); c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1); c.restoreState()
    draw_border(c)


def on_body(c, doc):
    c.saveState(); c.setFillColor(CREAM); c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1); c.restoreState()
    draw_border(c)
    # folio
    c.saveState()
    c.setFont("Garamond-Medium", 10.5); c.setFillColor(BROWN)
    txt = str(c.getPageNumber())
    c.drawCentredString(PAGE_W / 2, 40, txt)
    w = pdfmetrics.stringWidth(txt, "Garamond-Medium", 10.5)
    c.setStrokeColor(LIGHT_BROWN); c.setLineWidth(0.6)
    c.line(PAGE_W / 2 - w / 2 - 26, 43.5, PAGE_W / 2 - w / 2 - 8, 43.5)
    c.line(PAGE_W / 2 + w / 2 + 8, 43.5, PAGE_W / 2 + w / 2 + 26, 43.5)
    c.restoreState()


def cover_art_crop(src_plate, out_name, frac=0.05):
    im = PILImage.open(AST / "plates" / src_plate)
    w, h = im.size
    im.crop((int(w * frac), int(h * frac), int(w * (1 - frac)), int(h * (1 - frac)))).save(AST / out_name, quality=90)
    return AST / out_name


COVER_ART = cover_art_crop("plate-014.jpg", "cover_art.jpg")
BACK_ART = cover_art_crop("plate-022.jpg", "back_art.jpg")


def on_cover(c, doc):
    c.saveState()
    c.setFillColor(BLUE); c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(BLUE_DARK); c.rect(0, PAGE_H - 150, PAGE_W, 150, stroke=0, fill=0)
    # gold double border
    c.setStrokeColor(GOLD); c.setLineWidth(1.1); c.rect(22, 22, PAGE_W - 44, PAGE_H - 44, stroke=1, fill=0)
    c.setLineWidth(0.4); c.rect(26.5, 26.5, PAGE_W - 53, PAGE_H - 53, stroke=1, fill=0)
    # title
    c.setFillColor(GOLD); c.setFont("FellSC", 43)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 96, "Old, Old Tales")
    c.drawCentredString(PAGE_W / 2, PAGE_H - 142, "Retold")
    c.setStrokeColor(GOLD); c.setLineWidth(0.7)
    c.line(PAGE_W / 2 - 120, PAGE_H - 166, PAGE_W / 2 - 12, PAGE_H - 166)
    c.line(PAGE_W / 2 + 12, PAGE_H - 166, PAGE_W / 2 + 120, PAGE_H - 166)
    p = c.beginPath(); cy = PAGE_H - 166
    p.moveTo(PAGE_W / 2, cy + 4.5); p.lineTo(PAGE_W / 2 + 4.5, cy); p.lineTo(PAGE_W / 2, cy - 4.5); p.lineTo(PAGE_W / 2 - 4.5, cy); p.close()
    c.setFillColor(GOLD); c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(CREAM_TEXT); c.setFont("Garamond-Italic", 16.5)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 194, "Eight Best-Beloved Folk Stories for Children")
    # art
    im = PILImage.open(COVER_ART); iw, ih = im.size
    art_w = 452; art_h = art_w * ih / iw
    ax, ay = (PAGE_W - art_w) / 2, PAGE_H - 256 - art_h
    c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    c.rect(ax - 5, ay - 5, art_w + 10, art_h + 10, stroke=1, fill=0)
    c.drawImage(str(COVER_ART), ax, ay, width=art_w, height=art_h, preserveAspectRatio=True, mask='auto')
    # credits
    y = ay - 52
    c.setFillColor(CREAM_TEXT); c.setFont("Garamond-Italic", 13.5)
    c.drawCentredString(PAGE_W / 2, y, "Illustrated by")
    c.setFillColor(GOLD); c.setFont("FellSC", 20)
    c.drawCentredString(PAGE_W / 2, y - 30, "Frederick Richardson")
    c.setFillColor(CREAM_TEXT); c.setFont("Garamond-Medium", 9)
    c.drawCentredString(PAGE_W / 2, 52, "T H E   V O L L A N D   E D I T I O N   •   R E S T O R E D   E D I T I O N")
    c.restoreState()


def on_back(c, doc):
    c.saveState()
    c.setFillColor(BLUE); c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setStrokeColor(GOLD); c.setLineWidth(1.1); c.rect(22, 22, PAGE_W - 44, PAGE_H - 44, stroke=1, fill=0)
    c.setLineWidth(0.4); c.rect(26.5, 26.5, PAGE_W - 53, PAGE_H - 53, stroke=1, fill=0)
    # ISBN box (placeholder for the publisher)
    c.setFillColor(colors.white); c.rect(PAGE_W / 2 - 76, 44, 152, 86, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#444444")); c.setFont("Garamond-Medium", 8.5)
    c.drawCentredString(PAGE_W / 2, 118, "ISBN")
    c.setFont("Garamond-Italic", 8)
    c.drawCentredString(PAGE_W / 2, 58, "(to be added by the publisher)")
    c.restoreState()


# ---------------- text conversion ----------------
def esc(text):
    text = text.replace("&", "&amp;")
    def repl(m):
        sizes = {"BIG": 16.5, "MED": 14, "WEE": 11.5}
        return f'<font name="Fell" size="{sizes[m.group(1)]}">{m.group(2)}</font>'
    return re.sub(r"\[\[(BIG|MED|WEE):(.*?)\]\]", repl, text)


def block_flowables(block, dense=False, first=False):
    """One original block -> list of flowables."""
    if block.startswith("> "):
        style = S["VerseD" if dense else "Verse"]
        lines = [ln[2:] for ln in block.split("\n")]
        fl = [Paragraph(esc(ln), style) for ln in lines]
        fl.append(Spacer(1, 5 if not dense else 4))
        return fl
    is_dialogue = block.lstrip().startswith("“")
    if first:
        style = S["BodyFirstD" if dense else "BodyFirst"]
    elif is_dialogue:
        style = S["DialogueD" if dense else "Dialogue"]
    else:
        style = S["BodyD" if dense else "Body"]
    return [Paragraph(esc(block), style)]


def measure(flowables, width=FRAME_W - 12):
    total = 0
    for f in flowables:
        _, h = f.wrap(width, 2000)
        total += h + getattr(f, "getSpaceBefore", lambda: 0)() + getattr(f, "getSpaceAfter", lambda: 0)()
    return total


def img_flowable(path, width=None, height=None):
    im = PILImage.open(path); iw, ih = im.size
    if width and not height:
        height = width * ih / iw
    if height and not width:
        width = height * iw / ih
    img = Image(str(path), width=width, height=height)
    img.hAlign = "CENTER"
    return img


def chunk_page(story_title, blocks, plate_no, text_page_no):
    """Build one book page: running head + plate + text (+ line art). Plate is
    scaled so plate+text+line-art fill but never overflow the page."""
    plate_path = AST / "plates" / f"plate-{plate_no:03d}.jpg"
    pim = PILImage.open(plate_path); pw, ph = pim.size
    aspect = ph / pw  # height per width

    line_path = AST / "lineart" / f"line-{text_page_no:03d}.png"
    has_line = text_page_no in LINE_ART_PAGES and line_path.exists()
    line_h = 0
    if has_line:
        lim = PILImage.open(line_path); lw, lh = lim.size
        line_h = min(125, FRAME_W * 0.84 * lh / lw)

    avail = FRAME_H - 62  # running head + gaps + frame padding + safety buffer
    chosen = None
    for dense in (False, True):
        fl = []
        for i, b in enumerate(blocks):
            fl += block_flowables(b, dense=dense, first=(i == 0))
        text_h = measure(fl)
        for use_line in ((True, False) if has_line else (False,)):
            lh_needed = (line_h + 10) if use_line else 0
            plate_h = avail - text_h - lh_needed
            if plate_h >= 225:
                chosen = (fl, min(plate_h, 355), use_line)
                break
        if chosen:
            break
    if not chosen:  # very dense page: smallest plate, no line art
        fl = []
        for i, b in enumerate(blocks):
            fl += block_flowables(b, dense=True, first=(i == 0))
        chosen = (fl, 215, False)
    text_fl, plate_h, use_line = chosen
    plate_w = min(FRAME_W, plate_h / aspect)
    plate_actual_h = plate_w * aspect

    # distribute leftover whitespace on short pages so they look finished
    total_h = 21 + plate_actual_h + 13 + measure(text_fl) + ((line_h + 8) if use_line else 0)
    leftover = FRAME_H - 14 - total_h

    page = [Paragraph(story_title.upper(), S["RunHead"]),
            img_flowable(plate_path, width=plate_w), Spacer(1, 13)]
    page += text_fl
    if use_line:
        gap = 8 + (min(leftover * 0.5, 80) if leftover > 55 else 0)
        page += [Spacer(1, gap), img_flowable(line_path, height=line_h)]
    elif leftover > 95:
        page += [Spacer(1, min(leftover * 0.35, 60)), Ornament()]
    return [KeepTogether(page), PageBreak()]


# ---------------- pagination (deterministic: every section breaks) ----------------
def pagination():
    """Returns {story_title: pdf_page} and total pages, mirroring the build."""
    page = 1          # cover
    page += 1         # copyright
    page += 1         # title
    page += 1         # dedication
    page += 1         # contents
    intro_page = page + 1
    page += len(INTRO_PAGES)
    starts = {}
    for s in STORIES:
        starts[s["title"]] = page + 1
        page += 1 + len(s["pages"])
    end_page = page + 1
    total = end_page + 1  # + back cover
    return intro_page, starts, end_page, total


INTRO_PG, STARTS, END_PG, TOTAL = pagination()
NUM_WORDS = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]


class Doc(BaseDocTemplate):
    def afterFlowable(self, fl):
        if isinstance(fl, Paragraph):
            style = fl.style.name
            text = fl.getPlainText()
            if style == "StoryTitle":
                key = re.sub(r"\W+", "-", text.lower())
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, level=0, closed=False)
            elif style in ("IntroHead", "ContentsTitle", "EndTitle"):
                key = re.sub(r"\W+", "-", text.lower())
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, level=0, closed=False)


def build():
    out_path = OUT / "Old_Old_Tales_Retold_Restored_Edition.pdf"
    doc = Doc(str(out_path), pagesize=A4, leftMargin=FRAME_X, rightMargin=FRAME_X,
              topMargin=52, bottomMargin=FRAME_Y, title="Old, Old Tales Retold — Restored Edition",
              author="Illustrated by Frederick Richardson")
    frame = Frame(FRAME_X, FRAME_Y, FRAME_W, FRAME_H, id="main", leftPadding=6, rightPadding=6, topPadding=2)
    cover_frame = Frame(FRAME_X, FRAME_Y, FRAME_W, FRAME_H, id="cover")
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[cover_frame], onPage=on_cover),
        PageTemplate(id="Front", frames=[frame], onPage=on_front),
        PageTemplate(id="Body", frames=[frame], onPage=on_body),
        PageTemplate(id="Back", frames=[frame], onPage=on_back),
    ])

    F = []
    # ---- Cover (drawn by onPage) ----
    F += [Spacer(1, 10), NextPageTemplate("Front"), PageBreak()]

    # ---- Copyright / about this edition ----
    F += [Spacer(1, 120),
          Paragraph("OLD, OLD TALES RETOLD", S["StoryKicker"]),
          Paragraph("Eight Best-Beloved Folk Stories for Children", S["CenterItalic"]),
          Spacer(1, 8), Ornament(), Spacer(1, 6),
          Paragraph("Originally published by the P. F. Volland Company, Chicago, 1923.", S["Small"]),
          Paragraph("Illustrations by Frederick Richardson (1862–1937).", S["Small"]),
          Spacer(1, 14),
          Paragraph("<b>About this restored edition.</b> This edition was lovingly restored from photographs of a cherished 1923 copy of the Volland Edition. Every story has been transcribed faithful to the original pages and newly typeset for today’s young readers, and Frederick Richardson’s colour plates have been carefully straightened and restored. Only a few obvious printer’s errors in the old copy have been quietly corrected.", S["SmallLeft"]),
          Paragraph("The folk tales themselves belong to everyone — they were told and retold by mothers and grandmothers for hundreds of years before they were ever written down.", S["SmallLeft"]),
          Spacer(1, 26),
          Paragraph("Restored Edition", S["Small"]),
          Paragraph("ISBN: ______________________", S["Small"]),
          Paragraph("(Publisher: add ISBN and publication details here before printing.)", S["Small"]),
          PageBreak()]

    # ---- Title page ----
    F += [Spacer(1, 66),
          Paragraph("Old, Old Tales Retold", st("TitleMain", fontName="FellSC", fontSize=34, leading=38, alignment=TA_CENTER)),
          Spacer(1, 6),
          Paragraph("Eight Best-Beloved Folk Stories for Children", S["CenterItalic"]),
          Ornament(space_before=8, space_after=14),
          img_flowable(AST / "plates" / "plate-008.jpg", width=372),
          Spacer(1, 22),
          Paragraph("Illustrated by", S["CenterItalic"]),
          Paragraph("FREDERICK RICHARDSON", st("TitleIll", fontName="FellSC", fontSize=17, leading=21, alignment=TA_CENTER)),
          Spacer(1, 40),
          Paragraph("THE VOLLAND EDITION", st("TitleEd", fontName="Garamond-Medium", fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=BROWN)),
          Paragraph("Restored Edition", st("TitleEd2", fontName="Garamond-Italic", fontSize=11, leading=14, alignment=TA_CENTER, textColor=BROWN)),
          PageBreak()]

    # ---- Dedication ----
    F += [Spacer(1, 210),
          Paragraph(DEDICATION, S["Dedication"]),
          Paragraph(DEDICATION_TO, S["DedicationTo"]),
          Spacer(1, 20), Ornament(),
          PageBreak()]

    # ---- Contents ----
    F += [Spacer(1, 46), Paragraph("Contents", S["ContentsTitle"]), Ornament(space_after=14)]
    rows = []
    rows.append([img_flowable(AST / "vignettes" / "vig-006.jpg", height=44),
                 Paragraph(f'<link href="#to-all-children-who-love-stories" color="#2B2118">{INTRO_TITLE}</link>', S["TOCItem"]),
                 Paragraph(str(INTRO_PG), S["TOCPage"])])
    for s in STORIES:
        anchor = re.sub(r"\W+", "-", s["title"].lower())
        rows.append([img_flowable(AST / "vignettes" / f'vig-{s["vignette_page"]:03d}.jpg', height=44),
                     Paragraph(f'<link href="#{anchor}" color="#2B2118">{s["title"]}</link>', S["TOCItem"]),
                     Paragraph(str(STARTS[s["title"]]), S["TOCPage"])])
    toc = Table(rows, colWidths=[58, FRAME_W - 58 - 44, 32])
    toc.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (1, 0), (-1, -2), 0.4, colors.HexColor("#D8C49A")),
    ]))
    F += [toc, Spacer(1, 26), Ornament(), NextPageTemplate("Body"), PageBreak()]

    # ---- Introduction ----
    for pi, paras in enumerate(INTRO_PAGES):
        if pi == 0:
            F += [Paragraph("TO ALL CHILDREN WHO LOVE STORIES", S["IntroHead"]),
                  img_flowable(AST / "vignettes" / "vig-006.jpg", height=162),
                  Spacer(1, 12)]
        for i, p in enumerate(paras):
            F.append(Paragraph(esc(p), S["IntroFirst" if i == 0 else "Intro"]))
        if pi == len(INTRO_PAGES) - 1:
            F += [Spacer(1, 10), Ornament()]
        F.append(PageBreak())

    # ---- Stories ----
    for idx, s in enumerate(STORIES):
        tp = AST / "plates" / f'plate-{s["title_plate"]:03d}.jpg'
        anchor = re.sub(r"\W+", "-", s["title"].lower())
        F += [Spacer(1, 118),
              Paragraph(f"STORY {NUM_WORDS[idx].upper()}", S["StoryKicker"]),
              img_flowable(tp, width=FRAME_W - 12),
              Paragraph(f'<a name="{anchor}"/>{s["title"]}', S["StoryTitle"]),
              Spacer(1, 8), Ornament(),
              PageBreak()]
        for blocks, plate_no in s["pages"]:
            F += chunk_page(s["title"], blocks, plate_no, plate_no - 1)

    # ---- The End ----
    F += [Spacer(1, 84),
          Paragraph("The End", S["EndTitle"]),
          img_flowable(AST / "plates" / "endpaper.jpg", width=FRAME_W - 60),
          Spacer(1, 16),
          Paragraph("And so end the old, old tales — told over and over,<br/>and loved by children everywhere.", S["CenterItalic"]),
          Ornament(space_before=10),
          NextPageTemplate("Back"), PageBreak()]

    # ---- Back cover (flowables over blue onPage) ----
    F += [Spacer(1, 26),
          Paragraph("Old, Old Tales Retold", S["BackHead"]),
          Paragraph("Long, long ago there were no story books for children — so these eight best-beloved folk tales were told aloud, over and over, until at last they were written down. Here they are again, with Frederick Richardson’s beautiful colour pictures, restored for a new generation of children who love stories.", S["BackBody"]),
          Spacer(1, 6),
          img_flowable(BACK_ART, width=300),
          Spacer(1, 14)]
    for s in STORIES:
        F.append(Paragraph(s["title"], S["BackList"]))
    F += [Spacer(1, 16),
          Paragraph("Illustrated by Frederick Richardson", S["BackBody"])]

    doc.build(F)
    print("Built:", out_path)


if __name__ == "__main__":
    build()

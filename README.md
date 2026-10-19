## Old, Old Tales Retold — Restored Edition

A complete, newly typeset children's picture book built from the 110 photographs
in `Untitled design (1).zip` (a cherished 1923 copy of the **Volland Edition**,
P. F. Volland Company, illustrated by **Frederick Richardson**).

## Deliverables (`output/`)

| File | What it is |
|---|---|
| `Old_Old_Tales_Retold_Restored_Edition.pdf` | **Main book — print PDF.** A4, 60 pages, full colour, with bookmarks + clickable contents. |
| `Old_Old_Tales_Retold_Web.pdf` | Same book, compressed for screen / email / WhatsApp sharing. |
| `Old_Old_Tales_Retold_Restored_Edition.epub` | eBook (EPUB 3) with cover, contents and all 51 colour plates. |
| `Manuscript_Old_Old_Tales_Retold.docx` | Editable manuscript (Word) of the full text, with editor's notes at the end. |
| `Manuscript_Old_Old_Tales_Retold.md` | Same manuscript in Markdown/plain text. |

## Book specs

- **Trim:** A4 (210 × 297 mm), portrait — picture-book layout (colour plate + story text on every page)
- **Pages:** 60 (cover, copyright/about, title, dedication, illustrated contents,
  2-page introduction "To All Children Who Love Stories", 8 stories, *The End* page, back cover)
- **Stories (in the original's order):** The Three Bears · The Little Red Hen ·
  The House on the Hill · The Three Little Pigs · Chicken Licken ·
  The Old Woman and Her Pig · Little Tuppens · The Gingerbread Boy
- **Artwork:** all 51 colour plates were detected in the photographs, perspective-corrected
  (flattened), and gently colour/contrast-restored; the original line drawings that appear
  under the text in the old book were extracted and reused on 15 pages, and the original
  illustrated initial letters are used as contents thumbnails.
- **Text:** transcribed page-by-page from the photographs and faithfully re-set
  (EB Garamond / IM Fell English). The Three Bears' graded "great big / middle-sized /
  wee little" voices reproduce the original's different type sizes.
- **New cover & back cover** designed in the spirit of the original blue cloth binding.

## Before publishing — two placeholders to fill in

1. **ISBN** — left blank on the copyright page ("ISBN: ______") and as a white box on the back cover.
2. **Publisher name** — add it on the copyright page (page 2) next to the ISBN line.

If a different trim size is needed (e.g. 8.5″ × 8.5″ or US Letter for KDP), or the
author's name should appear on the cover/title page, that is a small change in
`build_book.py` (page size / cover text) — ask for a re-issue.

### A note on the text
This photographic copy is the original-grim folk version: the wolf eats the first two
little pigs and is burned in the chimney; Little Tuppens is *choking*; the cat *kills*
the rat and the rope *hangs* the butcher. It has been kept exactly as photographed —
soften these in the manuscript first if the author prefers, then rebuild (below).
Only obvious printer's errors were quietly fixed (details are in the Word manuscript's
"Editor's Notes"). The 1923 original is in the US public domain; the folk tales
themselves are traditional.

## Rebuilding the book

```bash
python3 -m venv /tmp/venv
/tmp/venv/bin/pip install reportlab pillow numpy opencv-python-headless PyMuPDF pypdf python-docx fonttools brotli

/tmp/venv/bin/python extract_pages.py    # zip -> pages_ordered/page-001…110.jpg (order from email.html)
/tmp/venv/bin/python process_images.py   # detect + flatten + restore plates -> book_assets/
/tmp/venv/bin/python build_book.py       # typeset the print PDF -> output/
/tmp/venv/bin/python build_extras.py     # manuscript (.md/.docx), EPUB, compressed web PDF
```

| File | Purpose |
|---|---|
| `extract_pages.py` | Unzips the photos and puts them in reading order |
| `process_images.py` | Plate detection, perspective warp, restoration; vignette & line-art extraction |
| `book_content.py` | **The full transcribed text** — edit stories here |
| `build_book.py` | Book design & PDF typesetting (ReportLab) |
| `build_extras.py` | Manuscript, EPUB and web-PDF generators |
| `fonts/*.ttf` | EB Garamond + IM Fell English (from Fontsource, OFL) |
| `pages_ordered/` | The 110 source photos in reading order (regenerable, not in git) |
| `book_assets/` | Restored plates / vignettes / line art (regenerable, not in git) |

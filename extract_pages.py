# -*- coding: utf-8 -*-
"""Step 0: unzip the author's photo archive and copy the 110 photos into
reading order (page-001.jpg ... page-110.jpg).

The reading order is taken from the <img> sequence inside the
`email.html` file that came in the zip — the file names inside the zip
are random hashes, so the HTML order is the only record of the order
in which the pages were photographed.
"""
import re
import shutil
import zipfile
from pathlib import Path

ZIP = Path("Untitled design (1).zip")
EXTRACTED = Path("extracted")
ORDERED = Path("pages_ordered")

if __name__ == "__main__":
    with zipfile.ZipFile(ZIP) as z:
        z.extractall(EXTRACTED)
    html = (EXTRACTED / "email.html").read_text(encoding="utf-8", errors="ignore")
    imgs = re.findall(r'<img[^>]+src="([^"]+)"', html)
    ORDERED.mkdir(exist_ok=True)
    for i, src in enumerate(imgs, 1):
        shutil.copy(EXTRACTED / src, ORDERED / f"page-{i:03d}.jpg")
    print(f"copied {len(imgs)} pages in reading order -> {ORDERED}/")

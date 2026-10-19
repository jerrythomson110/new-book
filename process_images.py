# -*- coding: utf-8 -*-
"""Restore plates from book photographs:
- detect plate rectangle, perspective-warp it flat (OpenCV)
- gentle colour/contrast/sharpness restoration
- rounded corners filled with the book's page cream so plates sit
  seamlessly on the page
Also extracts initial vignettes and the small line-art processions.
"""
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageOps
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from book_content import STORIES, LINE_ART_PAGES

SRC = Path("pages_ordered")
OUT = Path("book_assets")
(OUT / "plates").mkdir(parents=True, exist_ok=True)
(OUT / "vignettes").mkdir(parents=True, exist_ok=True)
(OUT / "lineart").mkdir(parents=True, exist_ok=True)

CREAM = (251, 246, 233)  # page background used in the PDF


def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]   # top-left
    rect[2] = pts[np.argmax(s)]   # bottom-right
    d = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(d)]   # top-right
    rect[3] = pts[np.argmax(d)]   # bottom-left
    return rect


def find_plate_quad(img):
    h, w = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray, 40, 140)
    edges = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=2)
    cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:6]
    for c in cnts:
        area = cv2.contourArea(c)
        if area < 0.35 * w * h:
            continue
        peri = cv2.arcLength(c, True)
        for eps in (0.02, 0.03, 0.015):
            approx = cv2.approxPolyDP(c, eps * peri, True)
            if len(approx) == 4:
                return order_points(approx.reshape(4, 2).astype("float32"))
        # fall back to min-area rectangle of a big contour
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect).astype("float32")
        return order_points(box)
    return None


def warp_plate(img, quad):
    (tl, tr, br, bl) = quad
    W = int(max(np.linalg.norm(br - bl), np.linalg.norm(tr - tl)))
    H = int(max(np.linalg.norm(tr - br), np.linalg.norm(tl - bl)))
    if W < H:  # plates are landscape
        quad = np.array([quad[3], quad[0], quad[1], quad[2]], dtype="float32")
        W, H = H, W
    dst = np.array([[0, 0], [W - 1, 0], [W - 1, H - 1], [0, H - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(quad, dst)
    return cv2.warpPerspective(img, M, (W, H))


def enhance(pil):
    pil = ImageOps.autocontrast(pil, cutoff=1)
    pil = ImageEnhance.Color(pil).enhance(1.10)
    pil = ImageEnhance.Brightness(pil).enhance(1.02)
    pil = ImageEnhance.Sharpness(pil).enhance(1.25)
    return pil


def fill_rounded_corners(pil, radius_frac=0.058):
    w, h = pil.size
    r = int(w * radius_frac)
    arr = np.array(pil)
    # distance outside rounded-rect corner circles -> cream
    for cx, cy, xs, xe, ys, ye in [
        (r, r, 0, r, 0, r), (w - 1 - r, r, w - r, w, 0, r),
        (r, h - 1 - r, 0, r, h - r, h), (w - 1 - r, h - 1 - r, w - r, w, h - r, h),
    ]:
        for y in range(ys, ye):
            for x in range(xs, xe):
                if (x - cx) ** 2 + (y - cy) ** 2 > r * r:
                    arr[y, x] = CREAM
    return Image.fromarray(arr)


def process_plate(page_no):
    path = SRC / f"page-{page_no:03d}.jpg"
    img = cv2.imread(str(path))
    quad = find_plate_quad(img)
    mode = "warp"
    if quad is None:
        h, w = img.shape[:2]
        x0, y0 = int(w * 0.045), int(h * 0.05)
        x1, y1 = int(w * 0.97), int(h * 0.95)
        warped = img[y0:y1, x0:x1]
        mode = "crop-fallback"
    else:
        warped = warp_plate(img, quad)
    # trim a sliver inside the plate edge to remove photo fringing
    hh, ww = warped.shape[:2]
    m = max(2, int(ww * 0.004))
    warped = warped[m:hh - m, m:ww - m]
    pil = Image.fromarray(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
    pil = enhance(pil)
    pil = fill_rounded_corners(pil)
    out = OUT / "plates" / f"plate-{page_no:03d}.jpg"
    pil.save(out, quality=88)
    return mode, pil.size


VIG_BOXES = {
    6: (0.185, 0.195, 0.365, 0.465), 9: (0.125, 0.175, 0.315, 0.505),
    21: (0.130, 0.185, 0.325, 0.495), 33: (0.125, 0.195, 0.315, 0.505),
    45: (0.125, 0.190, 0.325, 0.515), 57: (0.135, 0.185, 0.340, 0.490),
    71: (0.110, 0.160, 0.315, 0.525), 85: (0.120, 0.210, 0.350, 0.525),
    99: (0.125, 0.160, 0.315, 0.485),
}


def process_vignette(page_no):
    path = SRC / f"page-{page_no:03d}.jpg"
    img = cv2.imread(str(path))
    h, w = img.shape[:2]
    x0f, y0f, x1f, y1f = VIG_BOXES[page_no]
    crop = img[int(h * y0f):int(h * y1f), int(w * x0f):int(w * x1f)]
    pil = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
    pil = enhance(pil)
    pil.save(OUT / "vignettes" / f"vig-{page_no:03d}.jpg", quality=88)
    return f"{pil.size}"


# per-page line-art crop boxes (x0,y0,x1,y1 fractions), read off the photos
LINE_BOXES = {
    15: (0.32, 0.48, 0.72, 0.82), 17: (0.20, 0.53, 0.86, 0.85),
    21: (0.18, 0.61, 0.80, 0.86), 23: (0.27, 0.53, 0.84, 0.88),
    25: (0.20, 0.52, 0.85, 0.83), 27: (0.21, 0.57, 0.80, 0.87),
    33: (0.29, 0.61, 0.71, 0.89), 35: (0.26, 0.59, 0.82, 0.86),
    41: (0.14, 0.41, 0.87, 0.74), 45: (0.36, 0.595, 0.69, 0.875),
    47: (0.12, 0.61, 0.92, 0.90), 59: (0.22, 0.59, 0.82, 0.85),
    91: (0.19, 0.61, 0.81, 0.88), 101: (0.24, 0.44, 0.90, 0.76),
    103: (0.21, 0.49, 0.85, 0.80), 105: (0.20, 0.51, 0.90, 0.83),
}


def process_lineart(page_no):
    path = SRC / f"page-{page_no:03d}.jpg"
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    h, w = img.shape[:2]
    x0f, y0f, x1f, y1f = LINE_BOXES[page_no]
    crop = img[int(h * y0f):int(h * y1f), int(w * x0f):int(w * x1f)]
    bg = cv2.GaussianBlur(crop, (51, 51), 0)
    diff = cv2.subtract(bg, crop).astype(np.int16)
    if page_no in (15, 17, 45):  # solid-black animals also need a global-darkness term
        alpha = np.maximum(np.clip((diff - 6) * 4, 0, 255),
                           np.clip((190 - crop.astype(np.int16)) * 3, 0, 255)).astype(np.float32)
    else:
        alpha = np.clip((diff - 12) * 5, 0, 255).astype(np.float32)
    alpha[alpha < 22] = 0
    hh, ww = alpha.shape
    r = 18  # feather the crop edges so no rectangle shows on the page
    fy = np.clip(np.arange(hh) / r, 0, 1) * np.clip((hh - 1 - np.arange(hh)) / r, 0, 1)
    fx = np.clip(np.arange(ww) / r, 0, 1) * np.clip((ww - 1 - np.arange(ww)) / r, 0, 1)
    alpha *= fy[:, None] * fx[None, :]
    rgba = np.zeros((*crop.shape, 4), dtype=np.uint8)
    rgba[..., 0], rgba[..., 1], rgba[..., 2] = 74, 52, 38  # warm dark brown ink
    rgba[..., 3] = alpha.astype(np.uint8)
    Image.fromarray(rgba).save(OUT / "lineart" / f"line-{page_no:03d}.png")
    return crop.shape


def process_endpaper():
    img = cv2.imread(str(SRC / "page-110.jpg"))
    h, w = img.shape[:2]
    crop = img[int(h * 0.04):int(h * 0.97), int(w * 0.03):int(w * 0.97)]
    pil = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
    enhance(pil).save(OUT / "plates" / "endpaper.jpg", quality=88)


if __name__ == "__main__":
    plates = sorted({s["title_plate"] for s in STORIES} |
                    {p for s in STORIES for _, p in s["pages"]})
    print(f"{len(plates)} plates")
    for p in plates:
        print(p, process_plate(p))
    vig_pages = [6] + [s["vignette_page"] for s in STORIES]
    for p in vig_pages:
        print("vig", p, process_vignette(p))
    for p in LINE_ART_PAGES:
        print("line", p, process_lineart(p))
    process_endpaper()
    print("done")

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
    """Locate the colour plate in a page photo.

    v2: segment non-paper pixels in HSV (the plate is colourful/dark, the page
    is pale cream), take the largest blob and fit a quadrilateral to it. This
    tracks the artwork boundary far better than raw Canny edges, which often
    grab inner detail lines and leave a residual tilt after warping.
    Falls back to the original edge-based search.
    """
    h, w = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    sat = hsv[..., 1]
    val = hsv[..., 2]
    mask = ((sat > 42) | (val < 188)).astype(np.uint8) * 255
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,
                            np.ones((21, 21), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                            np.ones((7, 7), np.uint8), iterations=1)
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if cnts:
        c = max(cnts, key=cv2.contourArea)
        if cv2.contourArea(c) > 0.30 * w * h:
            peri = cv2.arcLength(c, True)
            for eps in (0.008, 0.012, 0.02, 0.03, 0.04):
                approx = cv2.approxPolyDP(c, eps * peri, True)
                if len(approx) == 4:
                    return _expand_quad(order_points(
                        approx.reshape(4, 2).astype("float32")))
            hull = cv2.convexHull(c)
            peri = cv2.arcLength(hull, True)
            for eps in (0.01, 0.02, 0.03):
                approx = cv2.approxPolyDP(hull, eps * peri, True)
                if len(approx) == 4:
                    return _expand_quad(order_points(
                        approx.reshape(4, 2).astype("float32")))
            box = cv2.boxPoints(cv2.minAreaRect(c)).astype("float32")
            return _expand_quad(order_points(box))
    quad = _find_plate_quad_edges(img)
    return _expand_quad(quad) if quad is not None else None


def _expand_quad(quad, frac=0.012):
    """Push corners slightly outward so no artwork is clipped; any paper
    sliver this adds is removed again by trim_paper_border() after warping."""
    centre = quad.mean(axis=0)
    return (centre + (quad - centre) * (1.0 + frac)).astype("float32")


def _find_plate_quad_edges(img):
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


def trim_paper_border(bgr, max_frac=0.07):
    """Crop residual photo paper from the warped plate's edges.

    After perspective warping, any small quad error shows up as a white/cream
    wedge along an edge or a hair of page still visible, which makes the
    plate look crooked in its printed box. Scan rows/columns inward from
    each side and cut while they are dominantly smooth pale paper (painted
    sky is textured, photo paper is not). Capped per side for safety.
    """
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    pale = (hsv[..., 2] >= 182) & (hsv[..., 1] <= 68)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    smooth = (np.abs(gx) + np.abs(gy)) < 24
    paper = (pale & smooth).astype(np.float32)
    hh, ww = paper.shape
    row_frac = paper.mean(axis=1)
    col_frac = paper.mean(axis=0)

    def scan(fracs, limit):
        n = 0
        while n < limit and fracs[n] > 0.50:
            n += 1
        return n

    top = scan(row_frac, int(hh * max_frac))
    bottom = scan(row_frac[::-1], int(hh * max_frac))
    left = scan(col_frac, int(ww * max_frac))
    right = scan(col_frac[::-1], int(ww * max_frac))
    return bgr[top:hh - bottom, left:ww - right]


def _edge_connected_paper(bgr):
    """Mask of smooth pale photo paper connected to an image edge."""
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    pale = (hsv[..., 2] >= 182) & (hsv[..., 1] <= 68)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    smooth = (np.abs(gx) + np.abs(gy)) < 24
    paper = (pale & smooth).astype(np.uint8)
    _, labels = cv2.connectedComponents(paper, connectivity=8)
    border_labels = np.unique(np.concatenate([
        labels[0, :], labels[-1, :], labels[:, 0], labels[:, -1]
    ]))
    border_labels = border_labels[border_labels != 0]
    return np.isin(labels, border_labels)


def _edge_runs(mask):
    """For each column, count consecutive True pixels from the first row."""
    return np.cumprod(mask.astype(np.int32), axis=0).sum(axis=0)


def _robust_line(x, y):
    """Fit y=ax+b while rejecting artwork details that break the line."""
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if len(x) < 80:
        return None
    keep = np.ones(len(x), dtype=bool)
    coeff = None
    for _ in range(8):
        if keep.sum() < 40:
            return None
        coeff = np.polyfit(x[keep], y[keep], 1)
        residual = np.abs(np.polyval(coeff, x) - y)
        med = np.median(residual[keep])
        mad = np.median(np.abs(residual[keep] - med))
        threshold = max(3.0, med + 4.0 * 1.4826 * mad)
        new_keep = residual <= threshold
        if np.array_equal(new_keep, keep):
            break
        keep = new_keep
    if coeff is None or keep.mean() < 0.45:
        return None
    return coeff


def _border_line(x, y, default, axis_max, low, high):
    coeff = _robust_line(x, y)
    if coeff is None or abs(coeff[0]) > 0.14:
        return np.asarray(default, dtype=np.float64)
    ends = np.polyval(coeff, [0, axis_max])
    if np.all((ends >= low) & (ends <= high)):
        return coeff
    return np.asarray(default, dtype=np.float64)


def refine_plate_rectangle(bgr):
    """Second, fine rectification based on the artwork's own border.

    The first warp removes the photograph's main perspective. On some pages
    a black plate border can still run a few degrees diagonally, leaving a
    cream wedge inside the rectangular image. Here the four visible
    paper/art boundaries are fitted as robust straight lines and their
    intersections are warped to a true rectangle. Conservative guards make
    the function a no-op whenever the evidence is weak or the proposed quad
    looks implausible.
    """
    h, w = bgr.shape[:2]
    edge_paper = _edge_connected_paper(bgr)
    xs = np.arange(w)
    ys = np.arange(h)

    top_run = _edge_runs(edge_paper)
    bottom_run = _edge_runs(edge_paper[::-1, :])
    left_run = _edge_runs(edge_paper.T)
    right_run = _edge_runs(edge_paper.T[::-1, :])

    x_mid = (xs > 0.05 * w) & (xs < 0.95 * w)
    y_mid = (ys > 0.05 * h) & (ys < 0.95 * h)

    mask = x_mid & (top_run >= 2) & (top_run <= 0.18 * h)
    top = _border_line(xs[mask], top_run[mask], (0.0, 0.0),
                       w - 1, -0.03 * h, 0.20 * h)

    mask = x_mid & (bottom_run >= 2) & (bottom_run <= 0.18 * h)
    bottom = _border_line(xs[mask], h - 1 - bottom_run[mask],
                          (0.0, h - 1.0), w - 1, 0.80 * h, 1.03 * h)

    mask = y_mid & (left_run >= 2) & (left_run <= 0.18 * w)
    left = _border_line(ys[mask], left_run[mask], (0.0, 0.0),
                         h - 1, -0.03 * w, 0.20 * w)

    mask = y_mid & (right_run >= 2) & (right_run <= 0.18 * w)
    right = _border_line(ys[mask], w - 1 - right_run[mask],
                          (0.0, w - 1.0), h - 1, 0.80 * w, 1.03 * w)

    def intersect(horizontal, vertical):
        ah, bh = horizontal
        av, bv = vertical
        denominator = 1.0 - ah * av
        if abs(denominator) < 0.5:
            return None
        x = (av * bh + bv) / denominator
        return np.array([x, ah * x + bh], dtype=np.float64)

    corners = [
        intersect(top, left),
        intersect(top, right),
        intersect(bottom, right),
        intersect(bottom, left),
    ]
    if any(corner is None for corner in corners):
        return bgr

    quad = np.asarray(corners, dtype=np.float64)
    quad[:, 0] = np.clip(quad[:, 0], 0, w - 1)
    quad[:, 1] = np.clip(quad[:, 1], 0, h - 1)

    centre = quad.mean(axis=0)
    vectors = centre - quad
    lengths = np.maximum(np.linalg.norm(vectors, axis=1, keepdims=True), 1.0)
    quad = quad + vectors / lengths * 3.0

    rect = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]],
                    dtype=np.float64)
    if np.max(np.linalg.norm(quad - rect, axis=1)) < 5.0:
        return bgr

    side_lengths = [
        np.linalg.norm(quad[1] - quad[0]),
        np.linalg.norm(quad[2] - quad[1]),
        np.linalg.norm(quad[2] - quad[3]),
        np.linalg.norm(quad[3] - quad[0]),
    ]
    area = cv2.contourArea(quad.astype(np.float32))
    if (area < 0.80 * w * h
            or min(side_lengths[0], side_lengths[2]) < 0.72 * w
            or min(side_lengths[1], side_lengths[3]) < 0.72 * h
            or not cv2.isContourConvex(quad.astype(np.int32))):
        return bgr

    return warp_plate(bgr, quad.astype(np.float32))


def enhance(pil):
    pil = ImageOps.autocontrast(pil, cutoff=1)
    pil = ImageEnhance.Color(pil).enhance(1.10)
    pil = ImageEnhance.Brightness(pil).enhance(1.02)
    pil = ImageEnhance.Sharpness(pil).enhance(1.25)
    return pil


def fill_rounded_corners(pil, radius_frac=0.018):
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


PLATE_ASPECT = 1.45  # one standard picture-box shape for every colour plate


def normalise_plate_box(pil, target_aspect=PLATE_ASPECT):
    """Crop a restored plate to the book's standard picture-box aspect.

    The photographs produce slightly different rectangles from page to page.
    A small centre crop (at most a few percent) gives every plate the same
    clean 1.45:1 box, so the printed frames line up consistently. When
    height must be trimmed, a little more comes off the bottom than the top
    so title banners near the top of the original art are preserved.
    """
    w, h = pil.size
    aspect = w / h
    if aspect > target_aspect:
        new_w = max(1, int(round(h * target_aspect)))
        x0 = (w - new_w) // 2
        return pil.crop((x0, 0, x0 + new_w, h))
    new_h = max(1, int(round(w / target_aspect)))
    excess = h - new_h
    y0 = int(round(excess * 0.38))
    return pil.crop((0, y0, w, y0 + new_h))


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
    # Fine-rectify against the artwork border itself, remove any residual
    # page paper so the plate sits dead-square in its printed box, then trim
    # a sliver inside the plate edge (photo fringing).
    warped = refine_plate_rectangle(warped)
    warped = trim_paper_border(warped)
    hh, ww = warped.shape[:2]
    mx = max(2, int(ww * 0.011))
    my = max(2, int(hh * 0.011))
    warped = warped[my:hh - my, mx:ww - mx]
    pil = Image.fromarray(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
    pil = enhance(pil)
    pil = normalise_plate_box(pil)
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

# Small, page-specific deskew (PIL degrees) and final insets
# (left, top, right, bottom fractions). These remove the white photo margins
# and neighbouring text fragments visible around several initial panels
# without clipping the parts of the big letters that extend beyond a panel.
VIG_REFINEMENTS = {
    6: (0.0, (0.040, 0.030, 0.010, 0.040)),
    9: (-0.7, (0.020, 0.030, 0.100, 0.015)),
    21: (-1.6, (0.060, 0.060, 0.040, 0.050)),
    33: (-1.2, (0.030, 0.020, 0.060, 0.020)),
    45: (0.8, (0.060, 0.070, 0.010, 0.040)),
    57: (-1.2, (0.040, 0.030, 0.010, 0.040)),
    71: (-0.7, (0.015, 0.010, 0.020, 0.005)),
    85: (-1.0, (0.040, 0.030, 0.070, 0.070)),
    99: (0.0, (0.020, 0.015, 0.020, 0.040)),
}


def process_vignette(page_no):
    path = SRC / f"page-{page_no:03d}.jpg"
    img = cv2.imread(str(path))
    h, w = img.shape[:2]
    x0f, y0f, x1f, y1f = VIG_BOXES[page_no]
    crop = img[int(h * y0f):int(h * y1f), int(w * x0f):int(w * x1f)]
    pil = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))

    angle, (lf, tf, rf, bf) = VIG_REFINEMENTS[page_no]
    if angle:
        pil = pil.rotate(angle, resample=Image.Resampling.BICUBIC,
                         expand=False, fillcolor=CREAM)
    iw, ih = pil.size
    pil = pil.crop((int(iw * lf), int(ih * tf),
                    int(iw * (1.0 - rf)), int(ih * (1.0 - bf))))

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
    # Warp the left-hand leaf itself (corners read off a grid overlay), so the
    # bedding above the book and the spine/facing page at the right are gone.
    quad = np.array([
        [w * 0.030, h * 0.100], [w * 0.905, h * 0.072],
        [w * 0.907, h * 0.972], [w * 0.030, h * 0.982],
    ], dtype="float32")
    warped = warp_plate(img, quad)
    hh, ww = warped.shape[:2]
    mx, my = int(ww * 0.008), int(hh * 0.008)
    warped = warped[my:hh - my, mx:ww - mx]
    pil = Image.fromarray(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
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

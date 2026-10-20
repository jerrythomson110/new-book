# Pro Black website audit — files

Independent audit of **https://problack.co**, conducted 20 October 2026 from the public site.

## Read this first
- **`Pro-Black-Website-Audit-2026-10-20.html`** — the full report, designed for reading/printing (open in a browser).
- **`EXECUTIVE-BRIEF.md`** — one-page summary for stakeholders.
- **`Pro-Black-Website-Audit-2026-10-20.md`** — the same full report in Markdown.

## Supporting data
- **`product-sample-audit.csv`** — 105 listings sampled across 13 category/search views, with brand, price, compare-at price, discount, seller, issue flags and a site-search lookup link.
- **`notes.md`** — raw working notes captured during the crawl.
- **`build_data.py`** — builds the CSV and prints the summary statistics.
- **`render_report.py`** — converts the Markdown report into the styled HTML.

## Method in one paragraph
The site is a Next.js app on Vercel with a separate API (`api.problack.co`). Because the sandbox could not reach the domain directly, pages were retrieved through a rendering/proxy layer and read as rendered text plus targeted HTML/meta/JSON-LD extracts. 40+ pages were reviewed, all eight child sitemaps parsed, 105 listings sampled, five product pages examined in depth, both app-store listings checked, and brand-ownership facts verified against public sources. No authenticated checkout, vendor dashboard or analytics access was available; Lighthouse could not complete (`PAGE_HUNG`), so performance findings are structural rather than scored.

## Headline findings
1. The catalog is not attributable to Black-owned sellers: every sampled product page says "Sold by ProBlack Team", and the 18 directory businesses have no products in the shop.
2. Sampled inventory is dominated by mass-market brands (Apple, Bose, LEGO, Clinique, Nivea, Garnier, Cantu, Frito-Lay, Barilla…).
3. Compare-at prices repeat across unrelated products ($388.70, $293.90, $299.00) and produce implausible prices ($855.40 speaker, $1,583.99 money counter).
4. Public statistics contradict each other by 10–100×; 4.9★ is displayed with zero reviews.
5. Clothing & Fashion — the destination of the homepage's main fashion tile — is empty.
6. Legal identity is fragmented (two addresses, two phones, personal Gmail, two App Store IDs) and policies are written for the mobile app only.

## Caveats
Point-in-time snapshot; prices and content change. The 105-listing sample is not a census of the claimed 9,807 products. The report is not legal advice — compliance observations should be reviewed by counsel.

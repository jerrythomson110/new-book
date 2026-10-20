# Pro Black — Executive Brief
**problack.co · 20 October 2026**

## Verdict
**D — not launch-ready in its current form.** The design and technical foundation are good. The catalog, claims and policies are not.

Pro Black presents itself as a marketplace of **verified Black-owned sellers**. The public evidence does not support that:

- **Every product page reviewed (5/5) says "Sold by ProBlack Team."**
- **105/105 sampled listings** are platform-branded ("Pro Black") or mass-market brands — Apple, Bose, Beats, Samsung, LEGO, Clinique, Elizabeth Arden, Nivea, Garnier, Cantu, Lottabody, Frito-Lay, Barilla, Knorr, Bertolli.
- **The 18 "verified" businesses have no products in the shop** and only **3 services** between them. A search for featured business *Luji's Chocolate* returns "No products found."
- SKU prefixes (`WM-…`), Walmart-style listings and images on `demo-client.us` indicate an imported drop-ship feed, not vendor listings.

The problem is not that the catalog is small. It is that **"Black-owned" is the product**, and the product data contradicts it.

## The numbers on the site do not agree
| Claim | Where | Reality |
|---|---|---|
| 9,807 products from Black-owned sellers | Home | No products attributable to the 18 directory businesses |
| 19 businesses / 14 states | Home | 18 businesses in the sitemap; directory exposes 5 states |
| 89 community members | Home | "50K+ Active Members" on Services |
| 265 orders | Home | "2K+ Total Bookings" on vendor signup |
| 69 sellers | Home | "150+ Active Vendors"; "500+ Black-owned businesses" |
| 4.9★ average rating | Services | 0 reviews on every business, service and product |
| "No inflated 'was' prices" | Deals | $388.70 is the "was" price of three jewelry sets **and** an iPhone 13; $293.90 covers two different earbuds |
| 2,052 genuine markdowns | Deals | A generic 30W speaker is listed at $855.40; a money counter at $1,583.99 |

## The five things that create the most risk
1. **Provenance misrepresentation.** Non-Black-owned brands sold under a Black-owned banner. FTC Act §5 and state UDAP exposure; "Black-owned" is a provenance claim and must be true and documented.
2. **Reference-price deception.** Repeated, implausible "was" prices plus an affirmative claim that no prices are inflated. FTC Deceptive Pricing Guides (16 CFR 233).
3. **Fabricated social proof.** 4.9★ with zero reviews; "verified reviews from real customers" with zero reviews; member/order counts that vary by 10–100×.
4. **Broken primary funnel.** The homepage's main "Shop Fashion" tile leads to `/shop/clothing-and-fashion`, which has **zero products**.
5. **Legal inconsistency.** Two addresses, two phone numbers, a personal Gmail on Google Play, two App Store IDs, app-only privacy/terms, `#` consent links on vendor signup, and contradictory return/refund promises ("prepaid label included" vs "return shipping non-refundable").

## What is genuinely good
Cohesive brand and visual design · Next.js/Vercel with edge caching, HTTPS/HSTS and Brotli · complete sitemap/robots setup · 23 categories with real inventory in most · product pages with gallery, breadcrumbs, wishlist and schema · live iOS and Android apps · multiple support channels · thoughtful SMS consent copy.

## The strategic choice
**Option A — be a real Black-owned marketplace.** Shrink to 200–500 verified SKUs, onboard vendors properly, publish a verification standard, and market honest numbers. 3–6 months.

**Option B — be a deals site.** Remove Black-owned framing from commerce, keep the directory separate, and compete on price. Faster, but a different brand.

The current hybrid — drop-ship catalog wrapped in a mission — is the one option that cannot work.

## 30-day plan
1. Remove "Black-owned" from catalog pages until provenance exists.
2. Delist non-Black-owned brands or move them to a clearly separate store.
3. Delete every compare-at price without a documented prior price; remove the "no inflated prices" sentence.
4. Fix or unpublish Clothing & Fashion; repoint the homepage hero.
5. Replace all public metrics with one audited source; delete the 4.9★ and review claims.
6. Publish one legal entity, address, phone and email everywhere.
7. Fix vendor-signup consent links; log consent.
8. Reconcile returns/refunds with operations.
9. Add security headers; review the unauthenticated account-deletion flow.
10. Rewrite category intros to match inventory; fix wrong-product template copy.

*Full evidence, page-by-page findings, SEO/security/accessibility analysis and a 90/180-day roadmap: `Pro-Black-Website-Audit-2026-10-20.html`.*

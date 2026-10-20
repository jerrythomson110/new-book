# Pro Black (problack.co)
## Full Website & Product Catalog Audit

**Audit date:** 20 October 2026
**Auditor:** Independent review (Arena agent)
**Scope:** Public website, product catalog, business directory, content, policies, SEO, performance, security and mobile-app presence
**Evidence base:** 40+ pages reviewed, 105 product listings sampled across 13 category/search views, 5 product pages reviewed in depth, all 8 child sitemaps inspected (large ones sampled), both app-store listings, HTTP headers, structured data and meta tags
**Companion file:** `product-sample-audit.csv` (listing-level dataset)

---

## Contents

1. [Executive summary](#1-executive-summary)
2. [Method, scope and limitations](#2-method-scope-and-limitations)
3. [Scorecard](#3-scorecard)
4. [Catalog audit: what is actually for sale](#4-catalog-audit-what-is-actually-for-sale)
5. [Pricing and promotions](#5-pricing-and-promotions)
6. [Product page content and UX](#6-product-page-content-and-ux)
7. [Category, browse and search architecture](#7-category-browse-and-search-architecture)
8. [Claims, statistics and social proof](#8-claims-statistics-and-social-proof)
9. [Business directory and services](#9-business-directory-and-services)
10. [Legal, policy and compliance](#10-legal-policy-and-compliance)
11. [SEO](#11-seo)
12. [Performance and technical delivery](#12-performance-and-technical-delivery)
13. [Security and privacy](#13-security-and-privacy)
14. [Accessibility](#14-accessibility)
15. [Mobile apps and cross-channel consistency](#15-mobile-apps-and-cross-channel-consistency)
16. [Support and operations](#16-support-and-operations)
17. [Content and blog](#17-content-and-blog)
18. [What is working](#18-what-is-working)
19. [Prioritised remediation plan](#19-prioritised-remediation-plan)
20. [Appendices](#20-appendices)

---

## 1. Executive summary

### Verdict

**Pro Black is a well-designed storefront wrapped around a catalog that does not support its core claim.**

The site presents itself as a marketplace of "verified Black-owned sellers" with 9,807 products. In reality:

- **Every product page examined (5/5) says "Sold by ProBlack Team."** No product we could find is attributed to one of the 18 businesses in the directory.
- **100% of the 105 sampled listings** are either platform-branded ("Pro Black") or mass-market third-party brands — Apple, Samsung, Bose, Beats, LEGO, Clinique, Elizabeth Arden, Nivea, Garnier, Cantu, Lottabody, Frito-Lay, Barilla, Knorr, Bertolli and similar.
- **The 18 "verified Black-owned businesses" have almost no sellable inventory**: 3 services in total, and no products we could attribute to them in the shop. Searching for *Luji's Chocolate* — a featured business — returns "No products found."
- **The catalog appears to be a drop-ship feed.** SKU prefixes (`WM-`, `PRB-ELE-`), Walmart-style product titles and pricing, and images hosted on a third-party domain (`demo-client.us`) all point to imported retail data rather than vendor listings.

This is not a cosmetic problem. The entire value proposition — "your money goes to Black entrepreneurs" — is contradicted by the product data. That is a **trust, brand and consumer-protection issue**, not a marketing tweak.

### The ten most serious findings

| # | Finding | Severity | Evidence |
|---|---|---|---|
| 1 | Products marketed as "from Black-owned sellers" are sold by the platform itself and are overwhelmingly non-Black-owned brands | **Critical** | 5/5 product pages: "Sold by ProBlack Team"; 105/105 sampled listings are platform- or mass-market-branded; no products attributable to the 18 directory businesses |
| 2 | "Compare-at" prices appear fabricated; discounts are anchored to repeated, implausible figures | **Critical** | Identical "was" price **$388.70** on a birthstone necklace, three jewelry sets *and* an iPhone 13; **$293.90** on two different earbuds; a generic 30W speaker at **$855.40**; a money counter at **$1,583.99** |
| 3 | The site explicitly claims discounts are genuine — while displaying the opposite | **Critical** | Deals page: "Every discount is a genuine reduction from the previous price — no inflated 'was' prices." Same page shows the repeated anchors above |
| 4 | Traffic-driving category pages are broken or mislabelled | **High** | `/shop/clothing-and-fashion` renders **zero products** yet is the destination of the homepage hero "Shop Fashion" tile; Electronics intro promises Canon/Sony cameras but lists watch batteries and headphones; Jewelry intro promises men's watches but lists women's jewelry sets |
| 5 | Statistics contradict each other across the site by orders of magnitude | **High** | 18 businesses (sitemap) vs 19 (homepage) vs "150+ Active Vendors" vs "500+ Black-owned businesses" vs "50K+ Active Members"; 3 services vs "2K+ Total Bookings"; 50+ Play Store installs vs "5K+ Happy Customers" |
| 6 | Zero reviews anywhere, despite claims of "verified reviews from real customers" and a "4.9★ Average Rating" | **High** | Every sampled product: "Reviews (0)"; both business profiles reviewed: "0 Reviews / — Rating"; the service page reviewed: "Reviews (0)"; services landing page displays 4.9★ |
| 7 | Product content is auto-generated and frequently about the wrong product | **High** | LEGO set described as "Offered in size SMALL… soft, safe materials… sounds babies love"; a Bluetooth speaker with "comfortable, lightweight design for all-day wear"; identical template paragraphs across unrelated categories |
| 8 | Legal identity and policies are inconsistent and written for the mobile app only | **High** | Privacy Policy says "Pro Black mobile application… available on the Google Play Store"; two different company addresses; support email is a personal Gmail on Google Play; vendor signup's Terms/Privacy links are `#` |
| 9 | Return and refund promises conflict and may be unfulfillable | **High** | Return Policy: "prepaid return label is included in your package"; Refund Policy: "return shipping costs are non-refundable"; refund window 5 days vs 5–10 business days |
| 10 | 9,800+ near-duplicate product pages and several hundred programmatic city/category pages create substantial SEO and quality risk | **High** | Every product sitemap entry sampled carried `lastmod` 2026-07-22; 9,807 products but only ~19 server-rendered per category; location pages with no businesses and self-referential links |

### Bottom line

If Pro Black intends to be a **Black-owned marketplace**, it needs to rebuild the catalog around actual verified vendors, remove non-Black-owned inventory, and replace every unsupported claim with audited numbers. That is a 3–6 month program.

If the intent is a **deals/affiliate storefront**, the Black-owned framing must be removed from the shop and reserved for the directory. Continuing to mix the two creates a consumer-deception risk that no amount of design polish offsets.

---

## 2. Method, scope and limitations

### What was reviewed

- **Core pages:** home, shop, deals, best-sellers, new arrivals, top categories, services, business directory, state page, business profiles ×2, service page, blog index, blog article ×2, FAQ, contact, support, app, our-mission, cart, checkout, login, signup, track order, delete account, privacy, terms, return policy, refund policy, 404.
- **Categories:** all 23 product-category URLs enumerated from the sitemap; 6 opened in full (Beauty, Electronics, Jewelry, Grocery, Financial Services, Clothing).
- **Catalog:** 105 listings captured with title, brand, price, compare-at price, discount, seller and flags. 5 product pages reviewed in depth.
- **Sitemaps:** all 8 child sitemaps inspected (pages, categories, products, blog, locations, SEO pages, businesses, services); the very large product/SEO sitemaps were sampled.
- **Technical:** HTTP response headers, meta tags, canonical tags, JSON-LD, robots.txt, sitemap structure, redirect behaviour, image delivery.
- **Off-site:** Apple App Store listing, Google Play listing, brand-ownership facts verified against public sources.

### Limitations

1. **No authenticated access.** Cart, checkout, account, vendor dashboard and order flows could not be exercised end-to-end. Findings on those areas are based on server-rendered pages and public information.
2. **Sample, not census.** The catalog claims 9,807 products. We sampled 105 listings across 13 views rather than fetching every page; percentages describe the sample, not the full catalog.
3. **Lighthouse did not complete.** An automated Lighthouse run on the homepage returned `PAGE_HUNG` ("the page stopped responding"). Performance findings are therefore structural observations, not scores. This should be re-run manually.
4. **No analytics or server access.** Conversion, traffic, refund and order data were unavailable.
5. **Point-in-time.** Prices, stock and content change; figures reflect 20 October 2026.
6. **Not legal advice.** Compliance observations flag risk for counsel to review.

---

## 3. Scorecard

| Area | Grade | One-line assessment |
|---|---|---|
| **Brand promise & trust** | **F** | The central claim (Black-owned sellers) is contradicted by the catalog and the seller field |
| **Catalog integrity** | **F** | Platform-owned drop-ship feed, mass-market brands, no vendor attribution |
| **Product content** | **F** | Template copy, wrong-product descriptions, empty specs, zero reviews |
| **Pricing & promotions** | **F** | Repeated/implausible anchor prices plus an explicit "no inflated prices" claim |
| **Category & browse UX** | **D** | Empty category, mismatched intros, no URL pagination, no working filters, very limited search |
| **Claims & social proof** | **F** | Statistics inconsistent by 10–100×; ratings shown with no reviews |
| **Legal & policy** | **D** | App-only policies, conflicting addresses, contradictory returns/refunds, dead consent links |
| **SEO** | **C−** | Sound technical base undermined by thin/duplicate pages, incomplete product schema, index bloat |
| **Performance** | **C (unverified)** | Modern stack, but page hung in automated testing; heavy image markup |
| **Security & privacy** | **C−** | HTTPS/HSTS present; most hardening headers missing; no visible cookie consent |
| **Accessibility** | **D** | Multiple unlabelled images, no accessibility statement, content hidden behind client-only tabs |
| **Content & blog** | **D** | High-volume AI content, off-topic, unsourced claims, duplicate URLs |
| **Support & operations** | **D** | One inbox, two phone numbers, unverifiable live chat, manual returns |
| **Mobile apps** | **D** | Two App Store IDs, 50+ Android installs, no ratings, personal Gmail as support contact |
| **Overall** | **D (not launch-ready in current form)** | Strong visual design; fundamental integrity and compliance gaps |

---

## 4. Catalog audit: what is actually for sale

### 4.1 Composition of the catalog

The store reads as a general-merchandise drop-ship feed, not a curated Black-owned marketplace. The sampled assortment included:

- **Electronics:** prepaid carrier phones (Straight Talk, Total Wireless, Cricket, Walmart Family Mobile), unlocked iPhones and Galaxy phones, headphones, earbuds, smartwatches, phone tripods, watch batteries, a gaming keyboard, a VR headset.
- **Beauty:** Clinique, Elizabeth Arden, Glow Recipe, Nivea, Tula, Medicube, Florence by Mills, Good Molecules, face masks, body lotion.
- **Jewelry:** "18K white gold plated" sets from Cate & Chloe and a long tail of marketplace brands (K-KED, OEOEOS, SPRING PARK, Ruanlalo).
- **Grocery:** Frito-Lay variety packs, Barilla pasta, Bertolli olive-oil spray, Knorr bouillon, Gamesa crackers, Badia spices, La Banderita tortillas.
- **Financial Services:** scientific calculators (Texas Instruments, Casio) and money counters.
- **Books & Media:** mass-market paperbacks including *The Hunger Games* prequel and *To Kill a Mockingbird*.
- **Toys, baby, pet, office, home & garden:** LEGO sets, generic dog chews, desk organizers, garden loppers, a sofa cover.

This is a generic Walmart/Amazon-style assortment. Nothing about it is curated around Black-owned makers.

### 4.2 Who is actually selling

| Check | Result |
|---|---|
| Product pages reviewed | 5 of 5 show **"Sold by ProBlack Team — Verified Seller"** |
| Products attributed to a directory business | **None found** |
| Directory businesses with products in the shop | **0** (18 businesses; Luji's Chocolate search returns "No products found") |
| Seller identity shown on category cards | The **brand name** (e.g. "Cate & Chloe", "Bose", "Apple") — visually implying the brand is the seller |
| Platform-branded listings in sample | **56 / 105 (53%)** show "Pro Black" as the brand |
| SKU formats | `WM-…` (Walmart-style), `PRB-ELE-…`, `WM-B2A7946C` |
| Image host | `demo-client.us` — a third-party domain, not a vendor CDN |

**Interpretation:** the "verified seller" badge is attached to the platform's own account. It certifies nothing about Black ownership. The category cards then display the national brand name where shoppers expect the seller, which compounds the impression that these are independent vendors.

### 4.3 The brand problem

The shop sells products from companies that are demonstrably not Black-owned — and in several cases are the exact brands that Black-owned-business advocates warn about.

| Product in shop | Brand | Ownership reality |
|---|---|---|
| Cantu Shea Butter Leave-In Cream | Cantu | Owned by PDC Brands (majority-owned by CVC Capital Partners). Cantu's own FAQ states: **"Whilst we are not Black-owned, we are Black-led."** |
| Garnier Fructis Bouncy Curls Gel | Garnier | L'Oréal |
| Nivea Cocoa Butter Body Lotion | Nivea | Beiersdorf AG |
| Clinique Discover 3-Piece Set | Clinique | The Estée Lauder Companies |
| Elizabeth Arden 9-Piece Set | Elizabeth Arden | The Estée Lauder Companies |
| Lottabody Wrap Me Mousse | Lottabody | Revlon Pro (Revlon) |
| Beats Solo3 | Beats by Dr. Dre | Apple |
| Frito-Lay variety packs; Gamesa crackers | Frito-Lay / Gamesa | PepsiCo |
| Knorr bouillon | Knorr | Unilever |
| Bertolli olive-oil spray | Bertolli | Deoleo (olive oil); brand held by Mizkan |
| Bose QC35 II | Bose | Bose Corporation |
| LEGO Jade Rabbit | LEGO | The LEGO Group |
| iPhone, Samsung Galaxy, Skullcandy, JLab, Casio, Texas Instruments, Barilla | — | National/multinational brands |

The site even publishes an article titled **"Brands You Thought Were Black-Owned (But Aren't)"** — which, despite never naming a single brand, warns that "popular beauty brands" are owned by large corporations while the shop simultaneously sells Cantu and Garnier under a Black-owned banner. The editorial and the commerce contradict each other.

**Why this matters beyond brand optics:** "Black-owned" is the product. A shopper paying a premium or choosing Pro Black over Amazon is paying for provenance. If provenance is absent, the transaction is misrepresented. In the US this falls within FTC Act §5 (deceptive practices) and state unfair-and-deceptive-practices statutes, and it is precisely the kind of claim that attorneys general and class-action firms test.

### 4.4 Catalog scale vs. catalog reality

| Measure | Claimed / observed |
|---|---|
| Products claimed on homepage | **9,807** |
| Products marked down (deals page) | **2,052** |
| Product URLs in sitemap | One `products.xml` file of ~9.8k URLs — consistent with the claim |
| Products visible without JavaScript per category | **~19** |
| Products attributable to directory businesses | **0** |
| Categories in sitemap | **23** |
| Categories in header navigation | **9** |
| Categories on "Top Categories" page | **21** (using `?category=` query URLs) |

A nine-figure product count is being used as proof of marketplace scale, but scale is not the issue — provenance is. Ten thousand feed items with no vendor relationship is a liability, not an asset.

### 4.5 Duplicate and variant sprawl

The product sitemap shows heavy near-duplication typical of feed imports:

- Multiple listings for the same phone in different carrier locks: iPhone 13 (unlocked, Cricket, Straight Talk, Walmart Family Mobile), Galaxy S22/A16/A17 variants, Pixel 3/4/7a/9/10 variants.
- Same item listed twice with different capitalization or punctuation (e.g. *For Richer, For Poorer* novel vs. variants in the feed).
- Spanish-language listings sit alongside English ones (a 71" tripod listed entirely in Spanish, with a transliterated slug) — no localisation strategy, just feed noise.
- Titles are truncated to a fixed character count, sometimes mid-word or with stray punctuation: "…Colors Crayons Colored P", "…Garden Loppers … Chops Thick Hi", "…Smart Watch … waterpro".

This creates thousands of thin, near-identical pages that compete with each other and dilute whatever authority the domain earns.

---

## 5. Pricing and promotions

### 5.1 The anchor-price problem

The "was" prices are not credible. Examples drawn directly from the site:

| Product | Price | "Was" | Shown discount |
|---|---|---|---|
| May Birthstone 18K White Gold Plated Jewelry | $45.49 | **$388.70** | −88% |
| Mckayla 18K White Gold Plated Set | $45.49 | **$388.70** | −88% |
| Cordelia 18K White Gold Plated Set | $45.49 | **$388.70** | −88% |
| Apple iPhone 13, unlocked 128GB | $388.70 | — | — |
| Viviana 18K Set with Swarovski Crystals | $34.99 | **$299.00** | −88% |
| Veatool T8 Wireless Earbuds | $32.32 | **$293.90** | −89% |
| Veatool Mini Go Headphones | $44.08 | **$293.90** | −85% |
| Wireless Headphone Bluetooth 5.4 | $19.89 | **$159.99** | −88% |
| Portable Bluetooth Speaker 30W (generic, brand CASCHO) | **$855.40** | **$1,002.86** | −15% |
| Cassida 9900R Money Counter | **$1,583.99** | — | — |
| Total Wireless iPhone 17e 512GB | **$1,038.70** | — | — |

Two patterns stand out:

1. **Repeated anchors across unrelated goods.** $388.70 appears as the "original" price of a birthstone necklace, two jewelry sets *and* an iPhone 13. $293.90 is shared by two unrelated earbuds. $299.00 covers two different jewelry sets. Real retail prices do not behave this way; generated or defaulted reference prices do.
2. **Implausible absolute prices.** A no-name 30W Bluetooth speaker at $855.40; a money counter at $1,583.99; a 512GB prepaid iPhone 17e at $1,038.70. Several of these are far above normal retail, suggesting unit/price mapping errors in the feed.

### 5.2 The claim that makes it worse

The Deals page states:

> "2,052 products marked down by Black-owned sellers. **Every discount is a genuine reduction from the previous price — no inflated 'was' prices.**"

That sentence converts a data-quality problem into an affirmative misrepresentation. Under the FTC's Guides Against Deceptive Pricing (16 CFR Part 233), a reference price must be a price at which the product was actually offered in the recent, regular course of business. If $388.70 was never charged, the "88% off" is fictitious. The explicit denial ("no inflated 'was' prices") is an aggravating factor, not a defence.

### 5.3 Promotional pages

- `Today's Deals` claims 2,052 marked-down products (21% of the claimed catalog).
- The same six jewelry items appear at the top of Home, Shop, Deals and Jewelry — the "Recommended" sort is effectively static, so "deals" look curated but are not.
- No price-history, no "was" date range, no per-product promotion end date.
- No coupon, bundle, loyalty or member pricing — the only promotion mechanic is a discount badge.

### 5.4 Recommended fix (pricing)

1. Remove every compare-at price that cannot be tied to a documented prior selling price and date.
2. Recompute discounts from actual price history; suppress the badge when history is missing.
3. Fix unit/price mapping errors in the feed (speaker, money counter, prepaid phones) before indexing.
4. Delete the "no inflated 'was' prices" sentence until it is true.
5. Add price-history disclosure ("lowest price in 90 days") if selling into the EU/UK.

---

## 6. Product page content and UX

### 6.1 Template copy, often about the wrong product

Every product page uses the same skeleton:

> "{Product} is a {piece/device/toy} built for quality and everyday usability. It comes as a value 1-pack and comes in a clean white finish… A dependable pick in {category}, it ships fast from ProBlack, the marketplace built around Black-owned commerce."

Consequences observed:

- **LEGO Jade Rabbit set** — "Offered in size **SMALL** for a comfortable fit… **Soft, safe materials** designed for little hands… **sounds babies love**." This is infant-rattle copy applied to a building-brick set.
- **Portable Bluetooth speaker** — "…**comfortable, lightweight design for all-day wear**." Headphone copy applied to a speaker.
- **Bose QC35 II** — no mention of noise cancellation, battery life, codecs, weight or what is in the box. Instead: "Genuine Bose quality you can trust."
- **Cantu leave-in cream** — six paragraphs of generic shea-butter essay, no ingredients, size confirmation beyond the title, or usage guidance specific to the SKU.

This is not just poor copywriting; it is **product misinformation**. A shopper relying on "size SMALL" for a LEGO set or "all-day wear" for a speaker is being misled about the item.

### 6.2 Empty tabs

Product pages show tabs: **About this item · Highlights · Specifications · FAQs · Reviews (0)**.

- **Specifications:** no specification table rendered on any sampled page.
- **FAQs:** no product-specific Q&A rendered.
- **Reviews:** zero on every sampled page.
- **Highlights:** repeats the "At a glance" bullets.

Three of five tabs are empty shells. This is visible to users and to Google.

### 6.3 No variant handling

No size, colour, capacity or carrier selector on product pages, even for items with obvious variants (phones, apparel, jewelry sets). Variants exist as separate SKUs with separate pages, which fragments reviews and SEO and makes comparison impossible.

### 6.4 Commerce mechanics

- **Stock:** "In stock" is static; no quantity or backorder state.
- **Shipping:** "Estimated in 2–6 business days" and "Shipping calculated at checkout" — no rate table, no free-shipping threshold, no carrier. The Product schema, however, declares a flat **$12.00 shipping rate** with 1–2 days handling and 1–4 days transit, which contradicts the visible copy.
- **Returns:** "an easy returns policy on every order" — links nowhere from the PDP. The Product schema declares `FreeReturn` / 30 days, while the Refund Policy says return shipping is non-refundable.
- **Schema:** Product/Offer markup exists and correctly names the seller "ProBlack Team", but omits `brand`, declares the LEGO set's weight as **1 lb**, and sets `priceValidUntil` a year out — signs of a templated generator rather than per-product data. BreadcrumbList points at a query-string category URL, and the FAQPage repeats two generic shipping questions rather than product-specific answers.
- **Seller contact:** "Chat with the vendor" — but the vendor is "ProBlack Team."
- **Wishlist/share:** present; wishlist requires an account and redirects to sign-in.
- **Breadcrumbs:** link to `https://problack.co/shop?category=Electronics` rather than `/shop/electronics`, creating duplicate taxonomy URLs.

### 6.5 Imagery

- Most listings have a single image; a few have 5–7.
- All images are proxied through Next Image at up to `w=3840&q=75`, including thumbnails at `w=256`.
- Images are hosted on `demo-client.us`, outside the brand's domain — a single point of failure and an SEO/image-licensing question.
- The product OG image is generated per product (`/merchant-image/<slug>/0.webp`) — good — but the page's `og:image` metadata on the homepage is a product photo, not brand artwork.

### 6.6 Recommended fix (PDP)

1. Replace template copy with structured, SKU-specific data: brand, model, dimensions, materials, what's in the box, compatibility, care.
2. Only render tabs that have content; otherwise remove them.
3. Add variant selectors and consolidate reviews at the parent-product level.
4. Show real shipping cost/ETA and a link to the return policy.
5. Attribute the seller correctly and show the vendor profile.
6. Complete the existing Product/Offer markup (add `brand`, fix weight, align shipping and returns) and fix BreadcrumbList so it points to the clean category URL; add `AggregateRating` only when reviews are real.

---

## 7. Category, browse and search architecture

### 7.1 The empty category

**`/shop/clothing-and-fashion` returns no products at all.** The page shows a category intro, a "Filters 1 / Active: Clothing & Fashion" chip, and then jumps straight to SEO copy and "Browse other categories." There is no empty-state message, no suggested alternative, no apology — just a blank aisle.

This matters because:

- The homepage's **primary featured tile** ("Back Black This Season — Style. Culture. Impact. **Shop Fashion**") links here.
- The header navigation links here.
- The category title promises "Women's Dresses & Tops" and the description promises bodycon dresses, tunics, leggings and joggers.
- The sitemap lists it with priority 0.8 and daily changefreq.

A new visitor following the site's most prominent merchandising unit lands on a dead end. This is the single highest-impact UX bug on the site.

### 7.2 Category copy does not match category contents

| Category | What the intro promises | What is actually listed |
|---|---|---|
| **Electronics** | "Our biggest department, and it leans heavily toward photo and video… mirrorless bodies and DSLRs from Canon and Sony, double-zoom lens kits, magnetic phone tripods and ring lights" | Watch batteries, headphones, earbuds, smartwatches, prepaid phones, a watch box |
| **Jewelry & Accessories** | "Watches make up most of this category, and men's styles in particular — gunmetal cases… large-face digital sports watches" | Women's birthstone jewelry sets, bridal sets, rhinestone necklaces |
| **Financial Services** | "Cash-handling equipment… bill counting machines with UV, magnetic and infrared counterfeit detection" | Scientific calculators (11 of the first 13 items), then money counters |
| **Clothing & Fashion** | Dresses, tunics, leggings, joggers, plus sizing | Nothing |
| **Beauty** | Firming/cellulite/stretch-mark creams and hair treatments including SheaMoisture | Clinique, Elizabeth Arden, Glow Recipe, Nivea, sheet masks |

The intros read as if written from a different dataset than the one powering the grid. Shoppers who click "Electronics" expecting cameras get watch batteries; that is an immediate bounce.

### 7.3 Taxonomy is duplicated and inconsistent

- **23 categories** in the sitemap, **9** in the header, **21** on the Top Categories page.
- Overlapping categories: Beauty vs Health & Beauty; Home & Kitchen vs Home & Garden vs Household Essentials; Clothing & Fashion vs Jewelry & Accessories; Food & Beverages vs Grocery.
- Two URL schemes for the same taxonomy:
  - Clean paths: `/shop/electronics`, `/shop/beauty`
  - Query parameters: `/shop?category=Electronics`, `/shop?category=Clothing%20%26%20Fashion` (used by breadcrumbs and Top Categories)
- This splits internal link equity, creates duplicate pages, and makes analytics unreliable.

### 7.4 Pagination and crawl depth

- Each category server-renders roughly **19 products** followed by a "Load more products" button.
- **Pagination is not URL-addressable.** `/shop?page=2` returns the same first page; there is no `/shop/electronics?page=2`.
- Consequence: Google and other crawlers can only discover ~19 products per category through internal links. The remaining ~9,000 products are reachable only via the XML sitemap. That is a fragile indexing strategy and a poor experience for users who share or bookmark a page.
- No `rel=next/prev`, no numbered pagination, no result count ("Showing 19 of 1,240").

### 7.5 Filters and sort

- A "Filters" control exists but no filter state is reflected in the URL (no brand, price, rating, size or availability facets).
- "Recommended" is the only visible sort; there is no price, newest or rating sort.
- The filter chip ("Active: Electronics") is a category label masquerading as a filter.

### 7.6 Search

- There is a search control in the header, but **`/search` is a 404**; search only works through `/shop?search=`.
- Results are extremely thin:
  - `shea` → **4 results** (Buttah, Cantu, Garnier, Lottabody) — despite SheaMoisture being named in the category copy.
  - `iphone` → a mix of iPhones, a smartwatch, selfie sticks and a Spanish tripod.
  - `luji` → **"No products found"** for a featured business.
- No typo tolerance, no synonyms, no category/brand suggestions, no "did you mean", no zero-result recovery.
- Search URLs are indexable (`index, follow`), creating crawlable duplicate result pages.

For a 9,807-SKU catalog, a four-result search for a core ingredient is a serious merchandising failure — and further evidence that the visible inventory is much smaller or less connected than the headline number suggests.

### 7.7 Recommended fix (browse)

1. Fix or unlink Clothing & Fashion immediately; add a real empty state.
2. Rewrite category intros from actual inventory (or remove them).
3. Consolidate to one canonical taxonomy with 301s from query-param URLs.
4. Implement server-rendered pagination with URLs, result counts and `rel=next`.
5. Add URL-driven facets (price, brand, availability, rating) and a sort control.
6. Build real search (Algolia/TypeSense/Elastic) with synonyms and zero-result handling; block result URLs from indexing.

---

## 8. Claims, statistics and social proof

### 8.1 The numbers do not agree — anywhere

| Claim | Where it appears | Contradicted by |
|---|---|---|
| **9,807** products from Black-owned sellers | Homepage | 2,052 deals; page-level limitation to 19 items; no products attributable to directory businesses |
| **19** verified businesses in **14** states | Homepage | **18** businesses in `businesses.xml`; the directory page exposes only **5 states / 19 cities** |
| **89** community members | Homepage | "50K+ Active Members" (services page); "5K+ Happy Customers" (vendor signup) |
| **265** orders placed securely | Homepage | "2K+ Total Bookings" (vendor signup); 50+ Android downloads |
| **69** Black-owned sellers | Homepage vendor block | 19 businesses; 150+ Active Vendors; 500+ Black-owned businesses |
| **150+** Active Vendors | app.problack.co/signup | 18 businesses |
| **500+** Black-owned businesses | app.problack.co/signup | 18 businesses |
| **4.9★** average rating | Services page hero | No reviews on any business, service or product we examined |
| **2,052** marked-down products | Deals page | Repeated/fabricated anchors (see §5) |
| **"Verified reviews from real customers"** on every listing | Shop page SEO copy | 0 reviews on all 5 sampled PDPs |

A visitor who browses for ten minutes sees at least four different versions of "how big is this marketplace," ranging from 18 businesses to 500+, and from 89 members to 50,000. Inconsistent statistics are the fastest way to lose a skeptical shopper — and they are trivially checkable.

### 8.2 Ratings without reviews

The services page presents **"4.9★ Average Rating"** as a hero proof point. Both business profiles reviewed show `— Rating` and `0 Reviews`; the service page reviewed shows "Reviews (0)"; every sampled product shows "Reviews (0)".

Displaying an aggregate rating with no underlying reviews is a classic deceptive-endorsement pattern and also breaches Google's review-snippet policies if marked up. The Product markup carries no `AggregateRating` or `Review`, which limits SEO exposure but not consumer-protection exposure.

### 8.3 "Verified" is undefined and unearned

- Every product carries a **"Verified Seller"** badge — attached to "ProBlack Team."
- Every business is described as "verified," but the site never states **who** verifies, **what** evidence is required, **when** verification expires, or **how** a business proves Black ownership.
- The FAQ question "How are businesses verified?" exists but its answer is not rendered (see §17.3).
- No verification certificate, badge ID, or appeal process is published.

If "verified Black-owned" is the product, the verification standard must be public, documented and auditable. Right now it is a word on a badge.

### 8.4 Recommended fix (claims)

1. Pick one source of truth for metrics and generate every number from it (ideally a live stats service).
2. Remove the 4.9★ rating and all star imagery until reviews exist.
3. Replace "verified" with a defined standard: ownership attestation, business registration, ID check, review date, re-verification cadence, and a public "how we verify" page.
4. Add a claims register: every public number has an owner, a query and a review date.
5. Add third-party trust signals only when real (Stripe, BBB, Trustpilot, verified reviews).

---

## 9. Business directory and services

### 9.1 The directory is tiny and disconnected

| Metric | Value |
|---|---|
| Businesses in sitemap | **18** |
| Services in sitemap | **3** |
| Category "listings" shown on `/services` | **8** (Beauty 2, Clothing 2, Accounting & Tax 1, Business & Industrial 1, Food & Beverage 1, Wellness 1) |
| Businesses with products in the shop | **None found** |
| Businesses with bookable services | 2 (Ne Ndoro: 1; one other) |
| Reviews across all businesses | **0** |
| States with listed businesses | 5 shown (CA, MI, NY, OK, plus…) — homepage claims 14 |

The directory and the marketplace are effectively two different products sharing a header. A shopper who discovers Luji's Chocolate cannot buy the chocolate; a shopper browsing the shop never encounters Luji's.

### 9.2 Service categories: hundreds of empty doors

`/services` lists 60+ categories. Almost all show **"0 listings"** — Accounting Services, Agriculture, Animal Care, Anti-Aging Facial, Baking, Beard Trim, Brake Service, Bridal Makeup, Call Centers, Catering, Childcare, Church, Cleaning, Construction, Cooking Classes, CrossFit, Dental, DJ Services, Electrical, Event Planning, and on and on.

Each one is a linked, crawlable URL. This is textbook **thin/doorway content**: pages created for search engines that offer no inventory. Google's spam policies explicitly target this pattern, and it dilutes the crawl budget for pages that do have content.

### 9.3 Programmatic location pages

The `locations.xml` sitemap contains 24 URLs (5 states, 19 cities). The `seo-pages.xml` sitemap contains **several hundred programmatic pages** (8 sitemap chunks) of the form:

- `/black-owned-businesses-in-{city}` (40+ cities, including Seattle, Portland, Las Vegas, Phoenix, Boston, Sacramento, Nashville — cities with no listed businesses)
- `/black-owned-{category}` (restaurants, barbershops, beauty salons, home services, financial services, etc.)
- `/black-owned-{category}-in-{city}` (a full city × category matrix)

The Georgia state page illustrates the quality:

- ~900 words of generic, spun copy ("Use one focused guide to compare practical options…").
- Internal links that point back to **the same page** ("local business directory" → the Georgia page; "related local category guides" → the Georgia page).
- **Zero Georgia businesses listed.**
- Unrelated product widgets (LEGO, dog toys, desk organizers) inserted below the copy.
- City links (Atlanta, Savannah, Augusta) that lead to further pages with no inventory.

At scale this is hundreds of near-duplicate pages competing for "Black-owned businesses in {city}" queries with no businesses to show. It can produce short-term impressions and long-term manual-action risk.

### 9.4 Business profile quality

Examples reviewed: **Ne Ndoro** (Richmond, CA) and **Luji's Chocolate** (Owings Mills, MD).

What works: address, phone, email, hours, category, service listing, map-style contact block, "Open now" status.

What does not:

- **Inventory mismatch:** Ne Ndoro is categorised "Hair & Beauty" but its only service is "Custom Tailoring," tagged "Other."
- **AI-generated imagery:** the Ne Ndoro service image is hosted on Cloudinary with the filename `ChatGPT Image Dec 30, 2025, 07_45_48 PM.png` — a generated image presented as a business photo. The business logo on the profile is also a generic webp.
- **Unformatted contact data:** `5106290705`, `5515019534` — no formatting, no validation.
- **"Open now · until 17:00"** is shown without a timezone and despite no timezone field on the profile.
- **Location granularity is wrong:** service page shows "Location: US"; no city, radius or travel policy.
- **No reviews, no rating, no response time, no verification date.**
- **No products** for a chocolate business.
- **Similar businesses** are all labelled "New" and include unrelated categories (a cleaning company next to a salon).
- **Schema exists but is mis-typed and truncated:** Ne Ndoro is marked up as a `HairSalon` even though its only service is tailoring; `addressLocality` is `"Richmond "` (trailing space); the Service `description` is cut off mid-sentence ("…allow 3 we"); duration is stored in `serviceOutput` rather than a duration property; and the service image is a **1.9 MB PNG** generated by ChatGPT.

### 9.5 Recommended fix (directory)

1. Merge directory and marketplace: every business profile should show its products and services, with a single checkout.
2. Publish the verification standard and display a verification date and method on each profile.
3. Remove all zero-inventory service categories from navigation and sitemaps until they have listings (or consolidate them).
4. Noindex or delete city/category pages with no businesses; only publish location pages that have ≥3 real listings.
5. Replace generic copy with locally specific, human-written content or remove it.
6. Fix and extend the existing `HairSalon`/`LocalBusiness` and `Service` markup (correct type, duration, address, description); add BreadcrumbList and `AggregateRating` once real reviews exist.
7. Normalise phone/address data; store timezone; show hours accurately.

---

## 10. Legal, policy and compliance

> These are risk observations for counsel to review, not legal conclusions.

### 10.1 Policies describe a different product

Both core policies are written for the **mobile app**, not the website:

- **Privacy Policy:** "This Privacy Policy outlines how we collect, use, disclose, and safeguard your information when you use the **Pro Black mobile application ('App'), available on the Google Play Store**." It never mentions the website, cookies, analytics, browser data or web checkout. It also ignores iOS despite an App Store listing.
- **Terms of Service:** "These Terms govern your access to and use of the **Pro Black mobile application ('App')**… By downloading, installing, or using Pro Black…" — download/install language, no website terms, no marketplace seller terms, no returns/refunds incorporated by reference.

**Gaps this creates:**

| Requirement | Status |
|---|---|
| Cookie/tracking disclosure | Absent |
| CCPA/CPRA "Do Not Sell or Share" notice and link | Absent (despite California audience) |
| GDPR/UK GDPR lawful basis, transfer mechanism, DPA | Absent |
| Data retention schedule | Absent |
| Processor/sub-processor list (Stripe, Vercel, image host) | Partial (Stripe only) |
| Seller terms / vendor agreement published | Absent |
| Marketplace role disclosure (who is merchant of record) | Absent |
| Dispute resolution / arbitration / governing law | Present but app-framed |
| Accessibility statement | Absent |
| SMS program terms with opt-in evidence | Present in policy and contact form |

The contact form's SMS consent paragraph is well drafted (STOP/HELP, frequency, rates). That is one of the few compliance positives.

### 10.2 Conflicting company identity

| Field | Value 1 | Value 2 |
|---|---|---|
| Address | **3009 Sweet Gum Lane, Williamsburg, VA 23185** (Privacy Policy) | **8401 Mayland Dr #7269, Richmond, VA 23294** (site footer) |
| Support phone | **+1 (859) 300-3983** (Support page) | **+1 (757) 870-4183** (Google Play) |
| Support email | **info@problack.co** (site) | **fjsherman1@gmail.com** (Google Play) |
| Developer | "Pro Black Inc." (App Store copyright) | "Freddie Sherman" (App Store seller / Play developer) |
| Privacy policy | `/privacy-policy` (site) | `problack-lp.vercel.app/privacy-policy.html` (App Store) |
| App Store app | `id6748367144` (buttons) | `id6449268531` (footer "Get the app") |

Two addresses, two phone numbers, two privacy policies, a personal Gmail and two App Store IDs. For a marketplace handling payments and personal data, this is a serious credibility and due-diligence problem — and it undermines any attempt to enforce terms or respond to a regulator.

### 10.3 Returns and refunds contradict each other

| Topic | Return Policy | Refund Policy |
|---|---|---|
| Return shipping | "Returns are free — a prepaid return label is included in your package" | "Original and return shipping costs are **non-refundable**" |
| Refund timing | "refunds are processed within **5 days**" | "processed within **5 to 10 business days**" |
| Damaged items | Contact within **7 days** for exchange | "Email us as soon as possible" |
| Non-returnable | Personal care, custom, digital, gift cards, final sale | Not addressed |

For a drop-ship catalog, "a prepaid return label is included in your package" is almost certainly not operationally true — the platform does not control what the third-party fulfiller puts in the box. Promising it creates a per-order obligation the business cannot meet, which is both a customer-service crisis and a potential misrepresentation.

### 10.4 Broken consent links at the point of signup

On **app.problack.co/signup** (the vendor signup), the footer of the form reads:

> "By creating an account, you agree to our **Terms of Service** and **Privacy Policy**."

Both links are `href="#"`. A vendor cannot review the terms they are agreeing to, and there is no evidence of affirmative consent. The main site's `/signup` links correctly to `/terms-of-service` and `/privacy-policy` — the inconsistency suggests the vendor app was built separately and never brought into compliance.

### 10.5 Account deletion

`/delete-account` asks only for an email address and a reason, with a confirmation checkbox. There is no authentication step visible before submission. If the backend deletes accounts based on an unauthenticated email submission, that is a **account-takeover / data-loss vulnerability**; if it sends a verification email, the page should say so. This needs immediate engineering review.

### 10.6 Advertising and endorsement exposure

Potentially material claims:

1. **"Verified Black-owned"** applied to products from L'Oréal, Estée Lauder, PepsiCo, Apple, Bose, LEGO, etc.
2. **"Every discount is a genuine reduction… no inflated 'was' prices"** alongside repeated/implausible anchors.
3. **"4.9★ Average Rating"** with zero reviews.
4. **"50K+ Active Members" / "5K+ Happy Customers"** with 50+ Android installs and 89 community members.
5. **"Every product listing includes verified reviews from real customers"** with zero reviews.
6. **"Verified businesses"** with no published verification standard.

In the US, these map to FTC Act §5 (deceptive acts), the FTC's endorsement and review guides (16 CFR Part 255), the deceptive-pricing guides (16 CFR Part 233), and state UDAP statutes. "Black-owned" is a provenance claim, and provenance claims are treated similarly to "Made in USA" claims: they must be true, documented and not misleading in context.

### 10.7 Recommended fix (legal)

1. Retain counsel to review all marketing claims, pricing representations and the returns/refund framework.
2. Rewrite Privacy Policy and Terms for the **website + marketplace**, with seller terms, merchant-of-record clarity, cookie policy, state privacy rights and retention.
3. Publish **one** legal entity, address, phone and email everywhere (site, apps, invoices, policies).
4. Fix the vendor-signup consent links; log consent (timestamp, version, IP).
5. Make returns/refunds operationally true before promising them; align the two policies.
6. Add a cookie consent manager if any analytics/marketing tags run; add "Do Not Sell/Share" and "Your Privacy Choices."
7. Add an accessibility statement and a public "How we verify" page.

---

## 11. SEO

### 11.1 What is technically sound

- Clean, descriptive title tags on home, category, blog and service pages.
- Self-referencing canonicals on product pages.
- `robots.txt` with sensible private-path exclusions and an explicit sitemap.
- Sitemap index with eight logical child sitemaps.
- HTTPS, HSTS, Vercel edge caching.
- Branded 404 page with recovery links.
- `www` → apex redirect works.
- A full JSON-LD stack on product and blog templates (Organization, WebSite, Product/Offer, BreadcrumbList, FAQPage, BlogPosting) — it needs correction, not construction.

### 11.2 What is holding it back

| Issue | Detail | Impact |
|---|---|---|
| **Structured data is present but flawed** | Each product carries five JSON-LD blocks: Organization, WebSite, Product/Offer (price, availability, seller "ProBlack Team", $12 shipping, free 30-day returns), BreadcrumbList and a two-question FAQPage. Gaps: **no `brand`**, no `AggregateRating`/`Review`, and the **same two generic FAQs** ("Does ProBlack offer fast shipping?") are repeated across thousands of products. BreadcrumbList points to `/shop?category=Toys%20%26%20Games`, entrenching the duplicate taxonomy. Offer declares **$12 flat shipping** vs "calculated at checkout" and **free returns** vs the Refund Policy's non-refundable return shipping. Blog posts do have `BlogPosting` + `FAQPage`, but the author is the Organization, not a person | Rich results are weakened; duplicated FAQ markup looks spammy; structured data contradicts visible policy |
| **Meta descriptions auto-truncated** | Product description is body copy cut mid-word: "…in a clean whit" | Poor CTR; low-quality snippet |
| **Product titles lack brand/store** | `<title>` is just the product name | Weaker differentiation in SERPs |
| **Thousands of near-duplicate pages** | Templated descriptions, repeated titles, variant sprawl | Crawl waste, cannibalisation, quality risk |
| **Only ~19 products linked per category** | "Load more" is client-side; no URL pagination | ~9,000 products depend entirely on sitemap discovery |
| **Indexable filter/search URLs** | `/shop?search=`, `?category=`, `?page=` all return `index, follow` | Faceted duplicate URLs |
| **Empty category indexed** | Clothing & Fashion is in the sitemap at priority 0.8 with no products | Thin page, bad landing experience |
| **~400 programmatic city/category pages** | No businesses; self-referential internal links; spun copy | Doorway-page risk; dilution |
| **Duplicate blog slugs** | e.g. `black-owned-fall-decor-…` and `…-2`; `black-owned-halloween-…` and `…-2`; `buy-black-build-wealth-…` and `…-2` | Duplicate content, split rankings |
| **Sitemap freshness is unreliable** | Every product entry sampled carried `lastmod` 2026-07-22; blog `lastmod` differs from on-page dates | Crawlers learn to distrust lastmod |
| **Breadcrumbs use query URLs** | `…/shop?category=Electronics` instead of `/shop/electronics` | Splits taxonomy signals |
| **No author/E-E-A-T signals** | "Pro Black Team" with no bio, no editorial policy, no sources | Weak trust for informational content |
| **Homepage OG image is a product photo** | `og:image` = May Birthstone image | Weak social sharing/brand recall |
| **Missing pages from sitemap** | Privacy, terms, returns, refunds, delete-account are footer-only | Minor discoverability gap |
| **Legal/trust pages lack schema** | No Organization contact/address consistency | Entity confusion |

### 11.3 Index-bloat math

- 9,807 product URLs (mostly thin, templated, no reviews, no specs).
- ~400 SEO landing pages (many with zero inventory).
- 60+ service categories, most with zero listings.
- 24 location pages, most with zero businesses.
- 80+ blog posts, several duplicated.

That is roughly **10,400+ indexable URLs**, of which only a few dozen have unique, substantive content and real inventory. Google tolerates this for a while; it does not reward it.

### 11.4 Recommended fix (SEO)

1. Complete the Product/Offer markup (add `brand`, fix weight, align shipping and returns), point BreadcrumbList at clean category URLs, replace the duplicated product FAQs with product-specific Q&A, and add `AggregateRating` only when real reviews exist.
2. Consolidate variants; write unique, structured descriptions from attributes.
3. Implement URL pagination and server-rendered category pages; add `rel=next`.
4. Canonicalise query-param URLs; `noindex, follow` internal search results.
5. Prune: remove or noindex zero-inventory categories, cities and service types.
6. Fix duplicate blog slugs with 301s; align sitemap `lastmod` with reality.
7. Build a real internal-linking layer (related categories, vendor pages, buying guides that link to buyable products).
8. Add brand assets to OG/Twitter metadata.
9. Publish editorial standards, author bios and sources for the blog.

---

## 12. Performance and technical delivery

### 12.1 Stack

- **Framework:** Next.js (App Router) — `x-powered-by: Next.js`, `x-nextjs-prerender: 1`, `x-nextjs-stale-time: 300`.
- **Hosting:** Vercel, `iad1` region, edge cache `HIT`, Brotli compression.
- **Images:** Next Image optimizer proxying `demo-client.us` and `res.cloudinary.com`.
- **Fonts/icons:** Font Awesome 6.5.1 CSS loaded from `cdnjs.cloudflare.com`.
- **API:** separate `api.problack.co` service.
- **Vendor app:** separate SPA at `app.problack.co`.

### 12.2 Observations

1. **Automated Lighthouse hung.** The run returned `PAGE_HUNG` ("the page stopped responding") on the homepage at 1280×720 mobile emulation. That may be bot mitigation or a heavy main-thread workload, but it needs investigation: if a real browser can hang, so can a shopper on a mid-range phone.
2. **Image sizing.** Product markup requests `w=3840&q=75` for grid images and `w=256` for thumbnails. Next Image will emit `srcset`, so browsers can downshift, but the default is aggressive and the source host is external. Every image is a proxied third-party fetch on a cache miss.
3. **Broken icon-font URLs.** On product pages, the inline `@font-face` blocks contain malformed sources:
   `url(https://problack.co/product/%22https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/webfonts/fa-solid-900.woff2%22)`
   The quoted absolute URL has been resolved as a path, so the font files 404 and icons fall back or disappear. The page also pulls the full Font Awesome stylesheet from a third-party CDN (render-blocking, ~100 KB) to render a handful of icons.
4. **Client-side pagination.** "Load more" requires JS and additional API calls; no progressive enhancement.
5. **Heavy client components.** Tabbed product content, filters, search and cart are all client-rendered; the server HTML contains only the first state.
6. **No visible preconnect** to `demo-client.us` or the image CDN in the reviewed pages.

### 12.3 Recommended fix (performance)

1. Re-run Lighthouse/WebPageTest manually and fix whatever causes `PAGE_HUNG` (long tasks, hydration, third-party scripts).
2. Self-host icon fonts (or use inline SVG) and remove the malformed `@font-face` rules; drop Font Awesome CSS.
3. Set explicit `sizes` and image widths per breakpoint; move images to the primary domain or a controlled CDN.
4. Preconnect to the image host; add `fetchpriority="high"` to the hero image only.
5. Server-render pagination and critical product data; hydrate interactivity progressively.
6. Add performance budgets and Lighthouse CI to the deploy pipeline.

---

## 13. Security and privacy

### 13.1 Response headers

Observed on `https://problack.co`:

```
strict-transport-security: max-age=63072000
x-powered-by: Next.js
server: Vercel
```

Missing:

- `Content-Security-Policy`
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options` / `frame-ancestors`
- `Referrer-Policy`
- `Permissions-Policy`
- `Cross-Origin-Opener-Policy` / `Cross-Origin-Resource-Policy`

HSTS is present but lacks `includeSubDomains` and `preload`, leaving `app.` and `api.` subdomains outside the policy.

### 13.2 API surface

`https://api.problack.co/` responds `{"status":"ok","message":"Server running"}`, and unknown routes return a descriptive error that echoes the full path and query string:

> `{"status":"fail","message":"Cant't find route for /api/products?limit=2 this url."}`

The typo ("Cant't") is cosmetic; the behaviour is informative to attackers and suggests a custom router without a central 404 handler. No rate limiting or WAF behaviour was observable through passive testing.

### 13.3 Privacy

- No cookie banner or consent manager was observed.
- The privacy policy does not mention cookies, analytics, pixels or the website.
- The site loads a third-party CDN stylesheet (cdnjs) — a supply-chain dependency without SRI hashes.
- The contact form collects name, email, phone and message and enables SMS consent; retention and processor details are not published.
- Google Play data-safety disclosure says the app may **share** personal, financial and device data with third parties — broader than the privacy policy suggests.

### 13.4 Recommended fix (security)

1. Add CSP (report-only first), `nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`, frame protection.
2. Extend HSTS to `includeSubDomains; preload` once all subdomains are HTTPS-only.
3. Remove `x-powered-by`.
4. Add SRI to third-party assets or self-host them.
5. Replace API route echoes with generic errors; add rate limiting and request IDs.
6. Implement cookie consent and a cookie policy; document analytics and retention.
7. Review the unauthenticated delete-account flow immediately.

---

## 14. Accessibility

Verified observations (not a full WCAG audit):

| Issue | Example |
|---|---|
| Images with empty `alt` | Homepage benefit icons (`icon-verified.png`, `icon-secure.png`, etc.) render as `![]`; business profile logo duplicated with empty alt |
| Icon-only links without accessible names | Footer social links render as `[](https://facebook.com/…)`, `[](https://instagram.com/…)`, `[](https://tiktok.com/…)`, `[](https://youtube.com/…)` |
| Content not in the DOM until interaction | Product Specifications/FAQs and most FAQ answers are absent from server HTML |
| No skip link | Not observed in the rendered header |
| No accessibility statement | Not found on the site or in the sitemap |
| Form validation/labels | Contact form labels are present and readable; login/signup rely on placeholder-like fields ("Full Name", "Email") without visible required markers beyond `*` on vendor signup |
| Motion/contrast | Not measured; must be tested with axe/WAVE and manual keyboard/screen-reader passes |

For a marketplace whose mission is inclusion, accessibility is also a brand statement. A WCAG 2.2 AA audit is inexpensive relative to the legal and reputational exposure of an inaccessible checkout.

---

## 15. Mobile apps and cross-channel consistency

| Item | iOS | Android |
|---|---|---|
| Listing | `id6748367144` (Pro Black) | `com.blackownedbusiness` |
| Second link on site | Footer "Get the app" → `id6449268531`, which does **not** match the app promoted on the page | — |
| Developer | Freddie Sherman (individual) | Freddie Sherman (individual) |
| Ratings | **None** ("hasn't received enough ratings") | No rating shown |
| Installs | — | **50+** |
| Size | 35.8 MB | — |
| Price | Free | Free, with in-app purchases |
| Privacy policy link | `problack-lp.vercel.app/privacy-policy.html` | `problack.co/privacy-policy` |
| Support contact | App Store developer page | **fjsherman1@gmail.com**, +1 757-870-4183 |
| Copyright | © 2025 Pro Black Inc. | — |
| Last update | v1.3, Aug 24 | Aug 19, 2026 |

Problems:

1. **Two App Store IDs** on the same site — one is stale or points to a different build/product.
2. **50+ installs** is inconsistent with "50K+ Active Members" and "5K+ Happy Customers."
3. **Personal Gmail** as the public support contact for a marketplace handling payments.
4. **Two different privacy policies** (site vs App Store).
5. The App page FAQ tells vendors to "start at **problack.co/signup**" — that is the **customer** signup; vendors need `app.problack.co/signup`.
6. The privacy policy describes only the Android app, yet iOS exists.

---

## 16. Support and operations

- **One inbox:** every contact topic (orders, refunds, vendor applications, partnerships, press) routes to `info@problack.co`. No ticketing, no SLA per topic, no phone on the contact page.
- **Two phone numbers:** site says +1 (859) 300-3983, Mon–Fri 9–6 EST; Google Play says +1 (757) 870-4183.
- **Live chat:** "Start Chat" is offered on the support page but no chat widget was observed in the page; the link target could not be verified.
- **Response promises differ:** "within one business day" (contact), "within 24 hours" (support), "up to three business days" (complex issues), "one to two business days" (FAQ).
- **Track order:** accepts a tracking ID or order number, but there is no guidance on where to find either, and no guest lookup by email.
- **Returns:** email-only, manual; no RMA portal, no return address, no carrier instructions.
- **No help centre articles:** the "Help Center" is a contact page with six FAQ questions, all collapsed.

Operationally, this is a startup support stack — acceptable at 265 orders, not at the scale the marketing claims.

---

## 17. Content and blog

### 17.1 Volume over relevance

The blog contains **80+ articles**. The most recent 12 are almost entirely about consumer tech:

- "Googlebook vs MacBook Air M5"
- "Googlebook vs Chromebook Plus"
- "Googlebook Price, Specs and Release Date"
- "Gemini on Your Laptop: Googlebook Features"
- "Pixel 11 vs Pixel 10"
- "MacBook Air M5 vs M4"
- "iPhone 18 Pro vs iPhone 17 Pro"

Only a minority relate to Black-owned business, and those that do are generic listicles ("Black-Owned Banks: The Complete 2026 List") that are not linked to any bookable product or service.

This is a programmatic-SEO content strategy attached to a mission-driven brand. It attracts tech shoppers, not conscious-spending shoppers, and it dilutes topical authority.

### 17.2 Accuracy and sourcing

The Googlebook article states as fact:

- "The Googlebook is Google's brand-new, Gemini-first flagship" at **$899**.
- Specs including "Snapdragon X Elite / Intel Core Ultra," "Android / Chrome OS," "up to 2.8K OLED touchscreen."
- "The MacBook Air M5 ships with a 512GB SSD as standard."
- Battery "up to 14h (some say 18)."

No sources, no citations, no "rumoured" hedging, no author expertise. If these products or specs are wrong or unannounced, the site is publishing misinformation under a trust-led brand. The same applies to "iPhone 18 Pro" and "Pixel 11" articles.

### 17.3 Content operations

- **Author:** all posts by "Pro Black Team"; no bio, no editorial policy, no corrections policy, no contact for editorial.
- **Dates:** article page says October 13, 2026; blog index says October 12, 2026; sitemap says 2026-10-15. Three dates for one post.
- **Duplicates:** multiple `-2` slugs indicate republished or cloned posts.
- **FAQ answers missing:** `/faq` lists 30 questions; only "What is Pro Black?" renders an answer in the HTML. The rest are collapsed and absent from source, so neither users without JS nor crawlers can read them.
- **Mission page:** repeats the widely circulated but poorly sourced "dollar circulates for 6 hours in the Black community vs 20 days in the Jewish community" claim, alongside conflicting figures ($1.3T contribution, $1.98T by 2025, $2.2T GDP, $1.4T/$1.8T buying power) with no citations and visible "From the original presentation" internal-deck language.
- **Brand article without brands:** "Brands You Thought Were Black-Owned (But Aren't)" names zero brands and offers no verifiable examples.

### 17.4 Recommended fix (content)

1. Kill or archive off-topic tech content; redirect to relevant buying guides tied to inventory.
2. Set an editorial standard: named authors, sources, dates, corrections, disclosure.
3. Fix FAQ rendering so answers are in the HTML; add FAQPage schema.
4. Replace mission-page statistics with cited, current sources — or remove them.
5. Consolidate duplicate posts with 301s; align publish dates everywhere.
6. Build content that supports commerce: "How to verify a Black-owned brand," vendor stories, category buying guides linked to real products.

---

## 18. What is working

It is worth being explicit, because the site has real strengths:

1. **Design and brand identity.** The visual system is cohesive, modern and warm; the hero, category tiles and typography are better than most early-stage marketplaces.
2. **Clear value proposition.** "Shop. Support. Empower." and the mission narrative are immediately understandable.
3. **Modern stack.** Next.js on Vercel with edge caching, Brotli and image optimisation is a sound foundation.
4. **SEO plumbing.** Sitemap index, robots.txt, canonicals, branded 404 and HTTPS/HSTS are in place — better than many launches.
5. **Page inventory.** Legal, support, contact, FAQ, app, mission, blog, directory and account pages all exist and are linked.
6. **Category breadth.** 23 categories with real content in most of them; grocery, beauty and electronics have substantial SKUs.
7. **Product page anatomy.** Gallery, breadcrumbs, price, stock, delivery estimate, wishlist, share and reviews tab are all present as components — they need data, not redesign. The underlying JSON-LD (Product/Offer/Breadcrumb/FAQ, BlogPosting) is more complete than most early-stage marketplaces.
8. **Two mobile apps.** Both stores have live listings, and the app landing page is well structured.
9. **SMS consent language.** The contact form's consent copy is better than typical.
10. **Support channels.** Email, phone and a promised chat give customers multiple routes.

The gap is not design or technology. It is **truth, data and operations**.

---

## 19. Prioritised remediation plan

### P0 — Stop the bleeding (0–30 days)

| # | Action | Owner | Effort | Why now |
|---|---|---|---|---|
| 1 | Remove "Black-owned" from catalog pages; relabel the shop as "Marketplace" until provenance exists | Marketing + Product | S | Stops active misrepresentation |
| 2 | Delist non-Black-owned brands (Cantu, Garnier, Nivea, Clinique, Estée Lauder brands, Frito-Lay, etc.) or move them to a separate, clearly labelled store | Merchandising | M | Removes the clearest evidence of deception |
| 3 | Remove all compare-at prices without documented prior selling price; delete the "no inflated 'was' prices" sentence | Pricing + Legal | M | Reference-price exposure |
| 4 | Fix Clothing & Fashion (populate or unpublish) and repoint the homepage hero | Merchandising | S | Broken primary funnel |
| 5 | Reconcile all public numbers to one audited source; delete 4.9★ and "verified reviews" | Marketing | S | Credibility |
| 6 | Publish one legal entity, address, phone and email across site and apps | Ops + Legal | S | Trust and enforceability |
| 7 | Fix vendor-signup Terms/Privacy links; log consent | Engineering | S | Contract formation |
| 8 | Resolve return/refund contradiction; remove prepaid-label promise until true | Ops + Legal | S | Consumer protection |
| 9 | Add security headers; remove `x-powered-by`; fix delete-account auth | Engineering | M | Security |
| 10 | Rewrite category intros to match actual inventory; fix wrong-product template inserts | Content + Merch | M | Product misinformation |
| 11 | Replace personal Gmail/phone on Google Play with company contacts; consolidate App Store IDs | Ops | S | Trust |

### P1 — Build the real marketplace (30–90 days)

| # | Action | Effort |
|---|---|---|
| 12 | Onboard the 18 businesses' catalogs; show "Sold by {vendor}" with profile links | L |
| 13 | Publish verification standard (ownership attestation, business registration, ID, re-verification) and a "How we verify" page | M |
| 14 | Product data enrichment: specs, variants, box contents, shipping, returns | L |
| 15 | Real search + URL pagination + facets + sort | L |
| 16 | Verified-purchase reviews; remove rating claims until volume exists | M |
| 17 | Fix Product schema (brand, weight, shipping/returns), breadcrumb URLs, duplicated FAQs; correct LocalBusiness/Service types and fields; add real review markup when reviews exist | M |
| 18 | Consolidate taxonomy; 301 query-param URLs; prune zero-inventory pages | M |
| 19 | Delete or noindex city/service pages with no listings; require ≥3 listings to publish | M |
| 20 | Cookie consent + analytics + conversion tracking | M |
| 21 | Rewrite policies for web + marketplace; add seller terms and privacy rights | L |
| 22 | Accessibility pass (WCAG 2.2 AA): alt text, labels, keyboard, contrast | M |

### P2 — Grow responsibly (90–180 days)

| # | Action | Effort |
|---|---|---|
| 23 | Curate a smaller, genuinely Black-owned catalog (200–500 SKUs) and market that number honestly | L |
| 24 | Editorial standards, named authors, sourcing, corrections policy | M |
| 25 | Performance program: icon fonts, image budgets, Lighthouse CI | M |
| 26 | Vendor success program: onboarding, photography, fulfilment SLAs | L |
| 27 | Returns/refund automation and RMA portal | L |
| 28 | Public trust centre: verified vendors, claims register, security, accessibility | M |
| 29 | Consider third-party audits (B Corp-style, Black-owned certification partners) | M |

### If the strategic answer is "we are a deals site"

Then:

1. Remove Black-owned language from the shop entirely.
2. Keep the directory as a separate, verified product with its own brand.
3. Rebuild the catalog narrative around price and convenience.
4. Remove the mission claims from commerce pages.

Trying to be both without operational separation is the current failure mode.

---

## 20. Appendices

### Appendix A — Page inventory

| URL | Status | Notes |
|---|---|---|
| `/` | 200 | Strong design; stats inconsistent; OG image is a product photo |
| `/shop` | 200 | ~19 products; no pagination URLs; no filters |
| `/shop/clothing-and-fashion` | **200 but empty** | Zero products; homepage hero links here |
| `/shop/beauty` | 200 | Products present; intro partly mismatched |
| `/shop/electronics` | 200 | Intro promises cameras; lists batteries/headphones |
| `/shop/jewelry-and-accessories` | 200 | Intro promises men's watches; lists women's jewelry |
| `/shop/grocery` | 200 | Mass-market CPG, not Black-owned |
| `/shop/financial-services` | 200 | Calculators, not financial services |
| `/shop/deals` | 200 | "No inflated 'was' prices" claim contradicted |
| `/shop/top-categories` | 200 | 21 categories, `?category=` URLs |
| `/services` | 200 | 8 listings; dozens of 0-listing categories; 4.9★ claim |
| `/black-owned-businesses` | 200 | 5 states / 19 cities only |
| `/black-owned-businesses/georgia` | 200 | No Georgia businesses; self-referential links |
| `/business/ne-ndoro` | 200 | 1 service; AI-generated image filename |
| `/business/lujis-chocolate` | 200 | 0 services, 0 products, 0 reviews |
| `/services/custom-tailoring` | 200 | "Other" category; location = "US" |
| `/blogs` | 200 | 80+ posts; off-topic tech content |
| `/blogs/googlebook-vs-macbook-air-m5-2026` | 200 | Unsourced product claims |
| `/blogs/brands-you-thought-were-black-owned-but-aren-t` | 200 | Names no brands |
| `/faq` | 200 | Answers not rendered |
| `/contact` | 200 | One email for all topics |
| `/support` | 200 | Phone; "Live Chat" unverified |
| `/app` | 200 | Wrong vendor-signup URL; two App Store IDs on site |
| `/our-mission` | 200 | Debunked circulation stat; uncited GDP figures |
| `/cart` | 200 | Empty-state works |
| `/checkout` | → `/cart` | Protected/empty redirect |
| `/login`, `/signup` | 200 | Work; main signup policies link correctly |
| `app.problack.co/signup` | 200 | Terms/Privacy links are `#`; stats contradict site |
| `/track-order` | 200 | No guidance; disallowed in robots |
| `/delete-account` | 200 | Unauthenticated request flow — review |
| `/privacy-policy` | 200 | App-only; Williamsburg address |
| `/terms-of-service` | 200 | App-only |
| `/return-policy` | 200 | Prepaid label promise |
| `/refund-policy` | 200 | Contradicts return policy |
| `/search` | **404** | No search route |
| `/api/products` | **404** | No public catalog API |
| `/product/{slug}` | 200 | Sold by ProBlack Team; empty tabs; 0 reviews |

### Appendix B — Product sample (excerpt)

Full dataset: `product-sample-audit.csv` (105 listings, 13 views).

| Category | Product | Brand shown | Price | "Was" | Seller |
|---|---|---|---|---|---|
| Jewelry | May Birthstone 18K White Gold Plated Jewelry | Cate & Chloe | $45.49 | $388.70 | ProBlack Team |
| Jewelry | Mckayla 18K White Gold Plated Set | Cate & Chloe | $45.49 | $388.70 | — |
| Jewelry | Cordelia 18K White Gold Plated Set | Cate & Chloe | $45.49 | $388.70 | — |
| Electronics | Bose QC35 II Wireless Headphones | Bose | $365.92 | $512.88 | ProBlack Team |
| Electronics | Portable Bluetooth Speaker 30W | CASCHO | $855.40 | $1,002.86 | ProBlack Team |
| Electronics | Veatool T8 Wireless Earbuds | Pro Black | $32.32 | $293.90 | — |
| Electronics | Veatool Mini Go Headphones | Pro Black | $44.08 | $293.90 | — |
| Beauty | Cantu Shea Butter Leave-In Cream | Pro Black | $5.97 | — | ProBlack Team |
| Beauty | Garnier Fructis Bouncy Curls Gel | Pro Black | $4.36 | — | — |
| Beauty | Clinique Discover 3-Piece Set | Pro Black | $28.60 | — | — |
| Grocery | Frito Lay Classic Mix, 18 count | Pro Black | $9.97 | — | — |
| Grocery | Barilla Fettuccine, 16 oz | Barilla | $2.39 | — | — |
| Financial | Cassida 9900R Money Counter | Pro Black | $1,583.99 | — | — |
| Toys | LEGO Jade Rabbit Building Set | Pro Black | $26.22 | — | ProBlack Team |
| Toys | Baby Infant Rattle Socks | Pro Black | $14.29 | $16.89 | — |
| Search | Apple iPhone 13, unlocked 128GB | Apple | $388.70 | — | — |

### Appendix C — Claim ledger

| Claim | Location | Status | Required action |
|---|---|---|---|
| "9,807 products from Black-owned sellers" | Homepage | Unsupported | Replace with audited counts of verifiably Black-owned SKUs |
| "19 verified businesses in 14 states" | Homepage | 18 businesses; 5 states shown | Reconcile |
| "89 community members" | Homepage | Conflicts with 50K+ | Reconcile |
| "265 orders placed securely" | Homepage | Conflicts with 2K+ bookings | Reconcile |
| "69 Black-owned sellers" | Homepage | Conflicts with 150+/500+ | Reconcile |
| "150+ Active Vendors" | Vendor signup | 18 businesses | Reconcile |
| "500+ Black-owned businesses" | Vendor signup | 18 businesses | Reconcile |
| "50K+ Active Members" | Services | 50+ app installs | Reconcile |
| "5K+ Happy Customers" | Vendor signup | No supporting data | Reconcile |
| "4.9★ Average Rating" | Services | 0 reviews | Remove |
| "Every discount is a genuine reduction… no inflated 'was' prices" | Deals | Contradicted | Remove until true |
| "Verified reviews from real customers" on every listing | Shop | 0 reviews | Remove |
| "Every business verified" | FAQ / sitewide | No standard published | Publish standard |
| "Returns are free — prepaid label included" | Return policy | Not operationally supported | Remove until true |
| "Everything on problack.co, built for your phone" | App page | App has 50+ installs, no ratings | Softer, accurate copy |

### Appendix D — Evidence log

Direct observations captured during the audit:

1. Homepage stats block: 9,807 / 19 / 89 / 265; vendor block "Join 69 Black-owned sellers."
2. Vendor signup hero: "Join 500+ Black-owned businesses"; 150+ Active Vendors; 2K+ Total Bookings; 5K+ Happy Customers; Terms/Privacy links `#`.
3. Services hero: 50K+ Active Members; 4.9★ Average Rating; 8 total listings across all categories.
4. Product pages (May Birthstone, Bose QC35 II, LEGO Jade Rabbit, Cantu, Portable Speaker): all "Sold by ProBlack Team — Verified Seller"; all "Reviews (0)"; no specifications.
5. LEGO PDP copy: "Offered in size SMALL for a comfortable fit… Soft, safe materials designed for little hands… sounds babies love."
6. Speaker PDP: $855.40 (was $1,002.86); "comfortable, lightweight design for all-day wear."
7. Deals page: 2,052 products; "Every discount is a genuine reduction… no inflated 'was' prices"; $388.70 repeated.
8. Clothing category: zero product cards across the full page.
9. Search `shea`: 4 results; `luji`: no products found.
10. `businesses.xml`: 18 URLs. `services.xml`: 3 URLs. `locations.xml`: 24 URLs. `seo-pages.xml`: 8 chunks (~400+ URLs).
11. Privacy Policy: "Pro Black mobile application… available on the Google Play Store"; address 3009 Sweet Gum Lane, Williamsburg, VA 23185.
12. Footer: 8401 Mayland Dr #7269, Richmond, VA 23294; "Powered by Wix Website Developers"; App Store link id6449268531.
13. Contact page: all four topics → info@problack.co.
14. Support page: +1 (859) 300-3983, Mon–Fri 9–6 EST.
15. Google Play: 50+ downloads; developer Freddie Sherman; fjsherman1@gmail.com; +1 (757) 870-4183.
16. App Store: no ratings; privacy policy at problack-lp.vercel.app; © 2025 Pro Black Inc.
17. Response headers: HSTS only; `x-powered-by: Next.js`; no CSP/XCTO/XFO/Referrer-Policy/Permissions-Policy.
18. Product JSON-LD: five blocks — Organization, WebSite, Product/Offer, BreadcrumbList, FAQPage. Missing `brand` and `AggregateRating`; FAQPage repeats two generic questions; Offer declares $12 shipping and FreeReturn, contradicting "calculated at checkout" and the Refund Policy; LEGO schema declares weight 1 LBR; breadcrumb category URL uses a query string. Business page uses `HairSalon` schema for a tailoring business; Service schema has a truncated description and stores duration in `serviceOutput`.
19. Lighthouse run: `PAGE_HUNG`.
20. Malformed Font Awesome `@font-face` URLs on product pages.
21. Blog dates: page Oct 13 / index Oct 12 / sitemap Oct 15.
22. Blog duplicate slugs (`-2`) in `blog.xml`.
23. Mission page: "From the original presentation"; $1.3T GDP, 2% recirculation, $1.98T by 2025, $2.2T; 6-hour/20-day/30-day dollar-circulation claims uncited.
24. Ne Ndoro service image filename: `ChatGPT Image Dec 30, 2025, 07_45_48 PM.png`.
25. Luji's Chocolate profile: 0 services, 0 reviews, 1 photo (same as logo).

### Appendix E — Verification standard checklist (recommended)

For every vendor and product, require and record:

1. **Legal entity name** and state of registration (Secretary of State filing).
2. **Ownership attestation** signed by a person with ≥51% ownership, with ID verification.
3. **Black ownership definition** (e.g. ≥51% Black-owned and Black-controlled), published publicly.
4. **Evidence type** (certification body, self-attestation + documents, or third-party verification).
5. **Verification date, verifier and expiry** (annual re-verification).
6. **Product provenance**: vendor SKU, manufacturer, fulfilment location.
7. **Permission to sell branded goods** (authorised reseller documentation) where applicable.
8. **Public profile fields**: verification badge with tooltip, verification date, "how we verify" link.
9. **Revocation process** and appeals.
10. **Audit log** retained for regulator/partner review.

---

### Closing note

Pro Black does not have a design problem. It has a **truth problem**. The site looks like a marketplace; the data says it is a drop-ship store with a directory attached. Fixing the catalog — fewer products, real vendors, real prices, real reviews — would do more for conversion, SEO and legal exposure than any redesign.

The fastest credible path is:

1. **Tell the truth now** (remove unsupported claims).
2. **Shrink to quality** (200–500 verified Black-owned SKUs).
3. **Prove it** (public verification standard, real reviews, real numbers).
4. **Then scale.**

*End of report.*

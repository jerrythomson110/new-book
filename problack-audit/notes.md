# Pro Black (problack.co) — Audit working notes

## Stack / infra observed
- Next.js (App Router), hosted on Vercel (x-vercel-cache HIT, iad1), HSTS 2 years
- Images served through Next Image optimizer from demo-client.us (external image host, oddly named)
- Separate API at api.problack.co ("Server running")
- Vendor app at app.problack.co
- robots.txt: allows all AI + search bots except /api/, order-confirmation, invoice, reset/verify, track-order, track-booking
- Sitemap index: pages, product-categories, products, blog, locations, seo-pages, businesses, services
- No site search route (/search = 404). No /api/products public route.
- 23 product categories in sitemap; homepage nav only 9 categories.

## Claims vs reality
- Homepage stats: 9,807 products, 19 verified businesses in 14 states, 89 community members, 265 orders
- Services page hero: "50K+ Active Members", "4.9★ Average Rating", "Discover from thousands"
- Actual service listings: 8 total (Beauty 2, Clothing & Fashion 2, Accounting & Tax 1, Business & Industrial 1, Food & Beverage 1, Wellness 1)
- Dozens of service categories with 0 listings still linked/indexable
- Homepage "Join 69 Black-owned sellers" vs "19 verified businesses" — inconsistent

## Product issues (sample 1: May Birthstone 18K White Gold Plated Jewelry)
- Sold by "ProBlack Team / Verified Seller" — platform itself, not a Black-owned vendor
- Brand field "Cate & Chloe" (mass-market jewelry brand) but seller is ProBlack
- Generic AI boilerplate description, no real specs (no metal, stone, dimensions, weight)
- "Value 1-pack", "clean white finish" — template language lifted from generic import
- $45.49 vs $388.70 "Save 88%" — implausible anchor price
- Reviews (0) tab — zero reviews
- Many SKUs branded Clinique, Elizabeth Arden, Nivea, LEGO, Nike? — not Black-owned
- Product titles truncated mid-word in cards and slugs ("...Colored P", "Chops Thick Hi")

## Category bug
- /shop/clothing-and-fashion renders ZERO products (only description + empty grid), while title promises dresses/tops
- /shop/beauty renders products

## Trust / legal
- Privacy Policy + Terms written for the mobile app only ("available on Google Play Store"), never mentions website/cookies
- Privacy effective 2025-09-20; Terms effective 2025-01-01
- Address: 3009 Sweet Gum Lane, Williamsburg, VA 23185
- Contact page: all 4 topics point to info@problack.co (no routing)
- Support page: phone +1 859 300 3983, Mon-Fri 9-6 EST, "Live Chat" button
- No returns/shipping policy pages found in sitemap (FAQ references return policy but answer not rendered)

## FAQ
- Answers are collapsed; only "What is Pro Black?" renders text. 30 questions, zero answers in HTML (indexable content missing)

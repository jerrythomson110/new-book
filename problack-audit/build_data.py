import csv, re, statistics
from collections import Counter

# (category, title, brand, price, compare_at, pdp_seller, flags)
R = []
def add(cat,title,brand,price,cmp=None,seller="",flags=""):
    R.append(dict(category=cat,title=title,brand_shown=brand,price=price,compare_at=cmp,
                  pdp_seller=seller,flags=flags))

# --- Jewelry & Accessories (19 cards observed) ---
add("Jewelry & Accessories","May Birthstone 18K White Gold Plated Women Jewelry","Cate & Chloe",45.49,388.70,"ProBlack Team","repeated_anchor;template_copy;no_specs;zero_reviews;category_copy_mismatch")
add("Jewelry & Accessories","Mckayla 18K White Gold Plated Silver Jewelry Set","Cate & Chloe",45.49,388.70,"","repeated_anchor;template_copy")
add("Jewelry & Accessories","Viviana 18k White Gold Plated Silver Jewelry Set with Swarovski Crystals for Women","Cate & Chloe",34.99,299.00,"","repeated_anchor")
add("Jewelry & Accessories","Cordelia 18K White Gold Plated Silver Jewelry Set","Cate & Chloe",45.49,388.70,"","repeated_anchor")
add("Jewelry & Accessories","Blake 18k White Gold Plated Halo Jewelry Set with Simulated Diamonds Gift for Women","Cate & Chloe",34.99,299.00,"","repeated_anchor")
add("Jewelry & Accessories","Women's Silver Plated Crystal Heart Earring","Believe by Brilliance",23.32,None,"","")
add("Jewelry & Accessories","51 Pcs Gold Silver Jewelry Set with 6 Pcs","DIY.STORE",16.89,None,"","")
add("Jewelry & Accessories","5PCS Elegant Crystal Delicate Jewelry Sets","K-KED",18.93,None,"","")
add("Jewelry & Accessories","Women Elegant Bridal Party Jewelry Sets Wedding","OEOEOS",24.69,None,"","")
add("Jewelry & Accessories","Bridal Women Necklace Faux Pearl Rhinestone Wedding Earrings Jewelry Set","SPRING PARK",7.86,8.83,"","")
add("Jewelry & Accessories","Prom Earrings Necklace Bracelet Set Elegant","esunarty",17.80,None,"","")
add("Jewelry & Accessories","Women Fashion Rhinestone Pendant Necklace Ring Bracelet Earrings Jewelry Set Red","Ruanlalo",17.29,None,"","")
add("Jewelry & Accessories","Noble Black Crystal Jewelry Set for Women, Luxury Necklace Earring, Bridal Wedding Chokers","VMENG YZYI",24.99,None,"","")
# --- Electronics (19 cards observed) ---
add("Electronics","Watch Battery Ctl1616 Ctl1616f Battery Watch Solar Rechargeable","Genuine Parts Company",24.38,None,"","category_mismatch;category_copy_mismatch")
add("Electronics","T Mobile Samsung A16","Samsung",360.04,None,"","")
add("Electronics","Watch Box for Men, 6 Slot Watch Display Case with Drawer, 2-Layer Jewelry and Watch Storage","YMWVH",19.60,22.88,"","category_mismatch")
add("Electronics","P6P 1.96\" HD Touch Screen 100+ Sports Modes Smart Watches (Answer/Make Call) with LED Flashlight","VOPOCO",47.99,None,"","")
add("Electronics","Wireless Headphone Bluetooth 5.4, 40H Playtime, 3EQ, 4 Mic ENC Noise Cancelling","Pro Black",19.89,159.99,"","repeated_anchor")
add("Electronics","Skullcandy Crusher ANC XT 2 Over-Ear Noise Cancelling Headphones, Black","Pro Black",202.89,None,"","")
add("Electronics","Oneodio Bluetooth Over Ear Headphones with Mic","Pro Black",58.77,None,"","")
add("Electronics","Wireless Earbuds Bluetooth 5.4 Headphones in Ear","Pro Black",26.44,32.32,"","")
add("Electronics","Veatool T8 Wireless Earbuds Bluetooth Headphones","Pro Black",32.32,293.90,"","repeated_anchor")
add("Electronics","Veatool Mini Go Wireless Retro Headphones 100 Hours","Pro Black",44.08,293.90,"","repeated_anchor")
add("Electronics","Beats by Dr. Dre Solo3 Active Noise Cancellation Bluetooth On-Ear Headphones, Black","Beats by Dr. Dre",198.99,None,"","")
add("Electronics","JLab JBuds Lux ANC Over-Ear Wireless Headphones, 70-Hour Battery, Graphite","JLab",41.99,79.99,"","")
add("Electronics","Bose Quietcomfort 35 Ii Wireless Headphones Black","Bose",365.92,512.88,"ProBlack Team","template_copy;no_specs;zero_reviews")
add("Electronics","Portable Bluetooth Speaker Ipx7 Waterproof 30W","CASCHO",855.40,1002.86,"ProBlack Team","implausible_price;template_copy;no_specs;zero_reviews")
# --- Beauty (14 cards observed) ---
add("Beauty","Elizabeth Arden 9-Piece Skincare & Beauty Gift Set with Ceramide Capsules, Retinol, Creams, Lipstick, Mascara","Pro Black",75.99,None,"","")
add("Beauty","Glow Recipe Fruit Babies Skincare Kit Gift Set","Pro Black",97.49,None,"","")
add("Beauty","Medicube Intensive Moisture and Skin Plumping Set","Pro Black",55.61,None,"","")
add("Beauty","Florence by Mills Have a Good Day Set","Pro Black",49.40,None,"","")
add("Beauty","12PK SKIN627 Hydrating Ceramide with Panthenol Face Masks","Pro Black",14.99,None,"","")
add("Beauty","5PCS Rice Face Routine Set Hydration Face Care Kit","Pro Black",22.78,None,"","")
add("Beauty","Clinique Discover 3 Piece Set","Pro Black",28.60,None,"","")
add("Beauty","ZealSea Collagen Face Mask Anti Aging Hydrating Sheet Mask","Pro Black",17.98,22.99,"","")
add("Beauty","Tula Skin Care 24 7 Moisture Hydrating Day","Pro Black",62.99,83.98,"","")
add("Beauty","Nivea Cocoa Butter Body Lotion for Dry Skin","Pro Black",10.36,None,"","")
add("Beauty","Tiege Hanley Men's Skin Care Set Rejuvenation Skin","Pro Black",162.50,None,"","")
add("Beauty","Vibriance Bundle Skincare Set | Super C Serum, Cleanser and Face Cream","Pro Black",95.00,None,"","")
add("Beauty","Good Molecules Skin Prep Essentials Kit","Pro Black",23.36,None,"","")
# --- Financial Services (13 cards observed) ---
add("Financial Services","default Texas Instruments TI-30Xa Scientific Calculator","Pro Black",15.15,None,"","category_mismatch;bad_title_prefix")
add("Financial Services","El506wbbk Scientific Calculator","Pro Black",37.69,None,"","category_mismatch")
add("Financial Services","Texas Instruments Ti 30XS Multiview Scientific Calculator","Texas Instruments",27.29,None,"","category_mismatch")
add("Financial Services","Casio FX-9910CW ClassWiz Advanced Scientific Calculator, Black","Casio",24.98,None,"","category_mismatch")
add("Financial Services","potrochi 2-Line Engineering Scientific Calculator, Cute Desk Accessories","Pro Black",9.99,None,"","category_mismatch")
add("Financial Services","FX-115ESPLS2-S 2nd Edition Scientific Calculator 12-Digit","Pro Black",33.00,None,"","category_mismatch")
add("Financial Services","Casio Fx 55PLUS Scientific Calculator 10 Digits","Casio",24.69,None,"","category_mismatch")
add("Financial Services","Fitop XR598 Money Counter - USD & EUR, MG/UV Detection","Pro Black",62.99,None,"","category_mismatch")
add("Financial Services","Cassida 9900R V2 2-Pocket Premium Bank Grade Money Counter","Pro Black",1583.99,None,"","category_mismatch;implausible_price")
add("Financial Services","Texas Instruments 30XSMV/TBL (5-Pack) TI-30XS Scientific Calculator","Texas Instruments",98.99,None,"","category_mismatch")
add("Financial Services","Nadex Scientific Calculator with Graph Functions","Pro Black",39.99,None,"","category_mismatch")
add("Financial Services","Casio FX-115ESPLSB Advanced Scientific Calculator","Casio",22.64,None,"","category_mismatch")
# --- Grocery (14 cards observed) ---
add("Grocery","Frito Lay Classic Mix Variety Pack, 1 oz Bags, 18 count","Pro Black",9.97,None,"","")
add("Grocery","Frito Lay Classic Mix Chips Variety pack, Mega Size, 1 oz, 42 Count","Pro Black",19.98,None,"","")
add("Grocery","Barilla Classic Non-GMO, Kosher Certified Fettuccine Pasta, 16 oz","Barilla Classic Non-GMO",2.39,None,"","")
add("Grocery","(7 pack) Urban Accents Roasted Garlic & Rosemary Veggie Roaster Seasoning Blend","Pro Black",38.49,None,"","")
add("Grocery","Frontier Co-op Dill Weed, Chopped, 0.35 oz (10 g)","Frontier Co-op Dill",4.91,None,"","")
add("Grocery","La Banderita Soft Taco Flour Tortillas, 16 oz, 10 Count","La Banderita Soft",3.55,None,"","")
add("Grocery","Bertolli Organic Extra Virgin Olive Oil Spray, Rich Taste","Bertolli Organic Extra",6.08,None,"","")
add("Grocery","Gamesa Saladitas Saltine Crackers, 16.2 oz","Gamesa Saladitas Saltine",6.66,None,"","")
add("Grocery","Ol Mexican Foods Xtreme Wellness High Fiber Zero Net Carbs Street Taco Wraps","Ol Mexican Foods",4.38,None,"","")
add("Grocery","La Moderna Fideo Macaroni, 7.05 oz","La Moderna Fideo",8.32,None,"","")
add("Grocery","(6 pack) Knorr Shelf Stable Granulated Chicken Bouillon, 32 oz Jar","Pro Black",45.80,None,"","")
add("Grocery","Barilla Classic Non-GMO, Kosher Certified Spaghetti Pasta, 16 oz","Barilla Classic Non-GMO",2.39,None,"","")
add("Grocery","(3 pack) Margaret Holmes Seasoned Turnip Greens, 27 oz Can","Pro Black",9.24,None,"","")
add("Grocery","Simply Organic Ground Turmeric, 2.38 oz Bottle","Simply Organic Ground",6.81,None,"","")
# --- Books & Media (6 cards) ---
add("Books & Media","For Whom the Belle Tolls (Paperback)","Pro Black",11.91,None,"","")
add("Books & Media","The Ballad of Songbirds and Snakes: Deluxe Edition (a Hunger Games Novel) (Paperback)","Pro Black",9.50,None,"","")
add("Books & Media","The Four Winds: A Novel","Pro Black",14.92,None,"","")
add("Books & Media","Hollow (Deluxe Limited Edition)","Pro Black",25.35,None,"","")
add("Books & Media","Shallow River","Pro Black",18.51,None,"","")
add("Books & Media","For Richer, For Poorer: A Novel","Pro Black",16.90,18.85,"","")
# --- Toys (cards) ---
add("Toys & Games","Lego Jade Rabbit Building Toy Set Fun Bunny","Pro Black",26.22,None,"ProBlack Team","template_copy;wrong_product_copy;no_specs;zero_reviews;brand_mismatch")
add("Toys & Games","Wooden Sticks and Rings Stem Construction Building Montessori Toys","Pro Black",18.19,None,"","")
add("Toys & Games","Rubiks Race Classic Fast Paced Strategy Travel Board","Pro Black",15.08,None,"","")
add("Toys & Games","Annexfun 200PCS Magnetic Blocks with Light Up","Pro Black",57.45,None,"","")
# --- Baby ---
add("Baby & Kids","Baby Infant Rattle Socks Toys 3 6 to 12 Months","Pro Black",14.29,16.89,"","")
add("Baby & Kids","Bebe Fuerte Move and Groove Crinklie Panda Newborn Infant","Bebe Fuerte",12.55,None,"","")
add("Baby & Kids","homicozy Art Supplies Kit for Kids Ages 4-12, Mermaid Art Case Coloring Set","Pro Black",20.62,20.98,"","truncated_title")
# --- Pet ---
add("Pet Supplies","Bullibone Nylon Bone Dental Hygiene Dog Chew Toy","Pro Black",20.99,None,"","")
add("Pet Supplies","Dog Toys for Small Dogs, 7 Pack Puppy Chew Toys for Teething and Training","Pro Black",16.14,None,"","truncated_title")
add("Pet Supplies","2 Pack Tough Nylon Dog Chew Toys for Aggressive Chewers","Pro Black",17.99,None,"","")
# --- Office ---
add("Office Supplies","Clackibukvyz 2 Pack Desk Organizer with 2 Drawer","Pro Black",16.89,None,"","")
add("Office Supplies","Intige 7 Tier Metal Mesh Desk File Organizer","Pro Black",46.79,None,"","")
add("Office Supplies","Vusign Desk Organizer with 2 Drawer Multi-Functional Pencil Holder","Pro Black",33.58,70.19,"","")
# --- Home & Garden ---
add("Home & Garden","Expert Gardener Floral Tool 3 Piece Set","Pro Black",14.97,None,"","")
add("Home & Garden","Garden Loppers Pruning Shears, Updated 3PCS Hedge Clippers Combo Set","Pro Black",28.99,49.99,"","truncated_title")
add("Home & Garden","Gped Reversible Sofa Cover Water Resistant Couch Cover","GPED",28.59,51.99,"","")
add("Home & Garden","Meromore Garden Tools 7 Piece Gardening Hand Tools","Pro Black",24.69,28.59,"","")
# --- Search: shea ---
add("Search: shea","Buttah Skin Complete Skin Kit - Cleanser, Vitamin C Serum & Shea Butter","Pro Black",54.98,65.00,"","")
add("Search: shea","Cantu Shea Butter Leave-In Conditioning Repair Cream, 16 oz","Pro Black",5.97,None,"ProBlack Team","brand_mismatch;template_copy;no_specs;zero_reviews")
add("Search: shea","Garnier Fructis Style Bouncy Curls Hair Styling Gel with Shea Butter, 5.1 fl oz","Pro Black",4.36,None,"","")
add("Search: shea","Lottabody Wrap Me Foaming Curl Mousse with Coconut and Shea Oil, 7 fl oz","Pro Black",4.94,None,"","")
# --- Search: iphone ---
add("Search: iphone","Smart Watch Fits for Android and Iphone Ip68 Waterproof","Tikland",34.82,233.65,"","")
add("Search: iphone","Frsara Tripode de Telefono Extensible de 71\" y Stick para Selfies (Spanish listing)","FrSara",20.79,40.29,"","non_english;truncated_title")
add("Search: iphone","70'' Extendable Selfie Stick Tripod with Light & Wireless Remote","Ehxcrt",12.99,None,"","")
add("Search: iphone","Apple iPhone 11 - T-Mobile - 64 GB Black","Apple",213.63,None,"","")
add("Search: iphone","Apple iPhone X A1865 (Fully Unlocked) 256GB Silver","Apple",214.49,None,"","")
add("Search: iphone","Total Wireless Apple iPhone 17e, 512GB, 5G, White - Prepaid Smartphone [Locked]","Apple",1038.70,None,"","")
add("Search: iphone","Apple iPhone 13 - Carrier Unlocked - 128GB Red","Apple",388.70,None,"","")
add("Search: iphone","Apple iPhone 13, 128GB, 8GB RAM, 16MP FF Camera, Midnight - Prepaid","Apple",323.70,None,"","")
add("Search: iphone","Straight Talk Apple iPhone 17e, 256GB, 5G, Black - Prepaid","Apple",713.70,None,"","")
add("Search: iphone","Straight Talk Apple iPhone 17, 5G, 256GB, Mist Blue - Prepaid","Apple",1077.70,None,"","")
add("Search: iphone","Apple iPhone 13 Pro 128 GB Smartphone, 6.1\" OLED 2532 x 1170","Apple",506.91,584.97,"","")
add("Search: iphone","Cricket Wireless Apple iPhone 16e 8GB RAM (Prepaid), Midnight","Apple",388.70,None,"","")

with open("product-sample-audit.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=["#","category","title","brand_shown","price_usd","compare_at_usd","discount_pct","pdp_seller","flags","lookup_url"])
    w.writeheader()
    for i,r in enumerate(R,1):
        d = None
        if r["compare_at"]:
            d = round((r["compare_at"]-r["price"])/r["compare_at"]*100)
        import urllib.parse
        q = " ".join(re.sub(r'[^A-Za-z0-9 ]',' ',r["title"]).split()[:5])
        w.writerow({"#":i,"category":r["category"],"title":r["title"],"brand_shown":r["brand_shown"],
                    "price_usd":f'{r["price"]:.2f}',"compare_at_usd":(f'{r["compare_at"]:.2f}' if r["compare_at"] else ""),
                    "discount_pct":(d if d is not None else ""),"pdp_seller":r["pdp_seller"],"flags":r["flags"],
                    "lookup_url":f"https://problack.co/shop?search={urllib.parse.quote(q)}"})

n=len(R); disc=[r for r in R if r["compare_at"]]
print("n =",n)
print("with compare-at:",len(disc),f"({len(disc)/n*100:.0f}%)")
print("median price:",statistics.median([r["price"] for r in R]))
print("min/max:",min(r["price"] for r in R),max(r["price"] for r in R))
print("brand frequencies:",Counter(r["brand_shown"] for r in R).most_common(8))
anchors=Counter(r["compare_at"] for r in disc)
print("repeated anchors:",[(a,c) for a,c in anchors.most_common(6)])
print("discount buckets:",Counter(("80%+" if ((r['compare_at']-r['price'])/r['compare_at'])>=.8 else "50-79%" if ((r['compare_at']-r['price'])/r['compare_at'])>=.5 else "20-49%" if ((r['compare_at']-r['price'])/r['compare_at'])>=.2 else "<20%") for r in disc))
print("platform-branded rows:",sum(1 for r in R if r["brand_shown"]=="Pro Black"),f"({sum(1 for r in R if r['brand_shown']=='Pro Black')/n*100:.0f}%)")
print("PDP-sampled sellers:",Counter(r["pdp_seller"] for r in R if r["pdp_seller"]))
print("flag counts:",Counter(f for r in R for f in r["flags"].split(";") if f).most_common())
print("categories:",Counter(r["category"] for r in R).most_common())

import re, markdown

src = open("Pro-Black-Website-Audit-2026-10-20.md").read()

# Drop the manual contents block and the title/meta block (cover replaces them)
src = re.sub(r"## Contents\n.*?\n---\n\n", "", src, flags=re.S)
src = src.split("\n---\n", 1)[1].lstrip("\n") if "Audit date" in src[:600] else src

# Split title block
lines = src.splitlines()
title = "Pro Black (problack.co)"
subtitle = "Full Website & Product Catalog Audit"

md = markdown.Markdown(extensions=["tables","toc","fenced_code","sane_lists","attr_list"],
                        extension_configs={"toc":{"permalink":False}})
body = md.convert(src)

# Build TOC from h2
toc = []
for m in re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body):
    hid, text = m.group(1), re.sub(r"<[^>]+>","",m.group(2))
    if text.strip().lower().startswith("contents"): continue
    toc.append((hid, text))
nav = "\n".join(f'<a href="#{h}" class="toc-link">{t}</a>' for h,t in toc)

# Grade colouring in tables
def grade(m):
    g = m.group(1)
    cls = {"A":"g-a","B":"g-b","C":"g-c","C−":"g-c","D":"g-d","F":"g-f"}.get(g,"")
    return f'<td class="{cls}"><strong>{g}</strong></td>'
body = re.sub(r'<td><strong>(A|B|C|C−|D|F)</strong></td>', grade, body)

# Severity pills
body = body.replace("<td><strong>Critical</strong></td>", '<td><span class="sev sev-c">Critical</span></td>')
body = body.replace("<td><strong>High</strong></td>", '<td><span class="sev sev-h">High</span></td>')
body = body.replace("<td><strong>Medium</strong></td>", '<td><span class="sev sev-m">Medium</span></td>')

# Generic "200" pills in inventory table
body = body.replace("<td><strong>200 but empty</strong></td>", '<td><span class="pill pill-amber">200 · empty</span></td>')
body = body.replace("<td><strong>404</strong></td>", '<td><span class="pill pill-red">404</span></td>')

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {subtitle}</title>
<style>
  :root {{
    --ink:#151412; --ink-2:#3d3a35; --muted:#6b665e; --line:#e6e1d8;
    --paper:#fbf9f4; --card:#ffffff; --gold:#b8862b; --gold-soft:#f0e3c8;
    --green:#1f6f43; --red:#a52a24; --amber:#a86a12; --plum:#5c2a4a;
  }}
  * {{ box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; }}
  body {{
    margin:0; background:var(--paper); color:var(--ink);
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
    font-size:16.5px; line-height:1.62; -webkit-font-smoothing:antialiased;
  }}
  .shell {{ display:grid; grid-template-columns: 280px minmax(0,1fr); gap:0; max-width:1400px; margin:0 auto; }}
  /* Sidebar */
  aside {{
    position:sticky; top:0; align-self:start; height:100vh; overflow-y:auto;
    padding:34px 22px 40px; border-right:1px solid var(--line);
    background:linear-gradient(180deg,#12110f 0%, #1b1915 100%); color:#efe9dc;
  }}
  aside .mark {{ font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
    letter-spacing:.16em; text-transform:uppercase; font-size:10.5px; color:#c9a862; }}
  aside h2 {{ font-size:19px; line-height:1.25; margin:10px 0 4px; color:#fff; font-weight:600; }}
  aside .sub {{ font-size:12.5px; color:#b9b1a2; margin-bottom:22px; }}
  aside .navlabel {{ font-family: ui-sans-serif, system-ui, sans-serif; font-size:10px;
    letter-spacing:.14em; text-transform:uppercase; color:#8f8778; margin:18px 0 8px; }}
  .toc-link {{ display:block; padding:4px 0; color:#d8d0c1; text-decoration:none; font-size:12.6px;
    font-family: ui-sans-serif, system-ui, -apple-system, sans-serif; border-left:2px solid transparent; padding-left:10px; }}
  .toc-link:hover {{ color:#f2d79b; border-left-color:var(--gold); }}
  main {{ padding:0 0 80px; background:var(--paper); min-width:0; }}
  /* Cover */
  .cover {{
    padding:64px 64px 40px; background:
      radial-gradient(1200px 380px at 85% -10%, rgba(184,134,43,.18), transparent 60%),
      linear-gradient(180deg,#17150f 0%, #211d16 100%);
    color:#f6efe2; border-bottom:4px solid var(--gold);
  }}
  .cover .kicker {{ font-family: ui-sans-serif, system-ui, sans-serif; font-size:11px; letter-spacing:.22em;
    text-transform:uppercase; color:#cfa95f; }}
  .cover h1 {{ font-size:52px; line-height:1.02; margin:14px 0 6px; font-weight:600; letter-spacing:-.02em; }}
  .cover .h2 {{ font-size:24px; color:#e8dcc6; font-weight:400; font-style:italic; margin:0 0 22px; }}
  .meta {{ display:flex; flex-wrap:wrap; gap:10px 26px; font-family: ui-sans-serif, system-ui, sans-serif;
    font-size:12px; color:#c9c0af; }}
  .meta b {{ color:#f3ead9; font-weight:600; }}
  .verdict {{ margin:26px 0 0; padding:16px 18px; border-left:3px solid var(--gold);
    background:rgba(255,255,255,.055); font-size:15px; color:#efe6d5; max-width:800px; }}
  .verdict b {{ color:#f6d99b; }}
  /* Body */
  .content {{ padding:46px 64px 40px; max-width:1000px; }}
  h2 {{ font-size:29px; line-height:1.2; margin:54px 0 14px; padding-top:10px; letter-spacing:-.01em; }}
  h2:first-of-type {{ margin-top:0; }}
  h3 {{ font-size:20px; margin:30px 0 8px; }}
  h4 {{ font-size:16px; margin:22px 0 6px; font-family: ui-sans-serif, system-ui, sans-serif; letter-spacing:.01em; }}
  p {{ margin:10px 0 14px; }}
  a {{ color:#8a5a12; text-decoration:none; border-bottom:1px solid rgba(138,90,18,.3); }}
  a:hover {{ border-bottom-color:#8a5a12; }}
  ul, ol {{ padding-left:22px; }}
  li {{ margin:5px 0; }}
  strong {{ font-weight:650; }}
  hr {{ border:0; border-top:1px solid var(--line); margin:42px 0; }}
  code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size:13px;
    background:#f1ece2; padding:1.5px 5px; border-radius:4px; color:#4a3a22; }}
  pre {{ background:#17150f; color:#efe8da; padding:16px 18px; border-radius:8px; overflow:auto; font-size:12.5px; }}
  pre code {{ background:none; color:inherit; padding:0; }}
  blockquote {{ margin:18px 0; padding:14px 18px; background:#fff; border-left:3px solid var(--gold);
    border-radius:0 6px 6px 0; color:var(--ink-2); box-shadow:0 1px 0 rgba(0,0,0,.03); }}
  blockquote p {{ margin:0; }}
  /* Tables */
  .tablewrap {{ overflow-x:auto; margin:18px 0 24px; border:1px solid var(--line); border-radius:8px; background:var(--card); }}
  table {{ border-collapse:collapse; width:100%; font-family: ui-sans-serif, system-ui, -apple-system, sans-serif; font-size:13.2px; }}
  th {{ text-align:left; background:#f6f1e7; color:#4a4338; font-weight:650; padding:10px 12px;
    border-bottom:1px solid var(--line); vertical-align:bottom; }}
  td {{ padding:10px 12px; border-bottom:1px solid #efeae1; vertical-align:top; color:var(--ink-2); }}
  tr:last-child td {{ border-bottom:0; }}
  tbody tr:hover {{ background:#fdfbf6; }}
  td.g-f, td.g-d {{ font-family: ui-sans-serif, system-ui, sans-serif; }}
  td.g-f {{ color:var(--red); }} td.g-d {{ color:var(--amber); }}
  td.g-c {{ color:#7a6512; }} td.g-a, td.g-b {{ color:var(--green); }}
  .pill {{ display:inline-block; font-family: ui-sans-serif, system-ui, sans-serif; font-size:11px;
    font-weight:650; padding:2px 8px; border-radius:999px; }}
  .pill-red {{ background:#f7e3e1; color:#8d2620; }}
  .pill-amber {{ background:#f8ecd6; color:#8a5a12; }}
  .sev {{ display:inline-block; font-family: ui-sans-serif, system-ui, sans-serif; font-size:10.5px;
    font-weight:700; letter-spacing:.03em; text-transform:uppercase; padding:2px 8px; border-radius:3px; white-space:nowrap; }}
  .sev-c {{ background:#f6dedb; color:#8d1f19; }}
  .sev-h {{ background:#f8e8cf; color:#8a5310; }}
  .sev-m {{ background:#eee9dc; color:#5f5748; }}
  /* Callouts: paragraphs starting with Verdict etc. left as-is */
  .content > p:first-of-type {{ font-size:18px; color:#4a453c; }}
  footer {{ margin-top:60px; padding:26px 0 0; border-top:1px solid var(--line);
    font-family: ui-sans-serif, system-ui, sans-serif; font-size:11.5px; color:var(--muted); }}
  @media (max-width: 1080px) {{
    .shell {{ grid-template-columns:1fr; }}
    aside {{ position:relative; height:auto; display:none; }}
    .cover, .content {{ padding-left:28px; padding-right:28px; }}
    .cover h1 {{ font-size:38px; }}
  }}
  @media print {{
    aside {{ display:none; }} .shell {{ display:block; }}
    body {{ background:#fff; font-size:10.5pt; }}
    .cover {{ background:#fff; color:#000; border-bottom:2px solid #000; padding:24px 0; }}
    .cover h1, .cover .h2, .cover .meta b {{ color:#000; }}
    .verdict {{ background:#f4f2ee; color:#000; }}
    .content {{ padding:18px 0; max-width:none; }}
    h2 {{ page-break-after:avoid; }} table {{ page-break-inside:auto; }} tr {{ page-break-inside:avoid; }}
    a {{ color:#000; border:0; }}
  }}
</style>
</head>
<body>
<div class="shell">
  <aside>
    <div class="mark">Independent Audit</div>
    <h2>Pro Black</h2>
    <div class="sub">problack.co · 20 Oct 2026</div>
    <div class="navlabel">Contents</div>
    {nav}
  </aside>
  <main>
    <div class="cover">
      <div class="kicker">Website &amp; Catalog Review</div>
      <h1>Pro Black</h1>
      <div class="h2">Full Website &amp; Product Catalog Audit</div>
      <div class="meta">
        <span><b>Site</b> problack.co</span>
        <span><b>Date</b> 20 October 2026</span>
        <span><b>Pages reviewed</b> 40+</span>
        <span><b>Listings sampled</b> 105</span>
        <span><b>Verdict</b> D — not launch-ready</span>
        <span><b>Evidence</b> 8 sitemaps · 2 app stores</span>
      </div>
      <div class="verdict">
        <b>Headline:</b> the storefront looks credible, but the catalog does not support its
        central claim. Every product page examined sells via “ProBlack Team”, the sampled inventory is
        platform- or mass-market-branded, and the 18 verified Black-owned businesses have no products
        in the shop. The site’s pricing claims, statistics and policies compound the problem.
      </div>
    </div>
    <div class="content">
      {body}
      <footer>
        Independent audit · 20 October 2026 · Prepared from public pages only · Companion dataset:
        product-sample-audit.csv · This document is not legal advice.
      </footer>
    </div>
  </main>
</div>
</body>
</html>"""

# Wrap tables for horizontal scrolling
html = re.sub(r'(<table>.*?</table>)', r'<div class="tablewrap">\1</div>', html, flags=re.S)
open("Pro-Black-Website-Audit-2026-10-20.html","w").write(html)
print("html bytes:", len(html))

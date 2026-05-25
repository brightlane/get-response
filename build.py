#!/usr/bin/env python3

import os
import json
import random
import textwrap
from datetime import datetime
from pathlib import Path

# =========================================================
# GETRESPONSE AUTHORITY ENGINE 2026
# Massive SEO + AI Discovery Build System
# =========================================================

CONFIG = {
    "SITE_NAME": "GetResponse Authority",
    "BASE_URL": "https://brightlane.github.io/getresponse",
    "AFFILIATE_URL": "https://try.getresponsetoday.com/zder3vacd7wn-xlkg1t",
    "AUTHOR": 'Benny "Palmo Kid" Palmarino',
    "BRAND": "GetResponse",
    "YEAR": "2026",
    "OUTPUT_DIR": "site"
}

# =========================================================
# SEO DATA ENGINE
# =========================================================

NICHES = [
    "Affiliate Marketing",
    "Real Estate",
    "Fitness",
    "Dental",
    "Legal",
    "Roofing",
    "HVAC",
    "Ecommerce",
    "Crypto",
    "SaaS",
    "Coaching",
    "Consulting",
    "Local Business",
    "Agencies",
    "Course Creators",
]

FEATURES = [
    "Email Marketing",
    "Marketing Automation",
    "Webinars",
    "Landing Pages",
    "Funnels",
    "Autoresponders",
    "Lead Generation",
    "CRM",
    "AI Website Builder",
    "SMS Marketing",
]

KEYWORDS = [
    "best email marketing software",
    "best autoresponder",
    "marketing automation platform",
    "email funnel software",
    "landing page builder",
    "affiliate marketing tools",
    "AI email marketing",
    "best webinar platform",
]

# =========================================================
# UTILITIES
# =========================================================

def slugify(text):
    return (
        text.lower()
        .replace("&", "and")
        .replace(" ", "-")
        .replace("/", "-")
    )

def ensure_dirs():
    Path(CONFIG["OUTPUT_DIR"]).mkdir(exist_ok=True)
    Path(f"{CONFIG['OUTPUT_DIR']}/blog").mkdir(exist_ok=True)

def html_template(title, description, content, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<meta name="description" content="{description}">
<meta name="keywords" content="GetResponse review, email marketing, funnels, automation, webinars">

<link rel="canonical" href="{canonical}">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">

<style>

:root {{
    --bg:#0f172a;
    --card:#111827;
    --text:#f8fafc;
    --muted:#94a3b8;
    --green:#10b981;
    --blue:#2563eb;
}}

* {{
    box-sizing:border-box;
}}

body {{
    margin:0;
    background:var(--bg);
    color:var(--text);
    font-family:system-ui,-apple-system,sans-serif;
    line-height:1.7;
}}

.container {{
    width:min(1150px,92%);
    margin:auto;
}}

.hero {{
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    padding:70px 25px;
    border-radius:24px;
    margin:30px 0;
    text-align:center;
}}

.hero h1 {{
    font-size:2.8rem;
}}

.btn {{
    display:inline-block;
    background:var(--green);
    color:white;
    text-decoration:none;
    padding:18px 34px;
    border-radius:14px;
    font-weight:700;
    margin-top:20px;
}}

.grid {{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
    gap:24px;
}}

.card {{
    background:var(--card);
    padding:24px;
    border-radius:18px;
    border:1px solid #1e293b;
}}

.section {{
    margin:55px 0;
}}

footer {{
    text-align:center;
    margin-top:70px;
    padding:40px;
    color:var(--muted);
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th, td {{
    border:1px solid #334155;
    padding:14px;
}}

th {{
    background:#1e293b;
}}

.disclosure {{
    background:#1e293b;
    padding:20px;
    border-left:4px solid orange;
    border-radius:10px;
    margin-top:20px;
}}

</style>

<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"Product",
  "name":"GetResponse",
  "brand": {{
      "@type":"Brand",
      "name":"GetResponse"
  }},
  "offers": {{
      "@type":"Offer",
      "url":"{CONFIG['AFFILIATE_URL']}"
  }}
}}
</script>

</head>

<body>

<div class="container">

{content}

<footer>
<p>© {CONFIG['YEAR']} {CONFIG['AUTHOR']}</p>
<p>Powered by GetResponse Authority Engine</p>
</footer>

</div>

</body>
</html>
"""

# =========================================================
# PAGE GENERATORS
# =========================================================

def build_homepage():
    title = "GetResponse Review 2026: Best Email Marketing & Automation Platform"
    description = "GetResponse combines email marketing, funnels, webinars, automation and AI tools into one platform."

    content = f"""
<section class="hero">

<h1>🚀 GetResponse Review 2026</h1>

<p>
Email marketing + funnels + webinars + automation + AI websites.
Everything modern marketers need in one platform.
</p>

<a href="{CONFIG['AFFILIATE_URL']}" class="btn" rel="nofollow sponsored">
Start Free Trial
</a>

</section>

<div class="disclosure">
<strong>Affiliate Disclosure:</strong>
This page contains affiliate links. We may earn commissions at no additional cost to you.
</div>

<section class="section">

<h2>Why Marketers Choose GetResponse</h2>

<div class="grid">

<div class="card">
<h3>📧 Email Marketing</h3>
<p>Advanced newsletter campaigns and autoresponders.</p>
</div>

<div class="card">
<h3>⚡ Automation</h3>
<p>Behavior-based customer journeys and lead nurturing.</p>
</div>

<div class="card">
<h3>🎯 Funnels</h3>
<p>Build landing pages and complete conversion funnels.</p>
</div>

<div class="card">
<h3>🎥 Webinars</h3>
<p>Host live webinars without extra software.</p>
</div>

</div>

</section>

<section class="section">

<h2>Popular GetResponse Features</h2>

<table>

<tr>
<th>Feature</th>
<th>Benefit</th>
</tr>

<tr>
<td>Email Automation</td>
<td>Increase conversions with behavior triggers</td>
</tr>

<tr>
<td>Landing Pages</td>
<td>Capture leads with AI-powered pages</td>
</tr>

<tr>
<td>Webinars</td>
<td>Generate leads and sales live</td>
</tr>

<tr>
<td>Funnels</td>
<td>Automate complete customer journeys</td>
</tr>

</table>

</section>

<section class="section">

<h2>Start Growing Your Business Today</h2>

<p>
GetResponse helps affiliate marketers, ecommerce brands,
agencies and creators scale faster with automation.
</p>

<a href="{CONFIG['AFFILIATE_URL']}" class="btn" rel="nofollow sponsored">
Launch GetResponse →
</a>

</section>
"""

    html = html_template(
        title,
        description,
        content,
        CONFIG["BASE_URL"] + "/"
    )

    with open(f"{CONFIG['OUTPUT_DIR']}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

def build_blog_posts():
    sitemap_urls = []

    for niche in NICHES:
        for feature in FEATURES:

            slug = slugify(f"getresponse-for-{niche}-{feature}")

            title = f"GetResponse for {niche}: Best {feature} Platform in {CONFIG['YEAR']}"

            description = (
                f"Learn how {niche} businesses use GetResponse for "
                f"{feature.lower()} in {CONFIG['YEAR']}."
            )

            canonical = f"{CONFIG['BASE_URL']}/blog/{slug}.html"

            content = f"""
<section class="hero">

<h1>{title}</h1>

<p>
Scale your {niche.lower()} business using
GetResponse {feature.lower()} tools.
</p>

<a href="{CONFIG['AFFILIATE_URL']}" class="btn" rel="nofollow sponsored">
Try GetResponse
</a>

</section>

<section class="section">

<h2>Why {niche} Businesses Use GetResponse</h2>

<p>
GetResponse provides advanced {feature.lower()}
tools designed for modern marketers and agencies.
</p>

<div class="grid">

<div class="card">
<h3>📈 Better Conversions</h3>
<p>Automate lead nurturing and improve ROI.</p>
</div>

<div class="card">
<h3>⚡ Faster Deployment</h3>
<p>Launch campaigns and landing pages quickly.</p>
</div>

<div class="card">
<h3>🤖 AI Automation</h3>
<p>Use AI-powered workflows and optimization.</p>
</div>

</div>

</section>

<section class="section">

<h2>Best Use Cases</h2>

<ul>
<li>{niche} lead generation</li>
<li>{feature} automation</li>
<li>Sales funnel optimization</li>
<li>Email campaign scaling</li>
<li>Affiliate marketing</li>
</ul>

</section>

<section class="section">

<h2>GetResponse vs Competitors</h2>

<table>

<tr>
<th>Platform</th>
<th>Best Feature</th>
</tr>

<tr>
<td>GetResponse</td>
<td>All-in-one automation</td>
</tr>

<tr>
<td>Mailchimp</td>
<td>Basic newsletters</td>
</tr>

<tr>
<td>ConvertKit</td>
<td>Creator-focused tools</td>
</tr>

</table>

</section>

<section class="section">

<h2>Start Using GetResponse Today</h2>

<a href="{CONFIG['AFFILIATE_URL']}" class="btn" rel="nofollow sponsored">
Start Free Trial
</a>

</section>
"""

            html = html_template(
                title,
                description,
                content,
                canonical
            )

            output_path = f"{CONFIG['OUTPUT_DIR']}/blog/{slug}.html"

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html)

            sitemap_urls.append(canonical)

    return sitemap_urls

# =========================================================
# SEO FILES
# =========================================================

def build_robots():
    robots = f"""User-agent: *
Allow: /

Sitemap: {CONFIG['BASE_URL']}/sitemap.xml
"""

    with open(f"{CONFIG['OUTPUT_DIR']}/robots.txt", "w") as f:
        f.write(robots)

def build_llms():
    content = f"""# GetResponse Authority

AI-readable SEO authority layer for GetResponse.

Website:
{CONFIG['BASE_URL']}

Affiliate Link:
{CONFIG['AFFILIATE_URL']}

Topics:
- Email Marketing
- Marketing Automation
- Funnels
- Webinars
- Landing Pages
- Ecommerce
- AI Marketing
"""

    with open(f"{CONFIG['OUTPUT_DIR']}/llms.txt", "w") as f:
        f.write(content)

def build_404():
    html = html_template(
        "404 Page Not Found",
        "Page not found",
        """
<section class="hero">

<h1>404</h1>

<p>The page you requested does not exist.</p>

<a href="/" class="btn">Go Home</a>

</section>
""",
        CONFIG["BASE_URL"] + "/404.html"
    )

    with open(f"{CONFIG['OUTPUT_DIR']}/404.html", "w") as f:
        f.write(html)

def build_sitemap(blog_urls):
    today = datetime.utcnow().strftime("%Y-%m-%d")

    urls = [
        CONFIG["BASE_URL"] + "/"
    ] + blog_urls

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url in urls:
        sitemap.append(f"""
<url>
<loc>{url}</loc>
<lastmod>{today}</lastmod>
<changefreq>daily</changefreq>
<priority>0.90</priority>
</url>
""")

    sitemap.append("</urlset>")

    with open(f"{CONFIG['OUTPUT_DIR']}/sitemap.xml", "w") as f:
        f.write("\n".join(sitemap))

# =========================================================
# MAIN ENGINE
# =========================================================

def main():

    print("🚀 Starting GetResponse Authority Build")

    ensure_dirs()

    build_homepage()

    blog_urls = build_blog_posts()

    build_robots()

    build_llms()

    build_404()

    build_sitemap(blog_urls)

    total_pages = len(blog_urls) + 1

    print(f"✅ Generated {total_pages} SEO pages")
    print("✅ Sitemap generated")
    print("✅ Robots.txt generated")
    print("✅ llms.txt generated")
    print("✅ Build completed successfully")

if __name__ == "__main__":
    main()

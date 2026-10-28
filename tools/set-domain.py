#!/usr/bin/env python3
"""
Advanced SEO, AEO & GEO Automation for VIRELEO
Run with:
    python tools/set-domain.py https://vireleo.me

Features:
- Absolute Google Search Favicon priority tags (48x48 primary, 192x192, 512x512, shortcut icon)
- AEO / GEO Entity Grounding (Wikipedia / Wikidata entity definitions in knowsAbout)
- SpeakableSpecification for AI engines and voice answer queries
- Standardized Open Graph & Twitter Card metadata per page
- Rich Schema: Organization, ProfessionalService, WebSite, WebPage, BreadcrumbList, OfferCatalog, Services, ItemList
- Dynamic Google-compliant XML Sitemap with priorities and changefreq
- Explicit Googlebot & Googlebot-Favicon permissions in robots.txt
"""
import sys, re, json, datetime, pathlib

if len(sys.argv) != 2 or not re.match(r'^https://[a-z0-9.-]+\.[a-z]{2,}(:\d+)?$', sys.argv[1].rstrip('/'), re.I):
    sys.exit('Usage: python tools/set-domain.py https://vireleo.me   (must start with https://, no path)')

SITE = sys.argv[1].rstrip('/')
ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = datetime.date.today().isoformat()

PAGES = [  # file, path, schema type, breadcrumb name, priority, changefreq
    ('index.html', '/', 'WebPage', None, '1.0', 'weekly'),
    ('website-development.html', '/website-development.html', 'WebPage', 'Website Development', '0.9', 'monthly'),
    ('app-development.html', '/app-development.html', 'WebPage', 'App Development', '0.9', 'monthly'),
    ('ai-automation.html', '/ai-automation.html', 'WebPage', 'AI Automation', '0.9', 'monthly'),
    ('ai-chatbots.html', '/ai-chatbots.html', 'WebPage', 'AI Chatbots', '0.9', 'monthly'),
    ('work.html', '/work.html', 'CollectionPage', 'Work', '0.8', 'weekly'),
    ('capabilities.html', '/capabilities.html', 'CollectionPage', 'Capabilities', '0.8', 'monthly'),
    ('about.html', '/about.html', 'AboutPage', 'About', '0.7', 'monthly'),
    ('contact.html', '/contact.html', 'ContactPage', 'Contact', '0.8', 'monthly'),
]

SERVICES = [
    ('Website development', 'Custom-coded business websites, e-commerce, landing pages and web applications.', f'{SITE}/website-development.html'),
    ('Mobile app development', 'Mobile and web apps shaped around real workflows, users and outcomes.', f'{SITE}/app-development.html'),
    ('AI workflow automation', 'Connected, AI-assisted workflows that remove repetitive business tasks.', f'{SITE}/ai-automation.html'),
    ('AI chatbots and messaging automation', 'AI chatbots for websites, WhatsApp and Instagram direct messages.', f'{SITE}/ai-chatbots.html'),
]

js_path = ROOT / 'js' / 'script.js'
projects = []
if js_path.exists():
    js = js_path.read_text(encoding='utf-8')
    for m in re.finditer(r'\{\s*id:\s*"([^"]+)",\s*cat:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*desc:\s*"([^"]+)"(?:,\s*url:\s*"([^"]+)")?', js):
        projects.append(dict(id=m.group(1), title=m.group(3), desc=m.group(4), url=m.group(5)))

org_id = SITE + '/#organization'
site_id = SITE + '/#website'

org = {
    "@type": ["Organization", "ProfessionalService"],
    "@id": org_id,
    "name": "VIRELEO",
    "alternateName": "VIRELEO Studio",
    "url": SITE + '/',
    "logo": {
        "@type": "ImageObject",
        "url": SITE + '/icon-512.png',
        "width": 512,
        "height": 512,
        "caption": "VIRELEO Logo"
    },
    "image": SITE + '/images/og-image.jpg',
    "description": "Digital engineering studio providing custom website development, mobile app development, AI automation and AI chatbot solutions.",
    "email": "fitduo07@gmail.com",
    "telephone": "+92 321 5772078",
    "priceRange": "$$",
    "areaServed": {
        "@type": "Place",
        "name": "Worldwide"
    },
    "founder": {
        "@type": "Person",
        "name": "Ammar Hassan Malik",
        "jobTitle": "Founder & Lead Engineer",
        "sameAs": ["https://www.instagram.com/ammar.777_/"]
    },
    "sameAs": [
        "https://www.instagram.com/ammar.777_/"
    ],
    "contactPoint": [
        {
            "@type": "ContactPoint",
            "contactType": "sales",
            "email": "fitduo07@gmail.com",
            "telephone": "+92 321 5772078",
            "availableLanguage": ["English", "Urdu"]
        }
    ],
    "knowsAbout": [
        {"@type": "DefinedTerm", "name": "Web Development", "sameAs": "https://en.wikipedia.org/wiki/Web_development"},
        {"@type": "DefinedTerm", "name": "Artificial Intelligence", "sameAs": "https://en.wikipedia.org/wiki/Artificial_intelligence"},
        {"@type": "DefinedTerm", "name": "Chatbot", "sameAs": "https://en.wikipedia.org/wiki/Chatbot"},
        {"@type": "DefinedTerm", "name": "Business Process Automation", "sameAs": "https://en.wikipedia.org/wiki/Business_process_automation"},
        {"@type": "DefinedTerm", "name": "Mobile App Development", "sameAs": "https://en.wikipedia.org/wiki/Mobile_app_development"},
        "Custom Web Applications",
        "WhatsApp Automation",
        "Instagram Messaging Automation",
        "SaaS MVP Development",
        "Digital Engineering Studio"
    ],
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "VIRELEO Engineering Services",
        "itemListElement": [
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": name,
                    "description": desc,
                    "url": s_url
                }
            } for name, desc, s_url in SERVICES
        ]
    }
}

website = {
    "@type": "WebSite",
    "@id": site_id,
    "url": SITE + '/',
    "name": "VIRELEO",
    "alternateName": "VIRELEO Studio",
    "inLanguage": "en",
    "publisher": {"@id": org_id}
}

def build_block(file, path, ptype, crumb, title, desc):
    url = SITE + path
    graph = [org, website]
    page = {
        "@type": ptype,
        "@id": url + '#webpage',
        "url": url,
        "name": title,
        "description": desc,
        "inLanguage": "en",
        "isPartOf": {"@id": site_id},
        "about": {"@id": org_id},
        "primaryImageOfPage": {
            "@type": "ImageObject",
            "url": SITE + '/images/og-image.jpg'
        },
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": ["h1", ".hero2-lead", ".section-title", "h2"]
        }
    }
    if crumb:
        page["breadcrumb"] = {"@id": url + '#breadcrumb'}
        graph.append({
            "@type": "BreadcrumbList",
            "@id": url + '#breadcrumb',
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'},
                {"@type": "ListItem", "position": 2, "name": crumb, "item": url}
            ]
        })
    service_pages = {
        'website-development.html': ('Website development', 'Custom business websites, landing pages, portfolio sites and e-commerce experiences.'),
        'app-development.html': ('Web and mobile app development', 'Web applications, dashboards, portals, custom tools and MVPs.'),
        'ai-automation.html': ('AI workflow automation', 'AI-assisted workflows for lead routing, information processing, notifications and connected tools.'),
        'ai-chatbots.html': ('AI chatbot development', 'Website, WhatsApp and Instagram chatbot experiences for customer enquiries and lead capture.'),
    }
    if file in service_pages:
        n, d = service_pages[file]
        page['mainEntity'] = {
            '@type': 'Service',
            'name': n,
            'description': d,
            'provider': {'@id': org_id},
            'serviceType': n,
            'areaServed': 'Worldwide'
        }
    if file == 'capabilities.html':
        page["mainEntity"] = {
            "@type": "ItemList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "item": {
                        "@type": "Service",
                        "name": n,
                        "description": d,
                        "url": s_url,
                        "provider": {"@id": org_id},
                        "serviceType": n
                    }
                } for i, (n, d, s_url) in enumerate(SERVICES)
            ]
        }
    if file == 'work.html' and projects:
        page["mainEntity"] = {
            "@type": "ItemList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "item": {
                        "@type": "CreativeWork",
                        "name": p['title'],
                        "description": p['desc'],
                        "creator": {"@id": org_id},
                        **({"url": p['url']} if p['url'] else {})
                    }
                } for i, p in enumerate(projects)
            ]
        }
    graph.append(page)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)
    return (
        f'<!--seo:start-->\n'
        f'<link rel="canonical" href="{url}">\n'
        f'<meta property="og:url" content="{url}">\n'
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:image" content="{SITE}/images/og-image.jpg">\n'
        f'<meta name="twitter:title" content="{title}">\n'
        f'<meta name="twitter:description" content="{desc}">\n'
        f'<meta name="twitter:image" content="{SITE}/images/og-image.jpg">\n'
        f'<script type="application/ld+json">\n{ld}\n</script>\n'
        f'<!--seo:end-->'
    )

FAVICON_BLOCK = (
    f'<link rel="icon" type="image/png" sizes="48x48" href="{SITE}/favicon-48.png">\n'
    f'<link rel="icon" type="image/png" sizes="192x192" href="{SITE}/icon-192.png">\n'
    f'<link rel="icon" type="image/png" sizes="512x512" href="{SITE}/icon-512.png">\n'
    f'<link rel="shortcut icon" href="{SITE}/favicon.ico">\n'
    f'<link rel="icon" href="{SITE}/favicon.ico" sizes="any">\n'
    f'<link rel="apple-touch-icon" sizes="180x180" href="{SITE}/apple-touch-icon.png">\n'
    f'<link rel="manifest" href="/site.webmanifest">\n'
    f'<meta name="msapplication-TileColor" content="#0a0f1f">'
)

for file, path, ptype, crumb, priority, changefreq in PAGES:
    p = ROOT / file
    if not p.exists():
        continue
    h = p.read_text(encoding='utf-8')
    title_match = re.search(r'<title>(.*?)</title>', h, re.S)
    title = title_match.group(1).strip() if title_match else 'VIRELEO'
    desc_match = re.search(r'<meta name="description" content="(.*?)"', h)
    desc = desc_match.group(1).strip() if desc_match else ''

    # Clean legacy static Organization block if any
    h = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "Organization".*?</script>\s*', '', h, count=1, flags=re.S)

    # Standardize favicon links with absolute URLs
    h = re.sub(
        r'<link rel="(?:shortcut )?icon".*?>\s*(?:<link rel="(?:shortcut )?icon".*?>\s*)*(?:<link rel="apple-touch-icon".*?>\s*)*(?:<link rel="manifest".*?>\s*)*(?:<meta name="msapplication-TileColor".*?>\s*)?',
        FAVICON_BLOCK + '\n',
        h,
        count=1,
        flags=re.S
    )

    # Build and insert SEO block
    block = build_block(file, path, ptype, crumb, title, desc)
    if '<!--seo:start-->' in h:
        h = re.sub(r'<!--seo:start-->.*?<!--seo:end-->', lambda m: block, h, count=1, flags=re.S)
    else:
        h = h.replace('</head>', block + '\n</head>', 1)

    p.write_text(h, encoding='utf-8')
    print('updated', file)

# Generate Sitemap with proper XML namespaces, priorities, and changefreq
sitemap_urls = []
for file, path, _, _, priority, changefreq in PAGES:
    url_entry = (
        f'  <url>\n'
        f'    <loc>{SITE}{path}</loc>\n'
        f'    <lastmod>{TODAY}</lastmod>\n'
        f'    <changefreq>{changefreq}</changefreq>\n'
        f'    <priority>{priority}</priority>\n'
        f'  </url>\n'
    )
    sitemap_urls.append(url_entry)

sitemap_xml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(sitemap_urls)
    + '</urlset>\n'
)
(ROOT / 'sitemap.xml').write_text(sitemap_xml, encoding='utf-8')

# Ensure robots.txt points to correct sitemap and allows Googlebot-Favicon
r = (ROOT / 'robots.txt').read_text(encoding='utf-8')
if 'Googlebot-Favicon' not in r:
    r = re.sub(r'(User-agent: Googlebot\s*\nAllow: /)', r'\1\n\nUser-agent: Googlebot-Favicon\nAllow: /', r)
r = re.sub(r'^#?\s*Sitemap:.*$', '', r, flags=re.M).rstrip() + f'\n\nSitemap: {SITE}/sitemap.xml\n'
(ROOT / 'robots.txt').write_text(r, encoding='utf-8')

print('sitemap.xml and robots.txt successfully updated for', SITE)

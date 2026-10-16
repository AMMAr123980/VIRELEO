#!/usr/bin/env python3
"""
Run ONCE when you know the final domain (and again if the domain changes):

    python tools/set-domain.py https://vireleo.me

It writes into every page's <head> (between the <!--seo:start--> and <!--seo:end--> markers):
canonical link, og:url, og:image, twitter:image, and one JSON-LD graph (Organization with url + logo,
WebSite, WebPage/AboutPage/ContactPage/CollectionPage, BreadcrumbList, Service list on Capabilities,
project ItemList on Work). It also creates sitemap.xml and activates the Sitemap line in robots.txt.
Safe to re-run: it replaces its own block every time. Nothing else in the pages is touched.
"""
import sys, re, json, datetime, pathlib

if len(sys.argv) != 2 or not re.match(r'^https://[a-z0-9.-]+\.[a-z]{2,}(:\d+)?$', sys.argv[1].rstrip('/'), re.I):
    sys.exit('Usage: python tools/set-domain.py https://vireleo.me   (must start with https://, no path)')
SITE = sys.argv[1].rstrip('/')
ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = datetime.date.today().isoformat()

PAGES = [  # file, path, schema type, breadcrumb name
    ('index.html', '/', 'WebPage', None),
    ('work.html', '/work.html', 'CollectionPage', 'Work'),
    ('capabilities.html', '/capabilities.html', 'CollectionPage', 'Capabilities'),
    ('about.html', '/about.html', 'AboutPage', 'About'),
    ('contact.html', '/contact.html', 'ContactPage', 'Contact'),
    ('website-development.html', '/website-development.html', 'WebPage', 'Website Development'),
    ('app-development.html', '/app-development.html', 'WebPage', 'App Development'),
    ('ai-automation.html', '/ai-automation.html', 'WebPage', 'AI Automation'),
    ('ai-chatbots.html', '/ai-chatbots.html', 'WebPage', 'AI Chatbots'),
]
SERVICES = [
    ('Website development', 'Custom-coded business websites, e-commerce, landing pages and web applications.'),
    ('Mobile app development', 'Mobile and web apps shaped around real workflows, users and outcomes.'),
    ('AI workflow automation', 'Connected, AI-assisted workflows that remove repetitive business tasks.'),
    ('AI chatbots and messaging automation', 'AI chatbots for websites, WhatsApp and Instagram direct messages.'),
]

js = (ROOT / 'js' / 'script.js').read_text(encoding='utf-8')
projects = []
for m in re.finditer(r'\{\s*id:\s*"([^"]+)",\s*cat:\s*"([^"]+)",\s*title:\s*"([^"]+)",\s*desc:\s*"([^"]+)"(?:,\s*url:\s*"([^"]+)")?', js):
    projects.append(dict(id=m.group(1), title=m.group(3), desc=m.group(4), url=m.group(5)))

org_id = SITE + '/#organization'
site_id = SITE + '/#website'
org = {
    "@type": "Organization", "@id": org_id, "name": "VIRELEO", "url": SITE + '/',
    "logo": {"@type": "ImageObject", "url": SITE + '/icon-512.png', "width": 512, "height": 512},
    "image": SITE + '/images/og-image.jpg',
    "description": "Digital engineering studio providing custom website development, mobile app development, AI automation and AI chatbot solutions.",
    "email": "fitduo07@gmail.com", "telephone": "+92 321 5772078",
    "sameAs": ["https://www.instagram.com/ammar.777_/"],
    "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": "fitduo07@gmail.com",
                      "telephone": "+92 321 5772078", "availableLanguage": ["English", "Urdu"]}],
    "knowsAbout": ["Custom website development", "Mobile app development", "AI workflow automation", "AI chatbots",
                   "WhatsApp automation", "Instagram messaging automation", "Web applications", "SaaS MVP development"],
}
website = {"@type": "WebSite", "@id": site_id, "url": SITE + '/', "name": "VIRELEO", "inLanguage": "en",
           "publisher": {"@id": org_id}}

def build_block(file, path, ptype, crumb, title, desc):
    url = SITE + path
    graph = [org, website]
    page = {"@type": ptype, "@id": url + '#webpage', "url": url, "name": title, "description": desc,
            "inLanguage": "en", "isPartOf": {"@id": site_id}, "about": {"@id": org_id},
            "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + '/images/og-image.jpg'}}
    if crumb:
        page["breadcrumb"] = {"@id": url + '#breadcrumb'}
        graph.append({"@type": "BreadcrumbList", "@id": url + '#breadcrumb', "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + '/'},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]})
    service_pages = {
        'website-development.html': ('Website development', 'Custom business websites, landing pages, portfolio sites and e-commerce experiences.'),
        'app-development.html': ('Web and mobile app development', 'Web applications, dashboards, portals, custom tools and MVPs.'),
        'ai-automation.html': ('AI workflow automation', 'AI-assisted workflows for lead routing, information processing, notifications and connected tools.'),
        'ai-chatbots.html': ('AI chatbot development', 'Website, WhatsApp and Instagram chatbot experiences for customer enquiries and lead capture.'),
    }
    if file in service_pages:
        n, d = service_pages[file]
        page['mainEntity'] = {'@type': 'Service', 'name': n, 'description': d, 'provider': {'@id': org_id}, 'serviceType': n}
    if file == 'capabilities.html':
        page["mainEntity"] = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "Service", "name": n, "description": d,
             "provider": {"@id": org_id}, "serviceType": n}} for i, (n, d) in enumerate(SERVICES)]}
    if file == 'work.html' and projects:
        page["mainEntity"] = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "CreativeWork", "name": p['title'],
             "description": p['desc'], "creator": {"@id": org_id}, **({"url": p['url']} if p['url'] else {})}}
            for i, p in enumerate(projects)]}
    graph.append(page)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)
    return (f'<!--seo:start-->\n<link rel="canonical" href="{url}">\n'
            f'<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{SITE}/images/og-image.jpg">\n'
            f'<meta name="twitter:image" content="{SITE}/images/og-image.jpg">\n'
            f'<script type="application/ld+json">\n{ld}\n</script>\n<!--seo:end-->')

for file, path, ptype, crumb in PAGES:
    p = ROOT / file
    h = p.read_text(encoding='utf-8')
    title = re.search(r'<title>(.*?)</title>', h, re.S).group(1).strip()
    desc = re.search(r'<meta name="description" content="(.*?)"', h).group(1)
    # the static, domain-free Organization block is replaced by the full graph
    h = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "Organization".*?</script>\s*', '', h, count=1, flags=re.S)
    block = build_block(file, path, ptype, crumb, title, desc)
    if '<!--seo:start-->' in h:
        h = re.sub(r'<!--seo:start-->.*?<!--seo:end-->', lambda m: block, h, count=1, flags=re.S)
    else:
        h = h.replace('</head>', block + '\n</head>', 1)
    p.write_text(h, encoding='utf-8')
    print('updated', file)

urls = ''.join(f'  <url><loc>{SITE}{path}</loc><lastmod>{TODAY}</lastmod></url>\n' for _, path, _, _ in PAGES)
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n', encoding='utf-8')
r = (ROOT / 'robots.txt').read_text(encoding='utf-8')
r = re.sub(r'^#?\s*Sitemap:.*$', '', r, flags=re.M).rstrip() + f'\n\nSitemap: {SITE}/sitemap.xml\n'
(ROOT / 'robots.txt').write_text(r, encoding='utf-8')
print('sitemap.xml + robots.txt written for', SITE)

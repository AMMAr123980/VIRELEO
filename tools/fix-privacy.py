"""Fix cookie banner text and add Privacy Policy link to all page footers."""
from pathlib import Path

ROOT = Path(__file__).parent.parent

PAGES = [
    'index.html','about.html','contact.html','work.html','capabilities.html',
    'website-development.html','app-development.html','ai-automation.html','ai-chatbots.html',
    'blog.html','blog-cost-to-build-saas-mvp.html','blog-custom-code-vs-wordpress.html',
    'blog-whatsapp-instagram-ai-chatbot-guide.html','blog-ai-workflow-automation-guide.html'
]

COOKIE_OLD = 'We use cookies and analytics to improve your experience and measure site performance. <a href="#" style="color:#1fc6d6;text-decoration:underline">Learn more</a>.'
COOKIE_NEW = 'We use cookies for analytics and personalised ads (Google AdSense). <a href="privacy-policy.html" style="color:#1fc6d6;text-decoration:underline">Privacy Policy</a>'

FOOTER_OLD = '<p>Custom-coded. Built to be owned.</p></div>'
FOOTER_NEW = '<p><a href="privacy-policy.html" style="color:inherit;opacity:.7;">Privacy Policy</a>&nbsp;&nbsp;·&nbsp;&nbsp;Custom-coded. Built to be owned.</p></div>'

for f in PAGES:
    p = ROOT / f
    if not p.exists():
        print(f'skip {f}')
        continue
    h = p.read_text(encoding='utf-8')
    changed = False
    if COOKIE_OLD in h:
        h = h.replace(COOKIE_OLD, COOKIE_NEW)
        changed = True
    if FOOTER_OLD in h:
        h = h.replace(FOOTER_OLD, FOOTER_NEW)
        changed = True
    if changed:
        p.write_text(h, encoding='utf-8')
        print(f'updated {f}')
    else:
        print(f'no change needed: {f}')

print('Done.')

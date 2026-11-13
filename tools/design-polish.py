"""
VIRELEO Design Polish Script
Improves typography, spacing, and visual polish across the website.
Run: python tools/design-polish.py
"""
import os
import re

WEBSITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── 1. IMPROVE GOOGLE FONTS IMPORT ─────────────────────────────────────────
# Add Sora + better weight range for Plus Jakarta Sans
OLD_FONT_IMPORT = 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap'
NEW_FONT_IMPORT = 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Sora:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap'

# ── 2. CSS DESIGN POLISH BLOCK ─────────────────────────────────────────────
POLISH_CSS = '''

/* ==========================================================================
   VIRELEO — Design Polish Pass (Nov 2026)
   Better typography, spacing, card refinement, and visual clarity.
   These are intentional overrides for a more polished editorial feel.
   ========================================================================== */

/* --- Font updates: load Sora properly ------------------------------------ */
:root {
  --font-head:  "Plus Jakarta Sans", "Sora", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-serif: "Sora", "Plus Jakarta Sans", sans-serif;
  --font-body:  "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* --- Body: warmer, more readable text color (not pure black) ------------- */
body {
  color: #0d1626;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}
p, li, td, th { color: inherit; }

/* --- Headings: tighter, more editorial ----------------------------------- */
h1, h2, h3, h4 {
  font-family: var(--font-head);
  font-feature-settings: "kern" 1, "liga" 1, "calt" 1;
}

/* --- Section typography hierarchy ---------------------------------------- */
.section-title {
  font-size: clamp(1.9rem, 3.6vw, 2.85rem);
  font-weight: 700;
  letter-spacing: -0.038em;
  line-height: 1.12;
}
.section-sub {
  font-size: 1.08rem;
  line-height: 1.72;
  color: #546080;
  margin-top: 14px;
  max-width: 56ch;
}
.label {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
}

/* --- Hero2: more editorial headline -------------------------------------- */
.hero2-copy h1 {
  font-weight: 800;
  letter-spacing: -0.032em;
}
.hero2-lead {
  color: #475569;
  letter-spacing: 0;
  line-height: 1.72;
}
/* Gradient word: use brand colours exactly */
.hero2 h1 .w.grad .wi {
  background: linear-gradient(105deg, #1a90f8 0%, #6d4df2 55%, #1fa5d6 100%);
  background-size: 220% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
}

/* --- Intro section: replace inline-styled pills with proper classes ------- */
.intro-pill {
  background: #fff;
  border: 1px solid rgba(16, 28, 54, .09);
  border-radius: 14px;
  padding: 20px 22px;
  box-shadow: 0 4px 18px -6px rgba(16, 28, 54, .07);
  transition: transform .28s ease, box-shadow .28s ease, border-color .28s;
}
.intro-pill:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 28px -10px rgba(16, 28, 54, .12);
  border-color: rgba(106, 61, 240, .22);
}
.intro-pill-label {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .07em;
  text-transform: uppercase;
  margin: 0 0 7px;
}
.intro-pill-label--cyan  { color: #0e9094; }
.intro-pill-label--blue  { color: #2b5cdb; }
.intro-pill-label--violet{ color: #6a2cc9; }
.intro-pill-text {
  margin: 0;
  font-size: .92rem;
  line-height: 1.6;
  color: #2a364f;
}
.intro h2 {
  font-size: clamp(2rem, 3.8vw, 3rem);
  font-weight: 700;
  letter-spacing: -.04em;
  line-height: 1.12;
}
.intro-text p {
  font-size: 1.04rem;
  line-height: 1.72;
  color: #546080;
}

/* --- "Tension" dark section: larger, bolder ------------------------------- */
.tension h2 {
  font-size: clamp(2.1rem, 4.4vw, 3.6rem);
  font-weight: 700;
  letter-spacing: -0.045em;
  line-height: 1.1;
}
.scrub {
  font-size: clamp(1.2rem, 2vw, 1.72rem);
  line-height: 1.55;
  color: rgba(255, 255, 255, .78);
}
.scrub.on { color: #fff; }

/* --- Process steps: more refined ----------------------------------------- */
.steps h3 {
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -.025em;
  color: #0d1626;
}
.steps p {
  font-size: .97rem;
  line-height: 1.7;
  color: #546080;
  margin-top: 10px;
}

/* --- Service cards: sharper heading -------------------------------------- */
.service h3 {
  font-size: 1.3rem;
  font-weight: 700;
  letter-spacing: -.02em;
  color: #0d1626;
}
.service > p {
  font-size: .95rem;
  line-height: 1.65;
  color: #546080;
}
.service li {
  font-size: .95rem;
  color: #3d4a63;
  line-height: 1.6;
}

/* --- Work cards: cleaner typography -------------------------------------- */
.card h3 {
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -.02em;
  color: #0d1626;
  line-height: 1.25;
}
.card p {
  font-size: .93rem;
  line-height: 1.65;
  color: #546080;
}
.card-foot { color: #667399; }

/* --- CTA section: bigger punchline --------------------------------------- */
.cta h2 {
  font-size: clamp(2.1rem, 4.5vw, 3.5rem);
  font-weight: 700;
  letter-spacing: -.045em;
  line-height: 1.1;
}
.cta p {
  font-size: 1.1rem;
  line-height: 1.65;
  color: rgba(255, 255, 255, .78);
  max-width: 46ch;
  margin: 18px auto 0;
}

/* --- Blog cards: more visual weight on homepage preview ------------------ */
.blog-preview-section .blog-card {
  border-radius: 22px;
  border: 1px solid rgba(16, 28, 54, .09);
  box-shadow: 0 12px 36px -18px rgba(18, 32, 62, .10);
  transition: transform .3s ease, box-shadow .35s ease, border-color .3s;
}
.blog-preview-section .blog-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 56px -20px rgba(18, 32, 62, .18);
  border-color: rgba(91, 69, 240, .28);
}
.blog-card-body {
  padding: 32px 32px 36px;
}
.blog-card h3 {
  font-size: clamp(1.18rem, 1.9vw, 1.45rem);
  font-weight: 700;
  letter-spacing: -.025em;
  line-height: 1.3;
  color: #101828;
  margin-bottom: 10px;
}
.blog-card p {
  font-size: .97rem;
  line-height: 1.68;
  color: #546080;
}
.blog-card-link {
  font-weight: 700;
  font-size: .88rem;
  color: #3b4de6;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  margin-top: 4px;
}
.blog-badge {
  font-weight: 700;
  letter-spacing: .06em;
  font-size: .68rem;
  padding: 5px 11px;
}
.blog-read-time {
  font-size: .78rem;
  color: #7a849d;
}

/* --- Capabilities dark section: sharper copy ----------------------------- */
.caps-stage h2 {
  font-size: clamp(2rem, 4vw, 3.1rem);
  font-weight: 700;
  letter-spacing: -.04em;
  line-height: 1.12;
}
.caps-stage p {
  font-size: 1.08rem;
  line-height: 1.68;
  color: rgba(255, 255, 255, .78);
  max-width: 50ch;
}

/* --- Commitment grid: refined text --------------------------------------- */
.cm p {
  font-size: .97rem;
  line-height: 1.65;
  color: rgba(255, 255, 255, .82);
}

/* --- Footer: typography cleanup ------------------------------------------ */
.footer-brand p {
  font-size: .93rem;
  line-height: 1.68;
  color: rgba(255, 255, 255, .56);
}
.footer-col a {
  font-size: .93rem;
  line-height: 1.6;
}
.footer-base {
  font-size: .84rem;
}

/* --- FAQ section: readable and editorial ---------------------------------- */
.faq-section .faq-item h3 {
  font-size: 1.1rem;
  font-weight: 650;
  letter-spacing: -.01em;
  line-height: 1.4;
}
.faq-section .faq-item p,
.faq-section .faq-item [itemprop="text"] {
  font-size: .97rem;
  line-height: 1.72;
  color: #3e4c66;
}
.faq-section h2 {
  font-weight: 700;
  letter-spacing: -.04em;
}

/* --- Contact form: refined inputs ---------------------------------------- */
.field label {
  font-size: .88rem;
  font-weight: 600;
  color: #0d1626;
  letter-spacing: .01em;
}
.field input,
.field select,
.field textarea {
  font-size: .97rem;
  line-height: 1.5;
  color: #0d1626;
}
.field input::placeholder,
.field textarea::placeholder {
  color: #9aa7c0;
}
.form-card {
  box-shadow: 0 24px 60px -36px rgba(16, 28, 54, .28);
}

/* --- Banner pages: sharper headings -------------------------------------- */
.banner h1 {
  font-weight: 700;
  letter-spacing: -.04em;
  line-height: 1.08;
}
.banner p.lead {
  font-size: 1.1rem;
  line-height: 1.68;
  color: rgba(255, 255, 255, .82);
}

/* --- Buttons: micro-polish ----------------------------------------------- */
.btn {
  font-weight: 650;
  letter-spacing: .01em;
}
.btn-blue {
  background: linear-gradient(105deg, #1fc6d6 0%, #477bff 52%, #8b45f5 100%);
  box-shadow: 0 12px 28px -12px rgba(71, 123, 255, .75);
}
.btn-blue:hover {
  box-shadow: 0 18px 36px -12px rgba(71, 123, 255, .9);
}

/* --- Progress bar: crisp ------------------------------------------------- */
.progress {
  height: 3px;
  background: linear-gradient(90deg, #1fc6d6, #477bff, #8b45f5);
}

/* --- Wordmark: Sora-based footer logo ------------------------------------ */
.wordmark {
  font-family: "Sora", "Plus Jakarta Sans", sans-serif !important;
}

/* --- Caps rail button: cleaner label ------------------------------------- */
.caps-rail button span {
  font-size: .9rem;
  font-weight: 500;
  letter-spacing: .01em;
}

/* --- Article content (blog posts): editorial readability ----------------- */
.article-content {
  font-size: 1.08rem;
  line-height: 1.82;
  color: #1e2b40;
  font-feature-settings: "kern" 1, "liga" 1;
}
.article-content h2 {
  font-weight: 700;
  letter-spacing: -.03em;
}
.article-content h3 {
  font-weight: 700;
  letter-spacing: -.025em;
}
.article-content strong {
  color: #0d1626;
  font-weight: 650;
}
.article-header h1 {
  font-weight: 700;
  letter-spacing: -.038em;
}

/* --- Mobile tweaks: bigger tap targets, readable text -------------------- */
@media (max-width: 700px) {
  .section-title { font-size: clamp(1.75rem, 7.2vw, 2.4rem); }
  .blog-card-body { padding: 24px 22px 28px; }
  .article-content { font-size: 1.03rem; line-height: 1.78; }
  .scrub { font-size: 1.15rem; }
  .cta h2 { font-size: clamp(1.9rem, 7vw, 2.6rem); }
  .intro h2 { font-size: clamp(1.9rem, 7.5vw, 2.5rem); }
}

/* --- Reduced motion: keep everything accessible -------------------------- */
@media (prefers-reduced-motion: reduce) {
  .intro-pill { transition: none; }
}
/* END design-polish */
'''

def fix_font_import_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if OLD_FONT_IMPORT in content:
        content = content.replace(OLD_FONT_IMPORT, NEW_FONT_IMPORT)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def add_polish_to_css(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove any previous polish block if it exists
    marker = '/* ==========================================================================\n   VIRELEO — Design Polish Pass'
    if marker in content:
        # Find the start index
        idx = content.find(marker)
        # Find the end marker
        end_marker = '/* END design-polish */'
        end_idx = content.find(end_marker)
        if end_idx != -1:
            content = content[:idx] + content[end_idx + len(end_marker):]
        else:
            content = content[:idx]
        content = content.rstrip()
    # Append new polish block
    content += '\n' + POLISH_CSS
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✅ Design polish CSS added to {css_path}')

def fix_intro_pills(html_path):
    """Replace inline-styled intro pills with proper CSS classes"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the intro-pills-grid pattern and replace inline styles
    old_pill_grid = '''<div class="intro-pills-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:24px 0 28px;">
          <div style="background:#ffffff;border:1px solid rgba(16,28,54,0.1);border-radius:12px;padding:18px 20px;box-shadow:0 4px 16px -6px rgba(16,28,54,0.06);">
            <p class="mono" style="font-size:0.75rem;font-weight:700;color:#0e8a94;margin:0 0 6px 0;letter-spacing:0.06em;text-transform:uppercase;">01 · For Startups &amp; Scaleups</p>
            <p style="margin:0;font-size:0.9rem;line-height:1.55;color:#2a364f;">Custom web applications, SaaS MVPs, and founder prototypes built with full IP ownership.</p>
          </div>
          <div style="background:#ffffff;border:1px solid rgba(16,28,54,0.1);border-radius:12px;padding:18px 20px;box-shadow:0 4px 16px -6px rgba(16,28,54,0.06);">
            <p class="mono" style="font-size:0.75rem;font-weight:700;color:#2b5cdb;margin:0 0 6px 0;letter-spacing:0.06em;text-transform:uppercase;">02 · What We Engineer</p>
            <p style="margin:0;font-size:0.9rem;line-height:1.55;color:#2a364f;">Handcrafted business websites, mobile apps, and autonomous WhatsApp &amp; Instagram AI bots.</p>
          </div>
          <div style="background:#ffffff;border:1px solid rgba(16,28,54,0.1);border-radius:12px;padding:18px 20px;box-shadow:0 4px 16px -6px rgba(16,28,54,0.06);">
            <p class="mono" style="font-size:0.75rem;font-weight:700;color:#6a2cc9;margin:0 0 6px 0;letter-spacing:0.06em;text-transform:uppercase;">03 · How We Deliver</p>
            <p style="margin:0;font-size:0.9rem;line-height:1.55;color:#2a364f;">Fixed-scope 3 to 6 week delivery with weekly milestone demos and clean architecture handover.</p>
          </div>
        </div>'''

    new_pill_grid = '''<div class="intro-pills-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:24px 0 28px;">
          <div class="intro-pill">
            <p class="mono intro-pill-label intro-pill-label--cyan">01 · For Startups &amp; Scaleups</p>
            <p class="intro-pill-text">Custom web applications, SaaS MVPs, and founder prototypes built with full IP ownership.</p>
          </div>
          <div class="intro-pill">
            <p class="mono intro-pill-label intro-pill-label--blue">02 · What We Engineer</p>
            <p class="intro-pill-text">Handcrafted business websites, mobile apps, and autonomous WhatsApp &amp; Instagram AI bots.</p>
          </div>
          <div class="intro-pill">
            <p class="mono intro-pill-label intro-pill-label--violet">03 · How We Deliver</p>
            <p class="intro-pill-text">Fixed-scope 3 to 6 week delivery with weekly milestone demos and clean architecture handover.</p>
          </div>
        </div>'''

    if old_pill_grid in content:
        content = content.replace(old_pill_grid, new_pill_grid)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ Intro pills refactored in {os.path.basename(html_path)}')
        return True
    else:
        print(f'ℹ️  Intro pills pattern not found in {os.path.basename(html_path)} (may already be updated)')
        return False

def run():
    # Step 1: Add polish CSS to style.css
    css_path = os.path.join(WEBSITE_DIR, 'css', 'style.css')
    add_polish_to_css(css_path)

    # Step 2: Fix Google Fonts import in all HTML files
    html_files = [f for f in os.listdir(WEBSITE_DIR) if f.endswith('.html')]
    font_fixed = 0
    for html_file in html_files:
        path = os.path.join(WEBSITE_DIR, html_file)
        if fix_font_import_in_file(path):
            font_fixed += 1
            print(f'✅ Font import updated: {html_file}')
    print(f'  → {font_fixed}/{len(html_files)} HTML files had font import updated')

    # Step 3: Fix intro pills in index.html
    index_path = os.path.join(WEBSITE_DIR, 'index.html')
    fix_intro_pills(index_path)

    print('\n🎨 Design polish complete!')

if __name__ == '__main__':
    run()

# VIRELEO — Digital Engineering Studio (3-page website)

Plain HTML, CSS and JavaScript. No build step, no frameworks.

## Pages
- `index.html`   home (hero, about, services, capabilities, selected work, process)
- `work.html`    all projects with category filters (`work.html?cat=web` opens a category)
- `contact.html` enquiry form that opens WhatsApp with the message ready to send

## Run locally
    cd VIRELEO-Website
    python -m http.server 5500      # then open http://localhost:5500
(or just double-click index.html)

## The two places you will edit
Both are at the top of `js/script.js`.

1. `CONFIG`: brand name, WhatsApp number, email. Changing `brand: "VIRELEO"` updates the name on every page.
2. `PROJECTS`: one entry per project. Add `url` for a live link; leave it out and the
   Details button opens WhatsApp with the project name instead.

## Your own pictures (optional)
The site ships with no photos. Everything is CSS.
- Hero photo: save a wide image as `images/hero.jpg`. It is used automatically behind the hero and page banners.
- Project screenshots: save as `images/projects/<id>.jpg` (ids are listed in `PROJECTS`, e.g. `portfolio.jpg`,
  `mailnexa.jpg`). If a file is missing, the built-in mockup is shown.

## Colors and fonts
Design tokens are at the top of `css/style.css` (`:root`).

## Deploy
Drag the folder onto https://app.netlify.com/drop, or import the GitHub repo in Vercel (framework: Other).

## Animations
All motion lives in the last section of `css/style.css` (marked MOTION) and in `js/script.js`.
- Navy page curtain with the logo on load and between pages
- Hero: slow background zoom, drifting light, parallax on scroll, light that follows the mouse (desktop)
- Headlines reveal word by word; sections, cards and steps fade up in sequence on scroll
- Project thumbnails wipe open; footer wordmark letters rise; the process blueprint draws itself
- Featured-work card and Capabilities slider autoplay with a progress line (pause on hover)
- Work tabs fill a progress line; cards re-animate when you switch category or filter
- Buttons sweep color on hover, cards lift, arrows move, live mockups loop (chat bubbles, flow lines, weather)
- Header hides while scrolling down and returns when scrolling up; scroll progress bar at the top
- Pulsing WhatsApp button

Visitors who set "reduce motion" in their system get the same site with the animation turned off.
To slow things down or speed them up, change the durations in the MOTION section.

## Theme v4 (colors and animations inspired by the reference video)
Colors: ink `#0a0f1f`, violet `#6a3df0` to cyan `#1fc6d6` gradient, lavender light sections, teal glow on dark sections
(tokens at the top of the "THEME v4" block in `css/style.css`).
New motion (CSS in THEME v4, JS in "MOTION v4" at the bottom of `js/script.js`):
- Floating dark pill navbar with active pill, and a Services mega menu that blurs/fades in with staggered links
- Hero: aurora blobs, drifting network of dots (reacts to the mouse), gradient headline word, glass stats card with count-up numbers and a self-drawing sparkline
- Dark page banners: moving grid, typewriter headline with blinking caret
- "The problem" section: sticky headline, words sharpen as you scroll
- Pinned story: stage expands on scroll, lines change one by one, phones and notification chips float
- Process: stepper and timeline fill with the gradient as you scroll, outlined step numbers
- Commitments cards with drawing check marks and pointer spotlight; magnetic gradient buttons; blur-in reveals
- Footer: dark gradient, ghost wordmark fading out, letters rising

## Instagram (temporary)
`CONFIG.instagram` at the top of `js/script.js` is set to `ammar.777_`. It shows in the footer (button + contact column)
and on the Contact page. Change the handle there, or set it to `""` to remove Instagram everywhere.


## SEO launch
Read `SEO-LAUNCH.md` before publishing. The canonical URL and sitemap are intentionally templates until the final domain is chosen; do not deploy the placeholder URLs as live SEO signals.


## SEO, AEO & GEO launch
See `SEO-LAUNCH.md` for domain setup, canonical URLs, sitemap, robots.txt, Search Console, and AI crawler guidance. The domain is not set in this package; replace placeholders only after choosing the final domain.


## Dedicated pages
- `capabilities.html` — service capabilities detail page.
- `about.html` — agency approach and about page.

The shared navigation links Capabilities and About to these dedicated pages. The footer wordmark and homepage hero sizing are refined in `css/style.css`.

## v19 changes
- Every "Start a project" / "Start your project" button now uses the same gradient pill (`btn btn-blue`):
  color sweep on hover, magnetic pull toward the pointer, small press effect on click. The home page
  "Let's build something remarkable" button and the About page button were changed to match.
- "What you can count on" icons are now rounded gradient-outline tiles (same language as the logo mark).
  The strokes draw in when the card appears, and the tile fills with the brand gradient on hover.
  The Contact page icons use the same tile shape in a light version.
- Click-to-page time measured at about 1 second (limit: 1.5 s).


## v20 responsive update
- Added final responsive overrides for desktop, laptop, tablet, mobile, small phones, and short landscape screens.
- Adjusted hero typography/layout, cards, navigation, forms, grids, and footer to reduce clipping and horizontal overflow.
- Existing colors, content, pages, and interactions are retained.

## v58 changes
- Work, Capabilities, About and Contact: the pictures in the top banner were removed.
- The left side is now a typographic block: crumb pill, kicker with accent line, heading with gradient-highlighted
  words (still typed out letter by letter), lead text, and a glowing vertical accent line.
- The right side carries one large outlined word per page (Work / Build / About / Talk) instead of an image.
  Change the words in each page's `<span class="banner-ghost">`; change the highlighted heading words with the
  `data-hl="..."` attribute on the `<h1>`.


## SEO / AEO / GEO update (v67)
Four service-specific landing pages have been added: `website-development.html`, `app-development.html`, `ai-automation.html`, and `ai-chatbots.html`. The `tools/set-domain.py` script generates canonical URLs, structured data and a sitemap for all nine indexable pages. The intended domain `vireleo.me` is provisional until purchased and connected to Vercel; read `SEO-LAUNCH.md` before deploying.


## Traffic and performance (v68)
- Static caching and security headers are configured in `vercel.json` (and mirrored in `_headers` for compatible hosts).
- Removed two third-party screenshot service dependencies from homepage cards.
- `PERFORMANCE-AND-SCALING.md` explains deployment, monitoring and limitations.
- `tests/load-test.js` is an optional k6 starter test; run it only against your own deployed site.

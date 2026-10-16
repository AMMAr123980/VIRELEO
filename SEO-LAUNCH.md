# VIRELEO SEO + AEO + GEO launch guide

## Domain status: provisional
The intended domain is **https://vireleo.me**, but it has not yet been purchased/verified. Do not publish this package with canonical URLs pointing to that domain until you own it and have connected it to Vercel. Once the domain is active, run from the website folder:

```bash
python tools/set-domain.py https://vireleo.me
```

The command writes canonical URLs, Open Graph/Twitter URLs, JSON-LD graphs and `sitemap.xml`, and adds the sitemap line to `robots.txt`. If you choose `www.vireleo.me` as the primary host instead, use that exact HTTPS URL consistently and configure Vercel redirects for the other host.

## Improvements included in this package
- Four dedicated service landing pages for website development, app development, AI automation and AI chatbot development.
- Unique titles and meta descriptions for each service page.
- Visible FAQs with matching FAQPage structured data on each service page.
- Internal navigation links to the service landing pages, improving discovery and topical relevance.
- Domain setup script extended to include all nine indexable pages in canonical metadata and sitemap generation.
- `llms.txt` updated with direct links and summaries for the service pages.
- Existing visual design, responsive styling, motion and contact pathways are retained.

## Before deployment
1. Buy/verify `vireleo.me`, add it in Vercel Project → Settings → Domains, and complete the DNS records Vercel shows you.
2. Run the domain setup command above from the `VIRELEO-Website` directory.
3. Confirm the generated `sitemap.xml` lists all nine pages and that each page has one correct canonical URL.
4. Deploy to Vercel and check `/robots.txt`, `/sitemap.xml`, `/llms.txt`, all service pages, CSS, JavaScript and images.
5. Pick one primary host (`https://vireleo.me` or `https://www.vireleo.me`) and configure redirects to it. Do not split canonical signals between both.
6. Verify the domain in Google Search Console and Bing Webmaster Tools; submit `/sitemap.xml` and request indexing for the main and service pages.
7. Validate JSON-LD and page experience with the relevant search-engine testing tools.

## SEO, AEO and GEO notes
- AEO: the pages provide direct answers to common service questions and structured FAQ data. Search engines decide whether any enhanced presentation is eligible; FAQ markup does not guarantee a rich result.
- GEO: `llms.txt` provides an additional readable site summary, but is not a substitute for crawlable HTML, credible sources, mentions and strong content.
- SEO: rankings depend on competition, intent match, content quality, site performance, indexing and authority. No technical package can guarantee a top position.
- Worldwide targeting: use clear English, consistent contact information, useful case studies and service-specific content. Avoid creating thin near-duplicate location pages.
- Add real case studies with verified outcomes and client testimonials only where permission exists. Never publish invented metrics or fake reviews.

## Search guidance
Google's documentation for AI features in Search: https://developers.google.com/search/docs/appearance/ai-features

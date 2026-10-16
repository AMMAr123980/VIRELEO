# VIRELEO — Performance, traffic spikes & scaling

## Current architecture

This is a static HTML/CSS/JavaScript site. It has no application server or database in the page-serving path. On Vercel, static assets are delivered through its network, so concurrent page visits generally do not create one server-side render or database query per visitor. This is a good starting point for traffic spikes, but not a promise of zero downtime or unlimited traffic.

## Improvements in this package

- Added cache policies for CSS/JS, images, video and HTML in `vercel.json`; mirrored equivalent rules in `_headers` for compatible static hosts.
- Added common security headers, including `Permissions-Policy`.
- Removed two external WordPress mShots preview requests from the homepage. Built-in CSS mockups remain, so those cards no longer depend on that third-party screenshot service.
- Added `tests/load-test.js`, a k6 starter test for the home page, service pages, CSS, JS, robots and sitemap.

## Before launch

1. Buy and connect `vireleo.me` to Vercel; make sure HTTPS works.
2. Deploy as a static site (Vercel framework preset: Other; no build command; output/root directory is the folder containing `index.html`).
3. Confirm production domain and redirects (choose either apex `vireleo.me` or `www.vireleo.me` as canonical, not both).
4. Run a browser performance audit and check mobile Core Web Vitals. The intro video already uses `preload="none"`; keep it from downloading until requested.
5. Install k6 and run a gradual load test against your own deployed site: `k6 run -e BASE_URL=https://vireleo.me tests/load-test.js`.
6. Review Vercel project usage, bandwidth and plan limits in the dashboard. Upgrade or contact Vercel if expected traffic or bandwidth approaches the plan's limits.
7. Monitor availability and performance after launch. A spike test samples a workload; it cannot prove every possible traffic level.

## Important limits

- This test is a starting point; thresholds are targets, not a guarantee. Increase traffic gradually and only test your own site.
- It does not test contact conversion, WhatsApp delivery, third-party services or a backend API.
- If a contact form, chatbot, login, API or database is later added, those dynamic services need their own rate limits, timeouts, monitoring and capacity tests. Never put secrets in frontend files.
- Large traffic can still be affected by account/plan limits, bandwidth, DNS, browser performance or a provider-wide outage.

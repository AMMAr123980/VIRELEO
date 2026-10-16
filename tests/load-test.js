// VIRELEO static-site smoke/load test (k6).
// Run only against your own deployed site: k6 run -e BASE_URL=https://vireleo.me tests/load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';
const failures = new Rate('http_failures');
const base = (__ENV.BASE_URL || 'https://vireleo.me').replace(/\/$/, '');
export const options = {
  stages: [ { duration: '30s', target: 10 }, { duration: '1m', target: 25 }, { duration: '1m', target: 50 }, { duration: '30s', target: 0 } ],
  thresholds: { http_req_failed: ['rate<0.01'], http_req_duration: ['p(95)<1500'] },
};
const paths = ['/', '/website-development.html', '/app-development.html', '/ai-automation.html', '/ai-chatbots.html', '/css/style.css', '/js/script.js', '/robots.txt', '/sitemap.xml'];
export default function () {
  const path = paths[Math.floor(Math.random() * paths.length)];
  const res = http.get(`${base}${path}`, { tags: { path } });
  const ok = check(res, { 'HTTP status is 200': r => r.status === 200 });
  failures.add(!ok);
  sleep(0.3);
}

/* ==========================================================================
   VIRELEO — settings, projects and behaviour
   1) Edit CONFIG for name and contact details.
   2) Edit PROJECTS to add, remove or change projects on every page.
   ========================================================================== */
const CONFIG = {
  brand: "VIRELEO",                      // change when the final name is ready
  whatsappNumber: "923215772078",    // digits only, country code first, no + or spaces
  whatsappDisplay: "+92 321 5772078",
  email: "fitduo07@gmail.com",
  instagram: "vireleo.me",           // Official VIRELEO Instagram handle
  linkedin: "https://www.linkedin.com/in/vireleo-806625322/", // Official VIRELEO LinkedIn profile
  defaultMessage: "Hi, I found your website and would like to talk about a project."
};

const CATS = {
  web:        { name: "Website development",    short: "Web" },
  app:        { name: "App Development",        short: "Apps" },
  automation: { name: "AI Automation",          short: "AI Automation" },
  chatbot:    { name: "AI Chatbot Development", short: "AI Chatbots" }
};

/* url: live link (opens in a new tab). Leave url out and the Details button opens WhatsApp instead.
   shot: optional screenshot, e.g. "images/projects/portfolio.jpg". If the file is missing, the
   built-in mockup shows instead. */
const PROJECTS = [
  { id: "appliory", cat: "web", title: "Appliory",
    desc: "A web platform providing free document checking, PDF management and image processing tools directly in the browser.",
    url: "https://appliory.tech/", shot: "images/projects/appliory.jpg" },
  { id: "portfolio", cat: "web", title: "Ammar Portfolio",
    desc: "A responsive personal portfolio presenting skills, projects and contact details in a clean, fast layout.",
    url: "https://ammar-portfolio-web.netlify.app/", shot: "images/projects/ammar-portfolio.jpg" },
  { id: "lean-canvas", cat: "web", title: "Lean Canvas Model",
    desc: "A web tool for laying out a business idea on the Lean Canvas: problem, solution, customers, revenue and more.",
    url: "https://lean-canvas-model.netlify.app/", shot: "images/projects/lean-canvas-model.jpg" },
  { id: "whatsapp-dm", cat: "chatbot", title: "WhatsApp DM Automation",
    desc: "Automated replies, lead capture and booking flows that run inside your WhatsApp conversations.",
    shot: "images/projects/whatsapp-dm-wide.jpg" },
  { id: "instagram-dm", cat: "chatbot", title: "Instagram DM Automation",
    desc: "Instant, consistent answers to Instagram direct messages, so new enquiries are never left waiting.",
    shot: "images/projects/instagram-dm-wide.jpg" },
  { id: "iot-weather", cat: "app", title: "IoT Weather and Hailstorm Protection System",
    desc: "A mobile app connected to IoT sensors that tracks local weather and warns of incoming hailstorms so crops and property can be protected in time.",
    shot: "images/projects/iot-weather.jpg" },
  { id: "ai-employee-os", cat: "automation", title: "AI Employee OS",
    desc: "An AI-powered workspace that takes on routine business tasks, like an extra member of the team.",
    url: "https://ai-employee-os-lhqy.vercel.app/", shot: "images/projects/ai-employee-os.jpg" },
  { id: "mailnexa", cat: "automation", title: "MailNexa AI",
    desc: "An email intelligence system that sorts incoming mail, summarizes it and helps you respond faster.",
    url: "https://email-intelligence-system-seven.vercel.app/select-portal", shot: "images/projects/mailnexa-ai.jpg" }
];

const CAPABILITIES = [
  { k: "Custom code", tags: ["Hand-written", "No page builders", "Built for you"], t: "Custom code, not templates", d: "Every site and system is engineered for the business it serves, not exported from a builder." },
  { k: "Your workflow", tags: ["Discovery first", "Smallest useful build", "Clear scope"], t: "Built around your workflow", d: "We start from how your team and customers work today, then build the smallest thing that fixes it." },
  { k: "Fast & accessible", tags: ["Quick to load", "Every screen size", "Accessible"], t: "Fast, responsive, accessible", d: "Pages load quickly, adapt to every screen and work for everyone who visits." },
  { k: "Scalable build", tags: ["Clean structure", "Integrations", "Room to grow"], t: "Scalable, connected architecture", d: "Clean structure and sensible integrations, so what we build can grow with you." },
  { k: "Clean handover", tags: ["Readable code", "Documentation", "No lock-in"], t: "Clean code, clear handover", d: "Readable, documented code and a proper handover, so you are never locked in." }
];

const ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12 12 4M5.5 4H12v6.5"/></svg>';

(function () {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const waLink = (t) => "https://wa.me/" + CONFIG.whatsappNumber + "?text=" + encodeURIComponent(t);
  const projectLink = (p) => p.url || waLink("Hi, I'd like to know more about the " + p.title + " project.");
  const status = (p) => (p.url ? "Live" : "On request");
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const PIN = !reduce && window.matchMedia("(min-width: 861px) and (min-height: 480px)").matches;
  if (PIN) document.documentElement.classList.add("pin");
  if (PIN) document.documentElement.classList.add("pinw");
  const EASE = "cubic-bezier(.2,.7,.2,1)";

  /* Apply CONFIG ------------------------------------------------------- */
  $$("[data-brand]").forEach((el) => (el.textContent = CONFIG.brand));
  $$("[data-wa]").forEach((a) => { a.href = waLink(a.dataset.msg || CONFIG.defaultMessage); });
  $$("[data-wa-text]").forEach((el) => (el.textContent = CONFIG.whatsappDisplay));
  $$("[data-mail]").forEach((a) => { a.href = "mailto:" + CONFIG.email; });
  $$("[data-mail-text]").forEach((el) => (el.textContent = CONFIG.email));
  $$("[data-ig]").forEach((a) => {
    if (!CONFIG.instagram) { (a.closest(".direct-item") || a).remove(); return; }
    a.href = "https://www.instagram.com/" + CONFIG.instagram + "/";
  });
  $$("[data-ig-text]").forEach((el) => (el.textContent = "@" + CONFIG.instagram));
  $$("[data-li]").forEach((a) => {
    if (!CONFIG.linkedin) { (a.closest(".direct-item") || a).remove(); return; }
    a.href = CONFIG.linkedin;
  });
  $$("[data-li-text]").forEach((el) => (el.textContent = "VIRELEO"));
  $$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
  document.title = document.title.replace("VIRELEO", CONFIG.brand);

  /* Text splitting (words for headings, letters for the footer wordmark) ---- */
  $$("[data-split]").forEach((el) => {
    el.setAttribute("aria-label", el.textContent.trim());
    let i = 0, html = "";
    el.childNodes.forEach((n) => {
      if (n.nodeType === 1 && n.tagName === "BR") { html += '<br class="hb">'; return; }
      const grad = n.nodeType === 1 && n.tagName === "EM";       // <em> words get the gradient
      n.textContent.trim().split(/\s+/).filter(Boolean).forEach((w) => {
        html += '<span class="w' + (grad ? " grad" : "") + '" aria-hidden="true"><span class="wi" style="--i:' + (i++) + '">' + esc(w) + "</span></span> ";
      });
    });
    el.innerHTML = html.trim();
  });
  const wordmark = $(".wordmark");
  if (wordmark) {
    const t = wordmark.textContent.trim();
    wordmark.innerHTML = Array.from(t).map((c, i) => '<span class="ch" style="--i:' + i + '">' + esc(c) + "</span>").join("");
    wordmark.setAttribute("data-letters", "");
  }

  /* Scroll reveal ---------------------------------------------------------- */
  $$("[data-stagger]").forEach((box) =>
    Array.from(box.children).forEach((ch, i) => {
      ch.setAttribute("data-reveal", "");
      ch.style.setProperty("--d", Math.min(i, 6) * 100);
    })
  );
  [".intro .btn", ".cta p", ".section-sub", ".slider-nav", ".tab-foot", ".services-head > .label"].forEach((sel) =>
    $$(sel).forEach((el) => { if (!el.hasAttribute("data-reveal")) el.setAttribute("data-reveal", ""); })
  );
  const io = "IntersectionObserver" in window && !reduce
    ? new IntersectionObserver((entries) => {
        entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); } });
      }, { threshold: 0.12, rootMargin: "0px 0px -5% 0px" })
    : null;
  const scan = (root = document) =>
    $$("[data-reveal],[data-split],[data-letters],[data-count],.stats", root).forEach((el) => {
      if (el.dataset.seen) return;
      el.dataset.seen = "1";
      if (!io) { el.classList.add("is-in"); return; }
      if (el.closest(".hero, .hero2, .banner")) return;     // hero text is triggered after the curtain lifts
      io.observe(el);
    });
  scan();
  setTimeout(() => $$(".hero [data-split], .hero2 [data-split], .banner [data-split]").forEach((el) => el.classList.add("is-in")), reduce ? 0 : 160);


  /* WhatsApp button: on the home page it stays hidden until the visitor scrolls down */
  (() => {
    const wa = document.querySelector(".wa"), hero = document.querySelector(".hero, .hero2");
    if (!wa || !hero) return;
    wa.classList.add("wa-late");
    const check = () => wa.classList.toggle("is-visible", window.scrollY > Math.max(120, window.innerHeight * 0.35));
    window.addEventListener("scroll", check, { passive: true });
    window.addEventListener("resize", check);
    check();
  })();

  /* Page curtain: wipe before leaving for another page --------------------- */
  const curtain = $(".curtain");
  document.addEventListener("click", (e) => {
    const a = e.target.closest("a[href]");
    if (!a || !curtain || reduce) return;
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (a.target === "_blank" || a.hasAttribute("download")) return;
    let url;
    try { url = new URL(a.href, location.href); } catch (_) { return; }
    if (!/^(https?|file):$/.test(url.protocol) || url.origin !== location.origin) return;
    if (url.pathname === location.pathname) return;  // same page: normal smooth scroll
    e.preventDefault();
    curtain.classList.add("leave");
    setTimeout(() => { location.href = url.href; }, 240);
  });
  window.addEventListener("pageshow", (e) => { if (e.persisted && curtain) curtain.classList.remove("leave"); });

  /* Header, progress bar and parallax ---------------------------------------- */
  const header = $("#siteHeader");
  const progress = $("#progress");
  const bg = $(".hero-bg");
  const heroCopy = $(".hero-copy") || $(".banner .wrap");
  const heroBox = $(".hero, .hero2, .banner");
  let lastY = window.scrollY, ticking = false;
  let docMax = 0;
  const measure = () => { docMax = document.documentElement.scrollHeight - window.innerHeight; };
  measure();
  if ("ResizeObserver" in window) new ResizeObserver(measure).observe(document.body); else window.addEventListener("load", measure);
  const frame = () => {
    ticking = false;
    const y = window.scrollY;
    const max = docMax;
    header.classList.toggle("is-scrolled", y > 8);
    const menuOpen = document.documentElement.classList.contains("fs-lock");
    if (y <= 260 || y < lastY - 4) header.classList.remove("is-hidden");
    else if (y > lastY + 4 && !menuOpen) header.classList.add("is-hidden");
    lastY = y;
    if (progress) progress.style.setProperty("--p", max > 0 ? (y / max).toFixed(4) : 0);
    if (!reduce && heroBox && bg) {
      const h = heroBox.offsetHeight;
      if (y < h + 100) {
        bg.style.translate = "0 " + (y * 0.28).toFixed(1) + "px";
        if (heroCopy) {
          heroCopy.style.translate = "0 " + (y * 0.16).toFixed(1) + "px";
          heroCopy.style.opacity = Math.max(0, 1 - y / (h * 0.85)).toFixed(3);
        }
      }
    }
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  frame();

  /* Soft light that follows the pointer over the hero ------------------------- */
  if (bg && !reduce && window.matchMedia("(pointer: fine)").matches) {
    let tx = 70, ty = 40, cx = 70, cy = 40, raf = 0;
    const loop = () => {
      cx += (tx - cx) * 0.08; cy += (ty - cy) * 0.08;
      bg.style.setProperty("--mx", cx.toFixed(2) + "%");
      bg.style.setProperty("--my", cy.toFixed(2) + "%");
      raf = Math.abs(tx - cx) + Math.abs(ty - cy) > 0.05 ? requestAnimationFrame(loop) : 0;
    };
    heroBox.addEventListener("pointermove", (e) => {
      const r = heroBox.getBoundingClientRect();
      tx = ((e.clientX - r.left) / r.width) * 100;
      ty = ((e.clientY - r.top) / r.height) * 100;
      if (!raf) raf = requestAnimationFrame(loop);
    });
  }

  /* Mobile menu ------------------------------------------------------------------ */
  const toggle = $("#menuToggle"), nav = $("#mainNav");
  const igUrl = CONFIG.instagram ? "https://instagram.com/" + CONFIG.instagram : "";
  const liUrl = CONFIG.linkedin || "";
  const fs = document.createElement("div");
  fs.className = "fsmenu"; fs.id = "fsMenu"; fs.setAttribute("role", "dialog"); fs.setAttribute("aria-modal", "true"); fs.setAttribute("aria-label", "Site menu"); fs.hidden = true;
  const links = [["Home","index.html"],["Services","index.html#services"],["Work","work.html"],["Capabilities","capabilities.html"],["About","about.html"],["Contact","contact.html"]];
  fs.innerHTML =
    '<button class="fs-close" type="button" aria-label="Close menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" aria-hidden="true"><path d="M4 4l16 16M20 4 4 20"/></svg></button>' +
    '<a class="fs-brand" href="index.html" aria-label="Home"><span>' + esc(CONFIG.brand) + '</span></a>' +
    '<div class="fs-grid"><nav class="fs-links" aria-label="Menu">' +
    links.map((l, i) => '<a href="' + l[1] + '" style="--i:' + i + '"><small>0' + (i + 1) + '</small><span>' + l[0] + '</span></a>').join("") +
    '</nav><div class="fs-side"><div class="fs-col" style="--i:2"><p>Services</p>' +
    '<a href="work.html?cat=web">Web Development</a><a href="work.html?cat=app">App Development</a><a href="work.html?cat=automation">AI Automation</a><a href="work.html?cat=chatbot">AI Chatbot Development</a></div>' +
    '<div class="fs-col" style="--i:4"><p>Contact</p><a href="mailto:' + esc(CONFIG.email) + '">' + esc(CONFIG.email) + '</a><a href="' + waLink(CONFIG.defaultMessage) + '" target="_blank" rel="noopener">WhatsApp ' + esc(CONFIG.whatsappDisplay) + '</a></div>' +
    '<div class="fs-socials" style="display:flex;gap:16px;align-items:center;">' +
    (igUrl ? '<a class="fs-ig" style="--i:5" href="' + igUrl + '" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 64 64" aria-hidden="true"><defs><radialGradient id="igG" cx="20%" cy="104%" r="130%"><stop offset="0" stop-color="#fdf497"/><stop offset=".08" stop-color="#fdf497"/><stop offset=".45" stop-color="#fd5949"/><stop offset=".6" stop-color="#d6249f"/><stop offset="1" stop-color="#285AEB"/></radialGradient></defs><rect width="64" height="64" rx="18" fill="url(#igG)"/><rect x="14" y="14" width="36" height="36" rx="11" fill="none" stroke="#fff" stroke-width="3.6"/><circle cx="32" cy="32" r="8.4" fill="none" stroke="#fff" stroke-width="3.6"/><circle cx="43" cy="21" r="2.4" fill="#fff"/></svg></a>' : "") +
    (liUrl ? '<a class="fs-li" style="--i:6" href="' + liUrl + '" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="18" fill="#0A66C2"/><path d="M19 25h7v21h-7zM22.5 16.5a4.2 4.2 0 1 0 0 8.4 4.2 4.2 0 0 0 0-8.4zM31 25h6.6v2.9h.1c.9-1.8 3.2-3.7 6.6-3.7 7.1 0 8.4 4.7 8.4 10.7V46h-7V35.2c0-2.6 0-5.9-3.6-5.9-3.6 0-4.2 2.8-4.2 5.7V46H31z" fill="#fff"/></svg></a>' : "") +
    '</div></div></div>';
  document.body.appendChild(fs);
  let fsTimer = 0;
  const setMenu = (open) => {
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    clearTimeout(fsTimer);
    if (open) {
      header.classList.remove("is-hidden");
      fs.hidden = false;
      requestAnimationFrame(() => requestAnimationFrame(() => fs.classList.add("is-open")));
      document.documentElement.classList.add("fs-lock");
      const c = $(".fs-close", fs); if (c) c.focus({ preventScroll: true });
    } else {
      fs.classList.remove("is-open");
      document.documentElement.classList.remove("fs-lock");
      fsTimer = setTimeout(() => { fs.hidden = true; }, 500);
    }
  };
  toggle.addEventListener("click", () => setMenu(toggle.getAttribute("aria-expanded") !== "true"));
  fs.addEventListener("click", (e) => { if (e.target.closest(".fs-close") || e.target.closest("a")) setMenu(false); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") setMenu(false); });

  /* Mobile: tap "Services" to open / close its dropdown (desktop keeps hover) */
  const megaWrap = $(".has-mega"), mobileNav = window.matchMedia("(max-width: 860px)");
  if (megaWrap) {
    const megaLink = $(".nl", megaWrap);
    const setMega = (open) => { megaWrap.classList.toggle("is-open", open); megaLink.setAttribute("aria-expanded", String(open)); };
    megaLink.addEventListener("click", (e) => { if (mobileNav.matches) { e.preventDefault(); setMega(!megaWrap.classList.contains("is-open")); } });
    document.addEventListener("click", (e) => { if (!megaWrap.contains(e.target)) setMega(false); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") setMega(false); });
    mobileNav.addEventListener("change", () => setMega(false));
    window.addEventListener("scroll", () => { if (megaWrap.classList.contains("is-open")) setMega(false); }, { passive: true });
  }

  /* Text swap used by the sliders ---------------------------------------------------- */
  const swap = (els, apply, dir) => {
    if (reduce || !els[0].animate) { apply(); return; }
    const out = els.map((el, k) => el.animate(
      [{ opacity: 1, transform: "none" }, { opacity: 0, transform: "translateY(" + -14 * dir + "px)" }],
      { duration: 220, delay: k * 40, easing: "ease-in", fill: "forwards" }).finished);
    Promise.all(out).then(() => {
      apply();
      els.forEach((el, k) => {
        el.getAnimations().forEach((a) => a.cancel());
        el.animate(
          [{ opacity: 0, transform: "translateY(" + 18 * dir + "px)" }, { opacity: 1, transform: "none" }],
          { duration: 600, delay: k * 70, easing: EASE, fill: "backwards" });
      });
    });
  };

  /* Autoplay helper: runs a progress line, then calls next ------------------------------- */
  const autoplay = (bar, ms, next, hoverEl) => {
    if (reduce || !bar || !bar.animate) return { restart() {} };
    let anim;
    const restart = () => {
      if (anim) anim.cancel();
      anim = bar.animate([{ transform: "scaleX(0)" }, { transform: "scaleX(1)" }], { duration: ms, fill: "forwards" });
      anim.onfinish = next;
    };
    ["mouseenter", "focusin"].forEach((ev) => hoverEl.addEventListener(ev, () => anim && anim.pause()));
    ["mouseleave", "focusout"].forEach((ev) => hoverEl.addEventListener(ev, () => anim && anim.play()));
    document.addEventListener("visibilitychange", () => { if (anim) (document.hidden ? anim.pause() : anim.play()); });
    restart();
    return { restart };
  };

  /* Thumbnails and cards ----------------------------------------------------------------- */
  const mock = {
    web: (p) => '<div class="mk-browser"><div class="mk-bar"><i></i><i></i><i></i></div><div class="mk-page"><b>' + esc(p.title) + '</b><i></i><i></i><em></em></div></div>',
    chatbot: () => '<div class="mk-phone"><span class="bub"></span><span class="bub out"></span><span class="bub short"></span><span class="bub out short"></span><span class="bub"></span></div>',
    app: () => '<div class="mk-phone"><div class="sun"></div><div class="temp">24°</div><span class="bub"></span><span class="bub out short"></span><div class="alert">Hail warning</div></div>',
    automation: () => '<div class="mk-flow"><span class="node"></span><i class="link"></i><span class="node"></span><i class="link"></i><span class="node"></span></div>'
  };
  const thumb = (p) =>
    '<div class="thumb" data-cat="' + p.cat + '">' + mock[p.cat](p) +
    (p.shot ? '<img src="' + esc(p.shot) + '" alt="' + esc(p.title) + ' preview" loading="lazy" onerror="this.remove()">' : "") + "</div>";
  const card = (p, i) =>
    '<article class="card" data-reveal style="--d:' + (i % 2) * 110 + '">' + thumb(p) +
    "<h3>" + esc(p.title) + "</h3><p>" + esc(p.desc) + "</p>" +
    '<div class="card-foot"><span class="label">' + CATS[p.cat].name + " · " + status(p) + "</span>" +
    '<a class="arrow-link label" href="' + esc(projectLink(p)) + '" target="_blank" rel="noopener">Details ' + ARROW +
    '<span class="sr-only"> about ' + esc(p.title) + "</span></a></div></article>";

  /* Hero featured carousel ------------------------------------------------------------------- */
  const featLink = $("#featLink");
  if (featLink) {
    const live = PROJECTS.filter((p) => p.url);
    let i = 0;
    const apply = () => {
      const p = live[i];
      $("#featTitle").textContent = p.title;
      $("#featMeta").textContent = CATS[p.cat].name + " · " + status(p);
      featLink.href = p.url;
    };
    const go = (n, dir) => {
      i = (n + live.length) % live.length;
      swap([$("#featTitle"), $("#featMeta")], apply, dir);
      auto.restart();
    };
    const auto = autoplay($("#featBar"), 6000, () => go(i + 1, 1), $(".featured-card"));
    $("#featPrev").addEventListener("click", () => go(i - 1, -1));
    $("#featNext").addEventListener("click", () => go(i + 1, 1));
    apply();
  }

  /* Service slider ------------------------------------------------------------------------------ */
  const track = $("#svcTrack");
  if (track) {
    const step = () => (track.firstElementChild ? track.firstElementChild.getBoundingClientRect().width + 20 : 300);
    const nudge = (d) => {
      if (document.documentElement.classList.contains("pin")) {
        const sec = $("#services-intro"), travel = track.scrollWidth - track.clientWidth;
        const total = sec.offsetHeight - window.innerHeight;
        const frac = (d * step()) / (travel || 1) * 0.8 * total;
        window.scrollBy({ top: frac, behavior: "smooth" });
      } else track.scrollBy({ left: d * step(), behavior: "smooth" });
    };
    $("#svcPrev").addEventListener("click", () => nudge(-1));
    $("#svcNext").addEventListener("click", () => nudge(1));
  }

  /* Capabilities slider -------------------------------------------------------------------------- */
  const stage = $("#capsStage");
  if (stage) {
    const rail = $("#capsRail");
    let c = 0;
    rail.innerHTML = CAPABILITIES.map((x, n) => '<button type="button" role="tab" aria-selected="false" aria-label="Point ' + (n + 1) + '"><b>0' + (n + 1) + "</b><span>" + esc(x.k) + "</span></button>").join("");
    const inner = $(".caps-inner");
    const ghost = document.createElement("div"); ghost.className = "caps-ghost"; ghost.setAttribute("aria-hidden", "true"); inner.appendChild(ghost);
    const eyebrow = document.createElement("p"); eyebrow.className = "caps-eyebrow"; stage.insertBefore(eyebrow, stage.firstChild);
    const tagsEl = document.createElement("div"); tagsEl.className = "caps-tags"; stage.insertBefore(tagsEl, $(".caps-nav", stage));
    const paint = () => {
      $("#capsTitle").textContent = CAPABILITIES[c].t;
      $("#capsText").textContent = CAPABILITIES[c].d;
      ghost.textContent = "0" + (c + 1);
      eyebrow.textContent = "Capability 0" + (c + 1) + " / 0" + CAPABILITIES.length;
      tagsEl.innerHTML = CAPABILITIES[c].tags.map((t) => "<span>" + esc(t) + "</span>").join("");
      /* v61 — highlight cycles through the chips every 1 s (1→2→3→1…), restarted for every point */
      const chips = $$("span", tagsEl); let ti = 0;
      const light = () => chips.forEach((el, k) => el.classList.toggle("is-on", k === ti));
      light(); clearInterval(window.__capsTagTimer);
      if (chips.length > 1 && !matchMedia("(prefers-reduced-motion: reduce)").matches) window.__capsTagTimer = setInterval(() => { ti = (ti + 1) % chips.length; light(); }, 1000);
    };
    const mark = () => $$("button", rail).forEach((b, k) => b.setAttribute("aria-selected", String(k === c)));
    const go = (n, dir) => {
      c = (n + CAPABILITIES.length) % CAPABILITIES.length;
      mark();
      swap([$("#capsTitle"), $("#capsText"), tagsEl, eyebrow], paint, dir);
      auto.restart();
    };
    const auto = autoplay($("#capsBar"), 3000, () => go(c + 1, 1), document.createElement("div"));   /* v50: every 3 s, endless loop 1→5→1 */
    window.__capsGo = (n) => { if (n !== c) go(n, n > c ? 1 : -1); };
    $$("button", rail).forEach((b, k) => b.addEventListener("click", () => go(k, k >= c ? 1 : -1)));
    $("#capsPrev").addEventListener("click", () => go(c - 1, -1));
    $("#capsNext").addEventListener("click", () => go(c + 1, 1));
    paint(); mark();
  }

  /* Home: work tabs ---------------------------------------------------------------------------------- */
  const tabs = $("#workTabs");
  if (tabs) {
    const keys = Object.keys(CATS);
    tabs.innerHTML = keys.map((k) => '<button type="button" class="tab" role="tab" data-cat="' + k + '" aria-selected="false"><span class="node"></span><span class="label">' + CATS[k].name + "</span></button>").join("");
    const out = $("#workCards");
    const pick = (k) => {
      const idx = keys.indexOf(k);
      tabs.style.setProperty("--fill", idx / (keys.length - 1));
      $$(".tab", tabs).forEach((t, n) => {
        t.setAttribute("aria-selected", String(t.dataset.cat === k));
        t.classList.toggle("is-past", n < idx);
      });
      const list = PROJECTS.filter((p) => p.cat === k);
      out.dataset.count = list.length;
      out.innerHTML = list.map(card).join("");
      scan(out);
    };
    $$(".tab", tabs).forEach((t) => t.addEventListener("click", () => pick(t.dataset.cat)));
    pick("web");
    window.__workKeys = keys;
    /* Pinned layout: keep all text at full size and let only the preview image strip flex so the whole panel fits the window */
    const wpEl = $("#work-preview"), panelEl = $(".work-panel");
    const fit = () => {
      if (!document.documentElement.classList.contains("pinw")) return;
      const th = $(".work-panel .card .thumb");
      if (!th) return;
      const avail = window.innerHeight - 64 - 16;
      const others = panelEl.offsetHeight - th.offsetHeight;
      const chat = th.dataset.cat === "chatbot";
      wpEl.classList.toggle("chat-tab", chat);
      const others2 = others;
      const h = Math.max(84, Math.min(400, avail - others2));
      wpEl.style.setProperty("--th", Math.round(h) + "px");
    };
    window.__workPick = (k) => { pick(k); requestAnimationFrame(fit); };
    let frt; window.addEventListener("resize", () => { clearTimeout(frt); frt = setTimeout(fit, 120); });
    requestAnimationFrame(fit); setTimeout(fit, 600);
  }

  /* Work page: filters ---------------------------------------------------------------------------------- */
  const grid = $("#workGrid");
  if (grid) {
    const buttons = $$(".filter");
    const apply = (k) => {
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.filter === k)));
      const list = PROJECTS.filter((p) => k === "all" || p.cat === k);
      grid.innerHTML = list.length ? list.map(card).join("") : '<p class="empty">No projects in this category yet.</p>';
      scan(grid);
    };
    buttons.forEach((b) => b.addEventListener("click", () => apply(b.dataset.filter)));
    const q = new URLSearchParams(location.search).get("cat");
    apply(q && CATS[q] ? q : "all");
  }

  /* Chat screenshot viewer: tap a chatbot preview to read the whole conversation ---------------- */
  (() => {
    let box = null, lastFocus = null;
    const close = () => {
      if (!box) return;
      box.classList.remove("is-open");
      document.documentElement.classList.remove("zoom-lock");
      const b = box; box = null;
      setTimeout(() => b.remove(), 260);
      if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
    };
    const open = (img) => {
      if (box) return;
      lastFocus = document.activeElement;
      box = document.createElement("div");
      box.className = "zoomview"; box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true"); box.setAttribute("aria-label", img.alt || "Preview");
      box.innerHTML = '<button class="zv-close" type="button" aria-label="Close preview"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M5 5l14 14M19 5 5 19"/></svg></button><div class="zv-scroll"><img src="' + esc((img.currentSrc || img.src).replace("-wide.jpg", ".jpg")) + '" alt="' + esc(img.alt || "") + '"></div>';
      document.body.appendChild(box);
      document.documentElement.classList.add("zoom-lock");
      requestAnimationFrame(() => box && box.classList.add("is-open"));
      box.addEventListener("click", (e) => { if (e.target.closest(".zv-close") || !e.target.closest("img")) close(); });
      $(".zv-close", box).focus({ preventScroll: true });
    };
    document.addEventListener("click", (e) => {
      const img = e.target.closest && e.target.closest('.thumb[data-cat="chatbot"] img');
      if (!img) return;
      e.preventDefault(); e.stopPropagation(); open(img);
    }, true);
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
  })();

  /* Contact form: validate, then open WhatsApp ----------------------------------------------------------- */
  const form = $("#contactForm");
  if (form) {
    const req = [
      { el: $("#cfName"), err: $("#cfNameErr"), msg: "Enter your name so we know who to reply to." },
      { el: $("#cfMessage"), err: $("#cfMessageErr"), msg: "Add a few details about your project." }
    ];
    const check = (f) => {
      const ok = f.el.value.trim().length > 0;
      f.err.textContent = ok ? "" : f.msg;
      f.el.closest(".field").classList.toggle("has-error", !ok);
      f.el.setAttribute("aria-invalid", String(!ok));
      if (!ok && f.el.animate && !reduce) f.el.animate([{ translate: "0" }, { translate: "-6px" }, { translate: "6px" }, { translate: "-4px" }, { translate: "0" }], { duration: 320 });
      return ok;
    };
    req.forEach((f) => f.el.addEventListener("input", () => { if (f.err.textContent) check(f); }));
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const res = req.map(check);
      if (res.includes(false)) { req[res.indexOf(false)].el.focus(); return; }
      const email = $("#cfEmail").value.trim();
      const text = "Hi " + CONFIG.brand + ", my name is " + req[0].el.value.trim() + "." +
        (email ? "\nEmail: " + email : "") +
        "\nI need: " + $("#cfService").value + "\n\n" + req[1].el.value.trim();
      window.open(waLink(text), "_blank", "noopener");
    });
  }
})();


/* ==========================================================================
   MOTION v4 — extra animations (network background, typewriter, count-up,
   scroll-scrubbed text, pinned story, timeline fill, spotlight, magnetic buttons)
   ========================================================================== */
(function () {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = window.matchMedia("(pointer: fine)").matches;
  const vh = () => window.innerHeight;

  /* Aurora blobs + drifting network behind the hero and page banners --------- */
  const heroBg = $(".hero-bg");
  if (heroBg) {
    ["b1", "b2", "b3"].forEach((c) => { const b = document.createElement("span"); b.className = "blob " + c; b.setAttribute("aria-hidden", "true"); heroBg.appendChild(b); });
    const dark = !!$(".banner");
    const cv = document.createElement("canvas");
    cv.className = "net"; cv.setAttribute("aria-hidden", "true");
    heroBg.appendChild(cv);
    const ctx = cv.getContext("2d");
    let W = 0, H = 0, dpr = 1, nodes = [], mouse = { x: -999, y: -999 }, raf = 0, visible = true;
    const make = () => {
      const n = Math.round(clamp((W * H) / 30000, 20, 48));
      nodes = Array.from({ length: n }, () => ({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .35, vy: (Math.random() - .5) * .35, r: Math.random() * 1.6 + 1 }));
    };
    const size = () => {
      dpr = Math.min(window.devicePixelRatio || 1, 1.5);
      W = heroBg.clientWidth; H = heroBg.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      make();
    };
    const link = dark ? "150,190,255" : "106,61,240";
    const dot = dark ? "190,220,255" : "91,69,240";
    const draw = () => {
      ctx.clearRect(0, 0, W, H);
      const D = 150;
      for (let i = 0; i < nodes.length; i++) {
        const a = nodes[i];
        if (!reduce) {
          a.x += a.vx; a.y += a.vy;
          if (a.x < 0 || a.x > W) a.vx *= -1;
          if (a.y < 0 || a.y > H) a.vy *= -1;
          const dx = a.x - mouse.x, dy = a.y - mouse.y, d2 = dx * dx + dy * dy;
          if (d2 < 14000) { a.x += dx * 0.004; a.y += dy * 0.004; }
        }
        for (let j = i + 1; j < nodes.length; j++) {
          const b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d = Math.sqrt(dx * dx + dy * dy);
          if (d < D) { ctx.strokeStyle = "rgba(" + link + "," + ((1 - d / D) * (dark ? .32 : .26)).toFixed(3) + ")"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); }
        }
        ctx.fillStyle = "rgba(" + dot + "," + (dark ? .7 : .55) + ")";
        ctx.beginPath(); ctx.arc(a.x, a.y, a.r, 0, 6.2832); ctx.fill();
      }
      raf = !reduce && visible && !document.hidden ? requestAnimationFrame(draw) : 0;
    };
    size(); draw();
    let rt; window.addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => { size(); if (!raf) draw(); }, 150); });
    if ("IntersectionObserver" in window) new IntersectionObserver((e) => { visible = e[0].isIntersecting; if (visible && !raf && !reduce) draw(); }).observe(heroBg.parentElement);
    document.addEventListener("visibilitychange", () => { if (!document.hidden && !raf && !reduce) draw(); });
    heroBg.parentElement.addEventListener("pointermove", (e) => { const r = cv.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
    heroBg.parentElement.addEventListener("pointerleave", () => { mouse.x = mouse.y = -999; });
  }

  /* Typewriter heading (page banners) ------------------------------------------ */
  $$("[data-type]").forEach((h) => {
    const text = h.textContent.trim();
    const hl = h.dataset.hl || "";
    const at = hl ? text.indexOf(hl) : -1;
    const safe = (x) => x.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    // first n characters of the heading, with the highlighted words wrapped in a gradient span
    const mark = (n) => {
      const part = text.slice(0, n);
      if (at < 0 || n <= at) return safe(part);
      const end = at + hl.length;
      return safe(part.slice(0, at)) + '<span class="hl">' + safe(part.slice(at, end)) + "</span>" + (n > end ? safe(part.slice(end)) : "");
    };
    h.setAttribute("aria-label", text);
    if (reduce) { h.innerHTML = mark(text.length); return; }
    h.innerHTML = '<span class="tw-full" aria-hidden="true">' + mark(text.length) + '</span><span class="tw-typed" aria-hidden="true"><span class="tw-t"></span><i class="caret"></i></span>';
    const t = $(".tw-t", h), caret = $(".caret", h);
    let n = 0;
    const tick = () => {
      n++; t.innerHTML = mark(n);
      if (n < text.length) setTimeout(tick, 12 + Math.random() * 12);
      else caret.classList.add("done");
    };
    setTimeout(tick, 180);
  });

  /* Count-up numbers + sparkline draw (hero stats) -------------------------------- */
  const stats = $("#heroStats");
  if (stats) {
    const proj = $("#statProjects");
    if (proj && typeof PROJECTS !== "undefined") proj.dataset.count = PROJECTS.length;
    const run = () => {
      stats.classList.add("is-in");
      $$("[data-count]", stats).forEach((el) => {
        const to = +el.dataset.count, suf = el.dataset.suffix || "";
        if (reduce) { el.textContent = to + suf; return; }
        const t0 = performance.now(), dur = 1700;
        const step = (t) => {
          const k = clamp((t - t0) / dur), e = 1 - Math.pow(1 - k, 4);
          el.textContent = Math.round(to * e) + suf;
          if (k < 1) requestAnimationFrame(step);
        };
        el.textContent = "0" + suf;
        requestAnimationFrame(step);
      });
    };
    setTimeout(run, reduce ? 0 : 350);
  }

  /* Scroll-scrubbed text: words sharpen as the paragraph crosses the screen ------------- */
  const scrubs = $$(".scrub").map((p) => {
    const words = p.textContent.trim().split(/\s+/);
    p.setAttribute("aria-label", p.textContent.trim());
    p.innerHTML = words.map((w) => '<span class="sw" aria-hidden="true">' + w.replace(/</g, "&lt;") + "</span>").join(" ");
    return { p, w: $$(".sw", p) };
  });

  /* Pinned story, process timeline ---------------------------------------------------------- */
  const story = $("#story"), stage = $("#storyStage");
  const lines = stage ? $$(".story-line", stage) : [];
  const phones = stage ? $$(".ph", stage) : [];
  const steps = $(".steps"), stepper = $("#stepper");
  let lastIdx = -2, lastW = -1;

  /* One pass per frame: read every rect first, then write. No layout thrashing. */
  const root = document.documentElement;
  const svSec = $("#services-intro"), svTrack = $("#svcTrack"), capsSec = $(".caps"), capsBar = $("#capsBar");
  const capsN = $$("#capsRail button").length || 5, wpSec = $("#work-preview");
  const stepLis = steps ? $$("li", steps) : [];
  const near = (r, H) => r.top < H * 1.2 && r.bottom > -H * 0.2;     // only work on sections near the screen
  let lastSv = -1;

  const update = () => {
    const H = vh(), pin = root.classList.contains("pin"), pinw = root.classList.contains("pinw");
    /* ---- read ---- */
    const sr = scrubs.map(({ p }) => p.getBoundingClientRect());
    const stR = story && stage && !reduce ? story.getBoundingClientRect() : null;
    const svR = null; /* v44: services slider runs by itself, no longer scroll-driven */
    const cpR = null; /* v50: capabilities now advance by themselves */
    const wpR = pinw && wpSec ? wpSec.getBoundingClientRect() : null;
    const tlR = steps ? steps.getBoundingClientRect() : null;
    const liR = tlR && near(tlR, H) ? stepLis.map((li) => li.getBoundingClientRect().top) : null;
    const trMax = svR && svTrack ? svTrack.scrollWidth - svTrack.clientWidth : 0;
    /* ---- write ---- */
    scrubs.forEach(({ w }, k) => {
      const r = sr[k];
      if (r.bottom < -H || r.top > H * 1.2) return;
      const prog = clamp((H * 0.82 - r.top) / (r.height + H * 0.28));
      const n = Math.round(prog * w.length * 1.08);
      w.forEach((el, i) => { const on = reduce || i < n; if (on !== el.classList.contains("on")) el.classList.toggle("on", on); });
    });
    if (stR && near(stR, H)) {
      const e = clamp((H - stR.top) / (H * 0.95));
      const p = clamp(-stR.top / (stR.height - H));
      stage.style.setProperty("--e", e.toFixed(3));
      phones.forEach((el) => el.style.setProperty("--p", p.toFixed(3)));
      const idx = e < 0.9 ? -1 : Math.min(lines.length - 1, Math.floor(p * lines.length * 0.999));
      if (idx !== lastIdx) {
        lastIdx = idx;
        lines.forEach((l, i) => { l.classList.toggle("on", i === idx); l.classList.toggle("past", i < idx); });
      }
    }
    if (svR && svR.top < H && svR.bottom > 0) {
      const p = clamp(-svR.top / (svR.height - H));
      const e = p < 0.1 ? 0 : p > 0.9 ? 1 : (p - 0.1) / 0.8;           // hold at both ends, slide in the middle
      const x = Math.round(e * trMax);
      if (x !== lastSv) { lastSv = x; svTrack.scrollLeft = x; }
    }
    if (cpR && cpR.top < H && cpR.bottom > 0 && window.__capsGo) {
      const p = clamp(-cpR.top / (cpR.height - H));
      const i = Math.min(capsN - 1, Math.floor(p * capsN));
      window.__capsGo(i);
      if (capsBar) capsBar.style.transform = "scaleX(" + (p * capsN - i).toFixed(3) + ")";
    }
    if (wpR && wpR.top < H && wpR.bottom > 0 && window.__workPick) {
      const keys = window.__workKeys, p = clamp(-wpR.top / (wpR.height - H));
      const i = Math.min(keys.length - 1, Math.floor(p * keys.length));
      if (i !== lastW) { lastW = i; window.__workPick(keys[i]); }
    }
    if (tlR && liR) {
      const prog = clamp((H * 0.62 - tlR.top) / tlR.height).toFixed(3);
      steps.style.setProperty("--tl", prog);
      if (stepper) stepper.style.setProperty("--tl", prog);
      stepLis.forEach((li, i) => {
        const on = reduce || liR[i] + 40 < H * 0.62;
        if (on !== li.classList.contains("on")) {
          li.classList.toggle("on", on);
          if (stepper && stepper.children[i]) stepper.children[i].classList.toggle("on", on);
        }
      });
    }
  };
  let tk = false;
  const req = () => { if (!tk) { tk = true; requestAnimationFrame(() => { tk = false; update(); }); } };
  window.addEventListener("scroll", req, { passive: true });
  window.addEventListener("resize", req);
  update();

  /* Spotlight that follows the pointer on cards ------------------------------------------------ */
  if (fine && !reduce) {
    document.addEventListener("pointermove", (e) => {
      const c = e.target.closest && e.target.closest(".service, .cm");
      if (!c) return;
      const r = c.getBoundingClientRect();
      c.style.setProperty("--sx", (e.clientX - r.left) + "px");
      c.style.setProperty("--sy", (e.clientY - r.top) + "px");
    }, { passive: true });

    /* Magnetic buttons (one active button tracked, no DOM queries per move) */
    let mag = null;
    document.addEventListener("pointermove", (e) => {
      const b = e.target.closest && e.target.closest(".btn-blue, .btn-white");
      if (mag && mag !== b) { mag.style.translate = ""; mag = null; }
      if (!b) return;
      mag = b;
      const r = b.getBoundingClientRect();
      b.style.translate = ((e.clientX - r.left - r.width / 2) * 0.16).toFixed(1) + "px " + ((e.clientY - r.top - r.height / 2) * 0.28).toFixed(1) + "px";
    }, { passive: true });
  }

  /* Drag-to-scroll on the services track ------------------------------------------------------------ */
  const trk = $("#svcTrack");
  if (trk && fine && !document.documentElement.classList.contains("pin")) {
    let down = false, sx = 0, sl = 0, moved = 0;
    trk.addEventListener("pointerdown", (e) => { if (e.button !== 0) return; down = true; moved = 0; sx = e.clientX; sl = trk.scrollLeft; });
    window.addEventListener("pointermove", (e) => {
      if (!down) return;
      const dx = e.clientX - sx; moved = Math.max(moved, Math.abs(dx));
      if (moved > 6) { trk.classList.add("is-drag"); trk.scrollLeft = sl - dx; }
    });
    window.addEventListener("pointerup", () => { if (!down) return; down = false; setTimeout(() => trk.classList.remove("is-drag"), 0); });
    trk.addEventListener("click", (e) => { if (moved > 6) { e.preventDefault(); e.stopPropagation(); } }, true);
  }
})();

/* v39 — 3D tilt for the About picture: mouse tilt on desktop, scroll-driven tilt on touch screens */
(() => {
  const box = document.querySelector("[data-tilt]");
  if (!box || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const set = (rx, ry, px, py, gx, gy, glare) => {
    box.style.setProperty("--rx", rx.toFixed(2) + "deg"); box.style.setProperty("--ry", ry.toFixed(2) + "deg");
    box.style.setProperty("--px", px.toFixed(1) + "px"); box.style.setProperty("--py", py.toFixed(1) + "px");
    box.style.setProperty("--gx", gx.toFixed(1) + "%"); box.style.setProperty("--gy", gy.toFixed(1) + "%");
    box.style.setProperty("--glare", glare);
  };
  const canHover = window.matchMedia("(hover: hover) and (pointer: fine)");
  let raf = 0, onScreen = false;
  box.addEventListener("pointermove", (e) => {
    if (e.pointerType !== "mouse") return;
    const r = box.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
    box.classList.add("is-live");
    set(-y * 16, x * 20, -x * 16, -y * 12, (x + .5) * 100, (y + .5) * 100, .9);
  });
  box.addEventListener("pointerleave", () => { box.classList.remove("is-live"); set(0, 0, 0, 0, 30, 20, 0); });
  /* touch / no-hover devices: tilt follows how far the picture is from the middle of the screen */
  const scrollTilt = () => {
    raf = 0;
    if (canHover.matches || !onScreen) return;
    const r = box.getBoundingClientRect(), vh = window.innerHeight || 1;
    const p = Math.max(-1, Math.min(1, ((r.top + r.height / 2) - vh / 2) / vh));
    set(p * -9, p * 7, p * -6, p * 10, 50 + p * 30, 50 - p * 30, .55);
  };
  const queue = () => { if (!raf) raf = requestAnimationFrame(scrollTilt); };
  if ("IntersectionObserver" in window) new IntersectionObserver((en) => { onScreen = en[0].isIntersecting; queue(); }, { rootMargin: "80px" }).observe(box);
  else onScreen = true;
  window.addEventListener("scroll", queue, { passive: true });
  window.addEventListener("resize", queue);
  queue();
})();


/* v44 — services slider: endless auto-loop (pauses on hover/touch, arrows still work) */
(() => {
  const track = document.getElementById("svcTrack");
  if (!track || !track.children.length) return;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const originals = Array.from(track.children);
  const makeSet = () => originals.forEach((c) => {
    const k = c.cloneNode(true);
    k.setAttribute("aria-hidden", "true"); k.tabIndex = -1; k.dataset.clone = "1";
    k.removeAttribute("data-reveal"); k.classList.add("is-in"); k.style.opacity = "1"; k.style.transform = "none";
    k.querySelectorAll("a, button").forEach((x) => x.tabIndex = -1);
    track.appendChild(k);
  });
  originals.forEach((c) => { c.classList.add("is-in"); });
  makeSet();
  /* enough copies so the strip never runs out, whatever the screen width */
  const fill = () => {
    const first = track.children[0], second = track.children[originals.length];
    if (!first || !second) return;
    const w = second.offsetLeft - first.offsetLeft;
    if (!w) return;
    const need = Math.ceil(track.clientWidth / w) + 1;       // copies needed after the first set
    let have = track.children.length / originals.length - 1;
    while (have < need) { makeSet(); have++; }
    track.querySelectorAll("img").forEach((i) => { i.loading = "eager"; });
  };
  fill();
  window.addEventListener("resize", fill);
  track.querySelectorAll("img").forEach((i) => { i.loading = "eager"; i.decoding = "async"; });
  track.classList.add("is-auto");
  const SPEED = 38;                  // px per second
  let pos = 0, last = 0, hold = false, holdTimer = 0, extra = 0, visible = true;
  const setHold = (ms) => { hold = true; clearTimeout(holdTimer); if (ms) holdTimer = setTimeout(() => { pos = track.scrollLeft; hold = false; }, ms); };
  const loopW = () => { const c = track.children[originals.length]; return c ? c.offsetLeft - track.children[0].offsetLeft : 0; };
  const step = () => (track.children[0].getBoundingClientRect().width + 20);
  const tick = (t) => {
    const dt = Math.min(0.25, (t - (last || t)) / 1000); last = t;
    const w = loopW();
    if (w) {
      if (!hold && !reduce) pos += SPEED * dt;
      if (extra) { const d = extra * Math.min(1, dt * 7); extra -= d; pos += d; if (Math.abs(extra) < 0.5) { pos += extra; extra = 0; } }
      if (pos >= w) pos -= w; else if (pos < 0) pos += w;
      if (!hold || extra) track.scrollLeft = pos;
    }
    requestAnimationFrame(tick);
  };
  const bind = (id, d) => {
    const b = document.getElementById(id); if (!b) return;
    const fresh = b.cloneNode(true); b.replaceWith(fresh);          // drop the old click handler
    fresh.addEventListener("click", () => { pos = track.scrollLeft; extra += d * step(); });
  };
  bind("svcPrev", -1); bind("svcNext", 1);
  track.addEventListener("touchstart", () => setHold(0), { passive: true });
  track.addEventListener("touchend", () => setHold(2500), { passive: true });
  track.addEventListener("wheel", () => setHold(2000), { passive: true });
  requestAnimationFrame(tick);
})();


/* v62 — home page intro video: open from the floating button, close with X / backdrop / Esc */
(function () {
  const openBtn = document.getElementById("vidOpen"), modal = document.getElementById("vidModal"), v = document.getElementById("vidEl");
  if (!openBtn || !modal || !v) return;
  /* show only while the page is at the top (hero); hide once the visitor scrolls down */
  const toggleFab = () => openBtn.classList.toggle("is-away", window.scrollY > 80);
  window.addEventListener("scroll", toggleFab, { passive: true }); toggleFab();
  const close = () => {
    v.pause(); modal.classList.remove("is-open");
    setTimeout(() => { modal.hidden = true; }, 300);
    document.removeEventListener("keydown", onKey); openBtn.focus({ preventScroll: true });
  };
  const onKey = (e) => { if (e.key === "Escape") close(); };
  openBtn.addEventListener("click", () => {
    modal.hidden = false; void modal.offsetWidth; modal.classList.add("is-open");
    document.addEventListener("keydown", onKey);
    const p = v.play(); if (p && p.catch) p.catch(() => {});
    document.getElementById("vidClose").focus({ preventScroll: true });
  });
  document.getElementById("vidClose").addEventListener("click", close);
  modal.addEventListener("click", (e) => { if (e.target === modal) close(); });
})();

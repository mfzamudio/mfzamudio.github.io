document.addEventListener("DOMContentLoaded", function () {
  const loadHTML = (selector, file) => {
    fetch(file)
      .then(response => response.text())
      .then(data => {
        const el = document.querySelector(selector);
        if (el) el.innerHTML = data;
      });
  };

  loadHTML("#header-placeholder", "/partials/header.html");
  loadHTML("#footer-placeholder", "/partials/footer.html");

  const path = location.pathname;
  const page = path.split("/").pop() || "index.html";

  // Wrap the existing <main> in a .pub-layout flex container and inject a
  // sticky .pub-sidebar built from `navFile`, then hand the <aside> back so
  // the caller can wire up active-state (filename match or scroll-spy).
  const injectSidebar = (navFile, onReady) => {
    fetch(navFile)
      .then(r => r.text())
      .then(html => {
        const main = document.querySelector("main");
        if (!main) return;
        const layout = document.createElement("div");
        layout.className = "pub-layout";
        const aside = document.createElement("aside");
        aside.className = "pub-sidebar";
        aside.innerHTML = html;
        main.parentNode.insertBefore(layout, main);
        layout.appendChild(aside);
        layout.appendChild(main);
        onReady(aside);
      })
      .catch(() => {});
  };

  // In-page table of contents: highlight the section currently in view and
  // reveal its group. Only the "leaf" links are observed — for a group with
  // sub-items (projects) the children, otherwise the section link itself
  // (resume) — so a wide wrapping section never steals the highlight.
  const initScrollSpy = (aside) => {
    const map = new Map();   // target id -> nav <a>
    const targets = [];
    aside.querySelectorAll(".pub-nav-group").forEach(group => {
      const subs = group.querySelectorAll("li a");
      const leaves = subs.length ? subs : group.querySelectorAll(".pub-nav-series");
      leaves.forEach(a => {
        const id = (a.getAttribute("href") || "").replace(/^#/, "");
        const el = id && document.getElementById(id);
        if (el) { map.set(id, a); targets.push(el); }
      });
    });
    if (!targets.length) return;

    const setActive = (id) => {
      aside.querySelectorAll("a.active").forEach(a => a.classList.remove("active"));
      aside.querySelectorAll(".active-group").forEach(g => g.classList.remove("active-group"));
      const a = map.get(id);
      if (!a) return;
      a.classList.add("active");
      const group = a.closest(".pub-nav-group");
      if (group) group.classList.add("active-group");
    };

    const obs = new IntersectionObserver(entries => {
      const visible = entries
        .filter(e => e.isIntersecting)
        .sort((x, y) => x.boundingClientRect.top - y.boundingClientRect.top);
      if (visible.length) setActive(visible[0].target.id);
    }, { rootMargin: "-120px 0px -65% 0px", threshold: 0 });

    targets.forEach(t => obs.observe(t));
    setActive(targets[0].id);
  };

  // Cross-page nav: mark the current page active by filename and reveal the
  // group it belongs to (used by publications + projects). `links` limits
  // which anchors can match (so section-header links don't false-match).
  const markActiveByFilename = (aside, fallback, links) => {
    const here = page || fallback;
    (links || aside.querySelectorAll("a")).forEach(a => {
      if (a.getAttribute("href").split("/").pop().split("#")[0] === here) {
        a.classList.add("active");
        const group = a.closest(".pub-nav-group");
        if (group) group.classList.add("active-group");
      }
    });
  };

  // Make each first-level group with sub-items collapsible. Wrap its header in
  // a row + a chevron toggle button (always collapses/expands in place,
  // flipping .active-group which drives the <ul> display; aria-expanded synced).
  // The HEADER text behaves per sidebar:
  //   • Writing (default): the header keeps navigating to the series landing —
  //     so it does BOTH (chevron collapses, header text opens the landing).
  //   • Projects (headerToggles=true): the header has no per-group landing, so
  //     its text toggles the group in place too.
  const wireCollapsibles = (aside, headerToggles) => {
    aside.querySelectorAll(".pub-nav-group").forEach(group => {
      const ul = group.querySelector(":scope > ul");
      const series = group.querySelector(":scope > .pub-nav-series");
      if (!ul || !series) return;   // childless groups stay plain links
      const row = document.createElement("div");
      row.className = "pub-nav-series-row";
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "pub-nav-toggle";
      btn.setAttribute("aria-label", "Expand or collapse section");
      group.insertBefore(row, series);
      row.appendChild(btn);
      row.appendChild(series);
      const sync = () => btn.setAttribute("aria-expanded",
        group.classList.contains("active-group") ? "true" : "false");
      const toggle = () => { group.classList.toggle("active-group"); sync(); };
      sync();
      btn.addEventListener("click", toggle);
      if (headerToggles) {
        series.addEventListener("click", e => { e.preventDefault(); toggle(); });
      }
    });
  };

  if (path.includes("/publications/")) {
    // Publications: the current series starts expanded; any group can be
    // toggled open/closed via its chevron. Series-landing links are matchable,
    // so the header can highlight on its own landing page.
    injectSidebar("/partials/publications-nav.html", aside => {
      markActiveByFilename(aside, "publications.html");
      wireCollapsibles(aside);
    });
  } else if (page === "projects.html" || path.includes("/projects/")) {
    // Projects: the same nav on the grid page AND every project detail page,
    // so you stay oriented. Mirrors the writing sidebar — groups start
    // collapsed; only the group holding the project you're viewing expands (on
    // the "All Projects" grid nothing matches, so everything stays collapsed).
    // Each group is collapsible via its chevron. Only the home link + leaf
    // items can match (section headers point at the grid).
    injectSidebar("/partials/projects-nav.html", aside => {
      markActiveByFilename(aside, "projects.html",
        aside.querySelectorAll(".pub-nav-home, .pub-nav-group li a"));
      wireCollapsibles(aside, true);   // no per-group landing → header toggles in place
    });
  } else if (page === "resume.html") {
    // Resume: single page — in-page scroll-spy TOC.
    injectSidebar("/partials/resume-nav.html", initScrollSpy);
  }
});

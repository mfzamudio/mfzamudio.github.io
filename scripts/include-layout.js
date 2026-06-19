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

  if (path.includes("/publications/")) {
    // Publications: cross-page series nav — mark the current page active by
    // matching its filename, and reveal the series group it belongs to.
    injectSidebar("/partials/publications-nav.html", aside => {
      const here = page || "publications.html";
      aside.querySelectorAll("a").forEach(a => {
        if (a.getAttribute("href").split("/").pop() === here) {
          a.classList.add("active");
          const group = a.closest(".pub-nav-group");
          if (group) group.classList.add("active-group");
        }
      });
    });
  } else if (page === "projects.html") {
    injectSidebar("/partials/projects-nav.html", initScrollSpy);
  } else if (page === "resume.html") {
    injectSidebar("/partials/resume-nav.html", initScrollSpy);
  }
});

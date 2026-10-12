/* site.js — geteiltes Verhalten fuer alle Seiten.
 *
 * Deckt die Bausteine ab, die base.css stylt: Scroll-Schatten der Nav,
 * Sticky-Mobil-CTA, Mobile-Menue-Toggle und die fade-up-Scroll-Animation.
 * Seiten-spezifische Skripte (z. B. Meisterbrief-Lightbox) bleiben inline
 * auf der jeweiligen Seite. Wird mit `defer` eingebunden, laeuft also nach
 * dem Parsen des DOM.
 */
(function () {
    "use strict";

    // Scroll-Schatten der Nav + Sticky-Mobil-CTA (erscheint nach dem Hero).
    var nav = document.getElementById("nav");
    var stickyCta = document.getElementById("stickyCta");
    if (nav || stickyCta) {
        window.addEventListener(
            "scroll",
            function () {
                if (nav) nav.classList.toggle("scrolled", window.scrollY > 20);
                if (stickyCta) {
                    var on = window.scrollY > 700;
                    stickyCta.classList.toggle("show", on);
                    document.body.classList.toggle("sticky-active", on);
                }
            },
            { passive: true }
        );
    }

    // Mobile-Menue-Toggle.
    var navToggle = document.getElementById("navToggle");
    var navLinks = document.getElementById("navLinks");
    if (navToggle && navLinks) {
        navToggle.addEventListener("click", function (e) {
            var open = navLinks.classList.toggle("open");
            e.currentTarget.setAttribute("aria-expanded", open ? "true" : "false");
        });
    }

    // Hinweis auf die englische Fassung (12.10.2026). Nur auf deutschen Seiten, nur wenn
    // KEINE der Browsersprachen Deutsch ist, einmal je Sitzung. Bewusst keine automatische
    // Umleitung: Google rät davon ab, der Crawler kommt selbst mit englischer Einstellung
    // und saehe die deutschen Seiten sonst nicht mehr. Fest positioniert, damit nichts
    // springt (CLS). Ziel ist der Sprachlink der Nav -- er kennt das Gegenstueck.
    var langLink = document.querySelector(".nav-lang");
    if (document.documentElement.lang === "de" && langLink) {
        var sprachen = navigator.languages || [navigator.language || ""];
        var deutsch = false;
        for (var i = 0; i < sprachen.length; i++) {
            if (/^de\b/i.test(sprachen[i])) deutsch = true;
        }
        var gesehen = false;
        try { gesehen = sessionStorage.getItem("lang-hint") === "1"; } catch (e) {}
        if (!deutsch && !gesehen) {
            // Stil hier statt in base.css: leistungen.html und sicherheit.html laden
            // base.css nicht (eigenes CSS), der Hinweis stand dort ungestylt am Seitenende.
            var stil = document.createElement("style");
            stil.textContent =
                ".lang-hint{position:fixed;top:84px;right:24px;z-index:90;display:flex;align-items:center;gap:10px;" +
                "background:#1B2A4A;color:#fff;padding:10px 12px 10px 16px;border-radius:8px;" +
                "box-shadow:0 8px 24px rgba(0,0,0,.2);font-family:'Open Sans',Arial,sans-serif;font-size:.85rem}" +
                ".lang-hint a{color:#fff;font-weight:600;text-decoration:underline;text-underline-offset:3px}" +
                ".lang-hint button{background:none;border:0;color:#fff;font-size:1.3rem;line-height:1;cursor:pointer;padding:4px 6px}" +
                "@media(max-width:680px){.lang-hint{top:80px;left:8px;right:8px;justify-content:space-between}}";
            document.head.appendChild(stil);
            var hint = document.createElement("div");
            hint.className = "lang-hint";
            hint.setAttribute("lang", "en");
            hint.innerHTML = '<a href="' + langLink.getAttribute("href") + '">This page is available in English &rarr;</a>' +
                '<button type="button" aria-label="Close">&times;</button>';
            document.body.appendChild(hint);
            var weg = function () {
                hint.remove();
                try { sessionStorage.setItem("lang-hint", "1"); } catch (e) {}
            };
            hint.querySelector("button").addEventListener("click", weg);
            hint.querySelector("a").addEventListener("click", function () {
                if (window.clarity) window.clarity("event", "lang-hint-en");
                weg();
            });
        }
    }

    // fade-up-Scroll-Animation (No-JS-Fallback: <noscript> zeigt Inhalte sofort).
    var faded = document.querySelectorAll(".fade-up");
    if (faded.length && "IntersectionObserver" in window) {
        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) entry.target.classList.add("visible");
                });
            },
            { threshold: 0.15 }
        );
        faded.forEach(function (el) {
            observer.observe(el);
        });
    }
})();

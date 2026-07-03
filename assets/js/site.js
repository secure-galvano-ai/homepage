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

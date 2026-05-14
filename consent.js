/*
 * Consent-Gate fuer Microsoft Clarity (Opt-in, DSGVO/TKG).
 * Clarity wird ausschliesslich nach aktiver Zustimmung geladen.
 * Entscheidung in localStorage; Widerruf ueber window.resetCookieConsent().
 */
(function () {
    'use strict';

    var STORAGE_KEY = 'cookie-consent';      // 'accepted' | 'rejected'
    var CLARITY_PROJECT_ID = 'wql3vpgrxl';

    function getConsent() {
        try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
    }

    function setConsent(value) {
        try { localStorage.setItem(STORAGE_KEY, value); } catch (e) {}
    }

    // --- Microsoft Clarity laden + Sales-Funnel-Events auf den CTAs setzen ---
    function loadClarity() {
        if (window.clarity) return;
        (function (c, l, a, r, i, t, y) {
            c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
            t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
            y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
        })(window, document, 'clarity', 'script', CLARITY_PROJECT_ID);
        wireFunnelEvents();
    }

    // CTA-Klicks als Clarity-Events: Bookings, WhatsApp, E-Mail
    function wireFunnelEvents() {
        var ctas = [
            { selector: 'a[href*="outlook.office.com/book"]', event: 'cta-erstgespraech' },
            { selector: 'a[href^="https://wa.me/"]', event: 'cta-whatsapp' },
            { selector: 'a[href^="mailto:"]', event: 'cta-email' }
        ];
        ctas.forEach(function (cta) {
            document.querySelectorAll(cta.selector).forEach(function (el) {
                el.addEventListener('click', function () {
                    if (window.clarity) window.clarity('event', cta.event);
                });
            });
        });
    }

    // --- Consent-Banner ---
    function injectStyles() {
        var css = [
            '.consent-banner{position:fixed;left:16px;bottom:16px;z-index:95;max-width:440px;',
            'background:rgba(27,42,74,0.97);color:rgba(255,255,255,0.92);padding:16px 18px;',
            'border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,0.25);',
            "font-family:'Open Sans',Arial,sans-serif;font-size:0.82rem;line-height:1.55;}",
            '.consent-banner p{margin:0 0 12px;}',
            '.consent-banner a{color:#9CC4FF;text-decoration:underline;}',
            '.consent-actions{display:flex;gap:10px;}',
            '.consent-btn{flex:1;border:0;border-radius:6px;padding:8px 14px;',
            'font-family:inherit;font-weight:600;font-size:0.8rem;cursor:pointer;transition:opacity 0.2s;}',
            '.consent-btn:hover{opacity:0.85;}',
            '.consent-accept{background:#3D8C3E;color:#fff;}',
            '.consent-reject{background:rgba(255,255,255,0.15);color:#fff;}',
            '@media(max-width:680px){.consent-banner{left:12px;right:90px;bottom:12px;max-width:none;}}'
        ].join('');
        var style = document.createElement('style');
        style.textContent = css;
        document.head.appendChild(style);
    }

    function showBanner() {
        injectStyles();
        var banner = document.createElement('div');
        banner.className = 'consent-banner';
        banner.setAttribute('role', 'region');
        banner.setAttribute('aria-label', 'Cookie-Zustimmung');
        banner.innerHTML =
            '<p>Wir nutzen <strong>Microsoft Clarity</strong> zur anonymen Analyse der Nutzung ' +
            '(Heatmaps, Klick-Verhalten, Sitzungsaufzeichnungen). Das hilft uns, die Seite zu ' +
            'verbessern. Details: <a href="datenschutz.html">Datenschutz</a>.</p>' +
            '<div class="consent-actions">' +
            '<button type="button" class="consent-btn consent-accept">Akzeptieren</button>' +
            '<button type="button" class="consent-btn consent-reject">Ablehnen</button>' +
            '</div>';
        document.body.appendChild(banner);

        banner.querySelector('.consent-accept').addEventListener('click', function () {
            setConsent('accepted');
            banner.remove();
            loadClarity();
        });
        banner.querySelector('.consent-reject').addEventListener('click', function () {
            setConsent('rejected');
            banner.remove();
        });
    }

    // --- Widerruf: Entscheidung loeschen, Banner erneut zeigen ---
    window.resetCookieConsent = function () {
        try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
        showBanner();
    };

    // --- Init ---
    function init() {
        document.querySelectorAll('.cookie-settings').forEach(function (el) {
            el.addEventListener('click', function (e) {
                e.preventDefault();
                window.resetCookieConsent();
            });
        });

        var consent = getConsent();
        if (consent === 'accepted') {
            loadClarity();
        } else if (consent !== 'rejected') {
            showBanner();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

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
    var funnelVerdrahtet = false;

    function loadClarity() {
        if (!window.clarity) {
            (function (c, l, a, r, i, t, y) {
                c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
                t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
                y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
            })(window, document, 'clarity', 'script', CLARITY_PROJECT_ID);
        }
        // Ausserhalb des window.clarity-Checks: nach "Cookie-Einstellungen -> erneut
        // akzeptieren" ist clarity schon geladen, die Listener waeren sonst nie gesetzt.
        if (!funnelVerdrahtet) {
            funnelVerdrahtet = true;
            wireFunnelEvents();
        }
    }

    // CTA-Klicks als Clarity-Events -- ausschliesslich ueber data-funnel.
    //
    // Frueher liefen hier zusaetzlich drei generische Selektoren
    // (a[href*="outlook.office.com/book"] -> 'cta-erstgespraech', wa.me -> 'cta-whatsapp',
    // mailto: -> 'cta-email'). Weil jeder CTA ohnehin ein data-funnel traegt, feuerte
    // JEDER Klick zwei Events. In der Auswertung sah ein einzelner Buchungsklick dadurch
    // aus wie zwei -- die Zahlen liessen sich weder summieren noch vergleichen.
    // Entfernt am 10.08.2026. Voraussetzung dafuer: alle Buchungs-, Mail- und
    // WhatsApp-Links tragen ein data-funnel. Beim Anlegen neuer CTAs mit pruefen:
    //     grep -o '<a [^>]*\(outlook.office.com/book\|mailto:\|wa.me/\)[^>]*>' *.html | grep -v data-funnel
    function wireFunnelEvents() {
        document.querySelectorAll('[data-funnel]').forEach(function (el) {
            el.addEventListener('click', function () {
                if (window.clarity) window.clarity('event', el.getAttribute('data-funnel'));
            });
        });

        wirePdfDownloads();
        wireVideoInteraktion();
        wireScrollDepth();
    }

    // PDF-Downloads: eigenes Event je Dokument. Die Unternehmenspraesentation ist das
    // staerkste Sales-Asset und war bisher als einziges ungetrackt.
    // Traegt der Link bereits ein data-funnel, ist er oben schon verdrahtet -- sonst
    // entstuenden zwei verschiedene Event-Namen fuer denselben Klick (z. B.
    // 'pdf-musterbefund' aus dem Attribut und 'pdf-standortanalyse-musterbefund' aus
    // dem Dateinamen), die in der Auswertung wie zwei Downloads aussehen.
    function wirePdfDownloads() {
        document.querySelectorAll('a[href$=".pdf"]:not([data-funnel])').forEach(function (el) {
            var name = el.getAttribute('href').split('/').pop().replace(/\.pdf$/, '');
            el.addEventListener('click', function () {
                if (window.clarity) window.clarity('event', 'pdf-' + name);
            });
        });
    }

    // Video-Start ist ueber die YouTube-IFrame-API nur mit einem zusaetzlichen
    // Google-Skript messbar -- das wollen wir dem nocookie-Embed nicht antun.
    // Ersatz ohne Fremd-Request: Klickt jemand in das iframe, verliert das
    // Eltern-Dokument den Fokus und activeElement wird das iframe.
    function wireVideoInteraktion() {
        var video = document.querySelector('iframe[src*="youtube"]');
        if (!video) return;
        var gemeldet = false;
        window.addEventListener('blur', function () {
            if (gemeldet) return;
            if (document.activeElement === video) {
                gemeldet = true;
                if (window.clarity) window.clarity('event', 'video-gestartet');
            }
        });
    }

    // Scroll-Tiefe als Clarity-Events (25/50/75/100 %), einmal pro Marke
    function wireScrollDepth() {
        var marks = [25, 50, 75, 100], hit = {};
        window.addEventListener('scroll', function () {
            var doc = document.documentElement;
            var scrollable = doc.scrollHeight - window.innerHeight;
            if (scrollable <= 0) return;
            var pct = (doc.scrollTop / scrollable) * 100;
            marks.forEach(function (m) {
                if (!hit[m] && pct >= m) {
                    hit[m] = true;
                    if (window.clarity) window.clarity('event', 'scroll-' + m);
                }
            });
        }, { passive: true });
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
            // Mobil bewusst kompakt (31.08.2026): Auf 390x844 lag das Banner genau ueber
            // dem Hero-CTA bei y=705 -- wer es nicht wegklickt, sieht den Hauptknopf nie.
            // Nur Groesse, KEINE Textkuerzung: der Einwilligungstext bleibt wortgleich.
            '@media(max-width:680px){.consent-banner{left:8px;right:76px;bottom:8px;max-width:none;',
            'padding:10px 12px;font-size:0.72rem;line-height:1.4;border-radius:8px;}',
            '.consent-banner p{margin:0 0 8px;}',
            '.consent-actions{gap:8px;}',
            '.consent-btn{padding:7px 10px;font-size:0.72rem;}}'
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

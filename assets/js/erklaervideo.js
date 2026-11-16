// Erklaervideos in den Einstiegskarten (index.html, leistungen.html) — seit 16.11.2026.
//
// Warum es das gibt: Stefan, 16.11.2026: "auf den ersten Blick als Video erkennbar und so
// interaktiv und einfach wie moeglich". Ein Poster mit kleinen nativen Controls las sich wie ein
// Bild. Deshalb: grosser Play-Knopf als Overlay, stumme Vorschau ohne Klick, Klick spielt von vorn
// mit Controls.
//
// Verhalten:
// - Desktop (Hover moeglich): Mouseover spielt stumm ab Sekunde 0, Verlassen pausiert und bringt
//   das Overlay zurueck.
// - Handy (hover: none / pointer: coarse): stumm, sobald der Videobereich zu >= 60 % sichtbar ist,
//   Pause beim Rausscrollen. Beobachtet wird das Video, nicht die ganze Karte — die ist mobil
//   hoeher als der Bildschirm und erreicht 60 % nie.
// - prefers-reduced-motion: keine Vorschau, nur der Knopf.
// - Nie mehr als ein Video gleichzeitig.
// - preload bleibt "none", bis Hover, Sichtbarkeit oder Klick die Datei braucht.
//
// Messung (Clarity, nur wenn nach Einwilligung geladen): Klick-Start 'video-<data-video>' einmal je
// Video und Seitenaufruf (vorher in consent.js wireEigeneVideos, dort entfernt, damit die
// Vorschau nicht als Start zaehlt); Vorschau 'video-vorschau' einmal je Seitenaufruf.
(function () {
    'use strict';
    var boxen = document.querySelectorAll('.ev');
    if (!boxen.length) return;

    var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var grob = window.matchMedia('(hover: none), (pointer: coarse)').matches;
    var vorschauGemeldet = false;

    function melden(name) {
        if (window.clarity) window.clarity('event', name);
    }

    function andereStoppen(aktiv) {
        boxen.forEach(function (b) {
            if (b === aktiv) return;
            var v = b.querySelector('video');
            if (!v.paused) v.pause();
            ruhezustand(b);
        });
    }

    function ruhezustand(box) {
        var v = box.querySelector('video');
        box.classList.remove('vorschau', 'voll');
        v.controls = false;
        v.loop = false;
    }

    function vorschau(box) {
        if (box.classList.contains('voll') || box.classList.contains('vorschau')) return;
        // Ein per Klick laufendes Video hat Vorrang: keine Vorschau daneben, die es beendet.
        var laeuft = false;
        boxen.forEach(function (b) {
            if (b.classList.contains('voll') && !b.querySelector('video').paused) laeuft = true;
        });
        if (laeuft) return;
        var v = box.querySelector('video');
        andereStoppen(box);
        v.preload = 'auto';
        v.muted = true;
        v.loop = true;
        try { v.currentTime = 0; } catch (e) { /* vor dem Laden nicht setzbar, startet ohnehin bei 0 */ }
        box.classList.add('vorschau');
        var p = v.play();
        if (p && p.catch) p.catch(function () { box.classList.remove('vorschau'); });
        if (!vorschauGemeldet) { vorschauGemeldet = true; melden('video-vorschau'); }
    }

    function vorschauEnde(box) {
        if (!box.classList.contains('vorschau')) return;
        box.querySelector('video').pause();
        box.classList.remove('vorschau');
    }

    function abspielen(box) {
        if (box.classList.contains('voll')) return;
        var v = box.querySelector('video');
        andereStoppen(box);
        box.classList.remove('vorschau');
        box.classList.add('voll');
        v.preload = 'auto';
        v.loop = false;
        v.controls = true;
        try { v.currentTime = 0; } catch (e) { /* siehe oben */ }
        v.play();
        if (!box.dataset.gemeldet) {
            box.dataset.gemeldet = '1';
            melden('video-' + v.getAttribute('data-video'));
        }
    }

    boxen.forEach(function (box) {
        var v = box.querySelector('video');
        // Ganzer Bereich klickbar, solange das Overlay bzw. die Vorschau laeuft; danach gehoeren
        // Klicks den nativen Controls.
        box.addEventListener('click', function () { abspielen(box); });
        v.addEventListener('ended', function () { if (box.classList.contains('voll')) ruhezustand(box); });

        if (ruhig) return;
        if (!grob) {
            box.addEventListener('mouseenter', function () { vorschau(box); });
            box.addEventListener('mouseleave', function () { vorschauEnde(box); });
        }
    });

    if (!ruhig && grob && 'IntersectionObserver' in window) {
        var beobachter = new IntersectionObserver(function (eintraege) {
            eintraege.forEach(function (e) {
                if (e.intersectionRatio >= 0.6) vorschau(e.target);
                else if (e.target.classList.contains('voll')) {
                    e.target.querySelector('video').pause();
                } else vorschauEnde(e.target);
            });
        }, { threshold: [0, 0.6] });
        boxen.forEach(function (b) { beobachter.observe(b); });
    }
})();

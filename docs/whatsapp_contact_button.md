# WhatsApp-Kontaktbutton (Homepage)

*Erstellt: 2026-04-23 — Status: offen, wartet auf Business-Nummer*
*Betrifft Repo: `homepage/` (nicht site_A) — Doku hier, weil site_A/docs/ als zentrales Working-Doc-Verzeichnis dient.*

## Ziel

Schwebender WhatsApp-Button unten mittig auf `homepage/index.html`, der Besucher
per Klick direkt in einen WhatsApp-Chat bringt (Desktop-App, Web oder Mobile
je nach Geraet).

## Gewaehlte Variante

**Floating Button, unten mittig** — gruener Kreis mit WhatsApp-Icon, sticky beim
Scrollen, rein HTML/CSS (kein JS, keine externen Libs, keine Tracker).

URL-Format: `https://wa.me/<nummer>?text=<url-encoded-nachricht>`

## Entscheidung: Nummer

Aktueller Stand: Private `+43`-Nummer ist **nicht** auf der Homepage oeffentlich
(geprueft in `index.html`, `impressum.html`, `datenschutz.html` — keine Treffer).

**Entscheidung:** Zweitnummer + WhatsApp Business App — statt Privatnummer.

### Begruendung

- Privatnummer ist heute nicht oeffentlich; Veroeffentlichung = dauerhaft
  (Scraper, Google-Cache, Wayback Machine).
- Keine Trennung Business/Privat (Kunden-Nachrichten am Wochenende auf
  gleicher Nummer wie Familie/Freunde).
- WhatsApp Business bietet Begruessungsnachricht, Abwesenheit,
  Schnellantworten, Labels, Statistiken — nur mit dedizierter Nummer.
- Eine Nummer kann nur in *einer* WhatsApp-App registriert sein
  (normal ODER Business, nicht beides).

## Naechste Schritte

1. **Prepaid-SIM besorgen** (AT-Anbieter: Yesss!, HoT, spusu — ~5–10 €/Monat,
   keine Vertragsbindung, keine Bonitaetspruefung).
2. **WhatsApp Business App** installieren (laeuft parallel zu privatem WhatsApp
   auf demselben Handy).
3. **Business-Profil einrichten:** Name (secure-galvano-ai), Branche, Adresse,
   Website, Begruessungsnachricht, Abwesenheitsnachricht.
4. **Nummer an Claude weitergeben** — Format `43XXXXXXXXXX` (ohne `+`,
   ohne fuehrende `0`, ohne Leerzeichen).
5. **Button implementieren** in `homepage/index.html`:
   - Floating Circle unten mittig (`position: fixed; bottom: 24px;
     left: 50%; transform: translateX(-50%);`)
   - WhatsApp-Gruen (`#25D366`), Hover-Effekt, Responsive
   - Link: `https://wa.me/43XXXXXXXXXX?text=<vorgefuellte-nachricht>`
   - Nur auf `index.html`, nicht auf Impressum/Datenschutz
6. **Nummer ins Impressum** ergaenzen (rechtlich nicht verpflichtend, aber
   erhoeht Vertrauen und SEO).
7. **Live-Test** auf Desktop + Mobile (iOS/Android).

## Vorgefuellte Nachricht (Vorschlag)

> Hallo Stefan, ich interessiere mich fuer secure-galvano-ai und haette ein
> paar Fragen.

Finaler Text noch abzustimmen.

## Implementierungs-Aufwand

- HTML/CSS-Snippet: ~30 Zeilen in `index.html`
- Kein Build-Schritt, keine Dependencies
- Reversibel: Ein Block entfernen/einkommentieren reicht

## Fallback (falls Zweitnummer spaeter)

Falls Zeit draengt: Snippet als auskommentierter Platzhalter in `index.html`
ablegen, ein Aendern der Nummer-Variable aktiviert den Button. So ist die
Code-Struktur vorbereitet, ohne dass die Privatnummer geleakt wird.

# SEO-404 Cleanup (Alt-URLs aus WordPress-Version)

**Stand:** 2026-04-14
**Status:** offen, nicht dringend

## Problem

Google Search Console meldet 404-Fehler fuer alte WordPress-URLs, die auf der neuen statischen Homepage nicht mehr existieren.

**Konkreter Fall (aus Search Console Mail vom 10.04.2026):**
- URL: `https://secure-galvano-ai.com/wp-content/uploads/2025/11/KI-in-der-Galvanotechnik-Call-Pilot-Projekt.pdf`
- Status: 404, letzter Crawl 10.04.2026
- Quelle: Ueberbleibsel der alten WordPress-Installation bei IONOS (Vertrag laeuft 02.06.2026 aus)
- In aktueller `index.html` kein Link mehr darauf (verifiziert per Grep)

## Einordnung

- 404 ist technisch der korrekte Status fuer nicht-existente Seiten
- Kein SEO-Problem, keine Ranking-Auswirkung
- Google dropt solche URLs nach ~4-8 Wochen automatisch aus dem Index
- Meldung in Search Console ist Info, keine Warnung

## To-Do (morgen)

### 1. Bestandsaufnahme
- Search Console oeffnen: <https://search.google.com/search-console>
- **Seitenindexierung → Nicht gefunden (404)** klicken
- Liste aller betroffenen URLs ansehen (nicht nur das eine PDF, wahrscheinlich mehrere WordPress-Altlasten wie `wp-content/`, `?p=123`, `/category/`, `/author/`, alte Seitenpfade)
- Screenshot oder kurze Liste fuer Doku ablegen

### 2. Je nach Anzahl entscheiden

**Wenn < 10 URLs:**
- Fuer jede URL **„Behebung validieren"** klicken
- Google crawlt nochmal, sieht 404, entfernt aus Report
- ~2 Minuten Aufwand pro URL

**Wenn viele URLs (> 10):**
- **Entfernungen → Neuer Antrag → Vorübergehend entfernen** nutzen
- Ganzes Verzeichnis entfernbar: Praefix `https://secure-galvano-ai.com/wp-content/` entfernt alle wp-content-URLs in einem Schritt
- Wirkt nach ~24h, gilt 6 Monate (danach sind sie ohnehin final gedropt)

### 3. Langfrist-Loesung: WordPress abschalten
- IONOS-Vertrag 100185485 laeuft am **02.06.2026** aus → keine Verlaengerung
- Nach Ablauf: alte wp-content-URLs geben definitiv 404 (WordPress-Instanz weg)
- Ggf. vorher schon abschalten wenn sinnvoll

## Nicht tun

- **Keine 301-Redirects bauen** — GitHub Pages kann keine echten Redirects. Meta-Refresh-HTML lohnt sich nur bei wertvollen Backlinks; bei internen Pilot-Projekt-PDFs nicht der Aufwand.
- **Nicht panisch** — das ist Normalbetrieb nach Hosting-Migration, kein Fehler.

## Referenzen

- Aktuelle Sitemap: `homepage/sitemap.xml` (3 URLs: `/`, `/impressum.html`, `/datenschutz.html`)
- DNS: siehe `homepage/README.md` § DNS-Konfiguration
- Hosting-Historie: WordPress bei IONOS → GitHub Pages (statisch) seit 2026-04-07

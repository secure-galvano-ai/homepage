# README — Herleitungen und Erledigtes

*Ausgelagert aus `README.md` am 24.11.2026 — dort stehen Regel, Datum und Anlass, hier die
abgeschlossenen Herleitungen, Messprotokolle und abgelösten Stände. Der Ordner beginnt mit einem
Unterstrich, damit Jekyll ihn nicht auf die Website ausliefert; **nicht nach `docs/` verschieben**,
das wird öffentlich ausgeliefert (`_config.yml`).*

---

## Regeln, die dauerhaft gelten

- **Partner-Logos, Dateigewicht** (22.10.2026): Dateibreite dreifach (480 px), als Palettenbild
  gespeichert — ein Viertel des Gewichts bei gleicher Darstellung (28 → 6 KB).
- **Schriften-Preload, Ergebnis** (24.08.2026): mit Preload und WebP-Portrait CLS 0, Startseite
  997 → 467 KB.
- **Angebote, abgelöst am 03.11.2026:** das **KI-Basis-Setup** (9.900 €, 22.10.–03.11.2026) und die
  **Datenwerkstatt** als Angebot.
- **Kontaktblock im Portraet** (`docs/portrait_galvano_forum_2026.pdf`) trägt „Stefan Maier /
  AT-6960 Buch" *(25.09.2026, direkt im PDF getauscht)*; Original:
  `01_Außenauftritt/02_Veranstaltungen/20260618_Galvano Forum SWISSGALVANIK/01_Anbahnung/`.

## Projektstruktur

- **`leistungen.html`:** seit 31.08.2026 wieder eigene Seite (87 GSC-Impressionen auf
  Weiterleitung, 0 Klicks); seit 03.11.2026 auf die Hälfte gekürzt (Stefan; 4,6 statt
  9,2 Bildschirme).
- **`ethik.html`, Herkunft der Zahlen:** Change-Management-Recherche 26.10.2026 (SharePoint,
  Akquise-Ordner) und BD `archive/ffg-kleinprojekt-eingereicht-2026-09/stand-der-technik.md`
  (Ausbildungsbestand = Bestand, nicht Neuabschlüsse).

## Datenwerkstatt-Seite (`ausbildung.html`)

- **Style-Block** am 11.09.2026 ausgebaut: jede Klasse gegen Rumpf, Generator, JS und `base.css`
  geprüft (rund 10 kB fremde Regeln aus `sicherheit.html`/`leistungen.html`).
- **Hero-Länge, letzte Messung** *(03.11.2026, Playwright-Chromium ohne gespeicherte
  Einwilligung, 390 × 844)*: Hauptknopf endet bei y 577, Banner ab 731 — **154 px Luft**,
  englisch ebenso. Erster Entwurf am 11.09.2026 lag **60 px** darunter.

## Externe Services

- **Bookings-Erstgespräch, Zeiten:** Mo 13–17 / Do 9–14 vom 01.10.2026, abgelöst am 14.11.2026
  durch eigene Zeiten im Dienst.

## Deployment

- **Zombie-Queue, Verlauf 17.08.2026:** Nach einem 503 im `deploy`-Job blieben **zwei** Runs
  (der eigene **und** ein älterer, schon vor dem Push hängender) dauerhaft auf `queued`;
  `gh run cancel` antwortete widersprüchlich mit *„Cannot cancel a workflow run that is
  completed"*. Weder Warten (1,5 h) noch der eine erlaubte `gh run rerun --failed` half — die
  Actions-Runs waren nicht mehr aufzuwecken. Gelöst hat es ein frisch angestoßener Legacy-Build,
  der in gut zwei Minuten durchlief. `githubstatus.com` meldete durchgehend „operational".
- **Deploy-Panne 02.07.2026:** rund 2 h Debugging; Pages meldete `Page build failed`/`errored`,
  die Live-Seite blieb korrekt auf dem letzten guten Stand.

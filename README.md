# secure-galvano-ai Homepage

**Status:** Live auf https://secure-galvano-ai.com
**HTTPS:** Aktiv (GitHub Pages + Let's Encrypt)
**Hosting:** GitHub Pages (kostenlos)
**Stand:** 2026-07-02

---

## Meilensteine

Grundausstattung steht seit Mai 2026: GitHub Pages mit eigener Domain und erzwungenem HTTPS,
Impressum/Datenschutz, Bookings-Termin, Open Graph, `robots.txt`/Sitemap, Search Console,
JSON-LD, self-hosted Fonts, Clarity mit Opt-in-Consent.

| Datum | Umbau | Ergebnis |
|---|---|---|
| 29.05.2026 | Customer-Journey neu geordnet (PAS, 3-Kachel-Onramp, Sticky-Mobil-CTA, Funnel-Tracking) | — |
| 02.07.2026 | **Fokussierung** — `ausbildung.html` + `sicherheit.html` zurueckgestellt, Leistungen 6 → 3 | — |
| 30.07.2026 | **EINE Botschaft** — Sektion `#ablauf` mit der sechsstufigen Vertriebsleiter (ohne Preise), Redundanzen zusammengelegt | 9 → 8 Sektionen, Seitenlaenge −27 % |
| 30.07.2026 | `leistungen.html` aufgeloest, alles auf die Startseite | Sitemap 6 → 5 URLs |
| 10.08.2026 | Presse-/Aktuell-Sektion `#aktuell` nach der Trust-Bar | — |
| 10.08.2026 | **Erster Optimierungslauf** — Messung repariert (jeder CTA war doppelt verdrahtet), zweiter Hero-Button ist jetzt ein Beleg statt eines Sprungankers | Ablauf ab jetzt in [`OPTIMIERUNG.md`](OPTIMIERUNG.md), monatlich per `/optimierung` |
| 17.08.2026 | Presse-Karte verlinkt die frei lesbare WISTO-Fassung | tote Platzhalter weg |

### Regeln, die daraus dauerhaft gelten

- **Presse (`#aktuell`): maximal zwei Karten, veraltete ersetzen statt stapeln.** Eine sichtbar
  veraltete News-Sektion schadet mehr als keine. ⚠ **Die Termin-Karte (KI Days) ist nach dem
  30.09.2026 abgelaufen** und muss dann getauscht werden.
- **Urheberrecht:** nur Kurzzitate mit Quellenangabe. **Keine VN-Fotos, kein VOL.AT-Logo als Bild**,
  kein selbst gehosteter Volltext — Nachdruckrechte liegen bei Russmedia/VN. Der VOL.AT-Artikel
  steht hinter einer Bezahlschranke, deshalb verlinken wir die WISTO-Fassung. Kaeme eine
  Verlagsfreigabe, ersetzt sie diesen Link — nicht stapeln.
- **Zurueckgestellte Seiten reaktivieren:** `ausbildung.html` und `sicherheit.html` existieren
  weiter. Zum Wiederbeleben: Nav-`<li>` einsetzen, Sitemap-Eintrag ergaenzen, `noindex` entfernen.
- **Tracking-Konvention:** je CTA-Position ein eigener Event-Name (`cta-nav`, `cta-hero`,
  `cta-ablauf`, `cta-abschluss`, `cta-sticky`, `cta-whatsapp-fab`, `mail-abschluss`), Downloads als
  `pdf-<dateiname>`. **Keine generischen Selektoren** — die haben die Zahlen einmal verdoppelt.
- **Bei Abweichungen zwischen Website und Angebotsvorlage gilt die Website** *(Stefan, 17.08.2026)*.
  Konkret angewandt: Die Diagnose dauert **„innerhalb einer Woche"**, nicht acht Wochen —
  `BD/areas/business-model.md` wurde am 17.08. an vier Stellen nachgezogen. Der Vor-Ort-Teil steckt
  seit 30.07. in der vorgelagerten **Standortanalyse** (Stufe 2). Preis unveraendert 9.500 €.
- **Produktname bleibt „Diagnose"**, nicht „Proof of Concept" — so in `BD/areas/business-model.md`
  festgelegt.
- **Bewusst getragener Widerspruch, nicht erneut melden** *(Stefan, 11.08.2026)*:
  `docs/portrait_galvano_forum_2026.pdf` sagt „Trusted-AI-**Zertifizierung**" und „Stefan Maier
  **e.U.**" — beides weicht von der Linie ab (korrekt: *Modellpruefung*, Firmierung ohne e.U.).
  Das Heft ist gedruckt; beim naechsten Nachdruck mitkorrigieren.

## Optional (noch offen)

- [ ] Weitere Unterseiten (Trusted AI, Downloads)

---

## Architektur (Single-Source, seit 2026-07-03)

Gemeinsame Bausteine liegen **an genau einer Stelle** und werden nicht mehr pro
Seite dupliziert. Wer Farben, Nav oder Footer aendert, editiert **eine** Quelle:

| Baustein | Single Source | Wird genutzt von |
|----------|---------------|------------------|
| Design-Tokens (Farben) + Reset + Typo + Container + Nav + Buttons + section-header + Footer + WA-FAB + Sticky-CTA + fade-up | `assets/css/base.css` | jede Seite (erstes CSS im `<head>`) |
| Geteiltes Verhalten (Nav-Scroll, Mobile-Menue, fade-up) | `assets/js/site.js` | jede Seite (`defer`) |
| Nav + Footer + WA-FAB + Sticky (HTML) | `_generate_layout.py` -> Marker `<!-- BEGIN/END nav -->` usw. | index, leistungen, ueber-mich, forschung, impressum, datenschutz |
| Leistungs-Karten | `_generate_leistungen.py` -> Marker | leistungen.html |

Die Markenfarben in `base.css :root` sind **kanonisch abgeleitet** aus
`Business Development/areas/brand/corporate_design.md`. Aendern sich Markenfarben,
wird NUR `base.css` editiert. Seiten-spezifisches CSS (Hero, einzelne Sektionen)
bleibt im `<style>`-Block der jeweiligen Seite.

**Nicht migriert (bewusst):** `ausbildung.html` + `sicherheit.html` sind
zurueckgestellt (noindex, nicht in Nav/Sitemap) und tragen weiter ihr eigenes
CSS. Zum Reaktivieren: in `_generate_layout.py` PAGES + NAV_LINKS ergaenzen,
Marker in die Seite setzen, `py _generate_layout.py` laufen lassen.

## Qualitaetssicherung / Self-Check

**Bei groesseren Aenderungen an HTML/CSS/Layout IMMER vor dem Commit/Deploy:**

```bash
cd homepage
py _generate_layout.py          # Nav/Footer/FAB/Sticky aus Single-Source neu rendern
py _scripts/check_site.py        # Self-Check (0 Fehler = grün)
```

`_scripts/check_site.py` ist das "pyright der Homepage" (zero-dependency ausser
tinycss2) und prueft je Seite: HTML wohlgeformt, CSS parst sauber, alle
`var(--token)` aufloesbar, Layout-Marker vorhanden **und in Sync mit dem
Generator**, interne Links/Assets existieren, keine Transliterations-Reste im
Sichttext. Exit 1 bei Fehlern -> nicht deployen.

Optionaler zweiter/dritter Validator (Node, kein Java noetig), als unabhaengiger
Gegencheck bei groesseren Umbauten:

```bash
npx --yes htmlhint *.html
npx --yes html-validate index.html leistungen.html ueber-mich.html forschung.html impressum.html datenschutz.html
```

## Projektstruktur

```
homepage/
  index.html               Predictive-Quality-Landing (ein roter Faden, KEINE Preise): Hero, Gruender-Stimme, Proof (TUeV/8-von-10), Schmerz, 3-Stufen-Treppe Fehlersuche->Live->Frueherkennung (#so-funktionierts), Diagnose-Angebot ohne Preis (#angebot), Kontakt (#kontakt). Traegt KEINE Leistungs-Teaser-Karten mehr.
  leistungen.html          Redirect-Stub auf index.html#ablauf (aufgeloest 2026-07-30, alles auf EINE Seite).
                           Vollstaendige Seite: git show 78ce8c3:leistungen.html
  ausbildung.html          Redirect-Stub auf die Startseite (Praxiskurs = Saeule 2, bis 2027 eingefroren).
                           Kursinhalt reaktivieren: git show feed14a:ausbildung.html
  sicherheit.html          Zurueckgestellt (noindex, nicht in Nav/Sitemap) — ersetzt durch docs/sicherheit-methoden-standards.pdf
  ueber-mich.html          Vollständiges Profil + Bio + Nachweise-Galerie
  nachweise.html           Redirect-Stub auf ueber-mich.html#nachweise (Instant-Meta-Refresh + Canonical, KEIN noindex)
  impressum/ stefan-maier/ kontakt/ trusted-ai/ data-analytics/
                           Redirect-Stubs auf die WordPress-Alt-URLs — generiert aus _generate_redirects.py,
                           nicht von Hand editieren. Nur Pfade mit echtem Nachfolger; tote PDFs bleiben 404.
  impressum.html           Impressum (ECG/UGB) + Marken-Hinweis
  datenschutz.html         Datenschutzerklärung (DSGVO)
  404.html                 GitHub-Pages-Fehlerseite (noindex, nicht in Nav/Sitemap) — faengt Alt-URLs
                           der WordPress-Zeit ab. NUR absolute Pfade (/assets/...), weil Pages die Datei
                           auch fuer tiefe Pfade wie /wp-content/uploads/... ausliefert. Ohne Layout-Marker
                           (Generator erzeugt relative hrefs) und ohne JS.
  assets/
    img/                   Bild-Assets: logo, portrait, aws, trustifai, og-image,
                           techniker-monitoring, stefan-entmetallisierung-2006
    css/
      base.css             SINGLE SOURCE: Tokens + Reset + Typo + Container + Nav + Buttons + section-header + Footer + WA-FAB + Sticky + fade-up (jede Seite bindet es als erstes CSS ein)
      leistungen.css       Geteilte Komponenten-CSS für die Leistungsbausteine (Karten + Mail-Button); genutzt von leistungen.html
    js/
      consent.js           Opt-in-Consent-Gate für Microsoft Clarity + CTA-Funnel-Events
      site.js              Geteiltes Verhalten: Nav-Scroll-Schatten, Mobile-Menue-Toggle, fade-up-Scroll-Animation
  _scripts/
    check_site.py          Self-Check (HTML/CSS/Tokens/Marker-Sync/Links/Transliteration) — vor jedem Deploy laufen lassen
  _generate_layout.py      Generator: Nav + Footer + WA-FAB + Sticky aus einer Quelle in die Marker-Bloecke aller Seiten
  _generate_redirects.py   Generator: Redirect-Stubs fuer WordPress-Alt-URLs (REDIRECTS-Dict = einzige Quelle)
  credentials/
    _generate_credentials.py  Renderer: PDF -> JPG-Thumbs + Full
    thumbs/                Grid-Thumbnails (16 Zertifikate)
    full/                  Lightbox-Originale
  docs/
    sicherheit-methoden-standards.pdf    Corporate-PDF Statement „Datensicherheit & Compliance" (ersetzt sicherheit.html)
    portrait_galvano_forum_2026.pdf      Galvano-Forum-Referenten-Portrait
    praesentation_forschungsvorhaben_2025-07.pdf  Forschungsvorhaben-Präsentation (Stand Juli 2025)
  fonts/
    fonts.css                Self-Hosted @font-face Definitionen (Montserrat + Open Sans, OFL)
    Montserrat-{400,600,700}-{latin,latin-ext}.woff2   6 WOFF2-Files
    OpenSans-{300,400,600}-{latin,latin-ext}.woff2     6 WOFF2-Files
  favicon.ico              Browser-Tab Icon (Root — Browser-Konvention)
  apple-touch-icon.png     iOS Home Screen Icon (Root — Konvention)
  CNAME                    Custom Domain Config
  robots.txt               Crawler-Erlaubnis
  sitemap.xml              Google Sitemap (5 URLs)
  _generate_assets.py      Generator für Favicon/OG-Image (liest/schreibt assets/img/)
  _generate_leistungen.py  STILLGELEGT (Ziel ist nur noch ein Redirect-Stub) — bricht bewusst beim Aufruf ab
  README.md                Diese Datei
```

## Search Console / Indexierung

> Der **monatliche Optimierungslauf** (Clarity + Search Console, Kennzahlen, Entscheidungsregeln,
> Zugaenge) steht in [`OPTIMIERUNG.md`](OPTIMIERUNG.md). Dieser Abschnitt hier deckt nur die
> Indexierungs-Sonderfaelle ab.

Der Bericht **Seitenindexierung** meldet regelmaessig „nicht indexierte Seiten". Die
meisten Eintraege sind **Soll-Zustand**, kein Defekt. Einordnung vor jeder Reaktion:

| Meldung | Ursache | Zu tun |
|---|---|---|
| **Nicht gefunden (404)** | Alt-URLs der WordPress-Installation bei IONOS. Instanz ist mit dem Vertragsende **02.06.2026** weg. Kein Link im Repo zeigt darauf (`check_site.py` prueft das). | Zweiteilen: Alt-URL **mit** heutigem Pendant -> Redirect-Stub in `_generate_redirects.py` eintragen. Alt-URL **ohne** Pendant (tote PDFs, `/wp-*.php`-Bot-Scans) -> nichts tun, 404 ist der korrekte Endzustand. |
| **Durch „noindex"-Tag ausgeschlossen** | `ausbildung.html`, `sicherheit.html` — bewusst zurueckgestellt (Fokussierung 2026-07-02). | Nichts. Reaktivierung siehe Setup-Abschnitt oben. |
| **Alternative Seite mit richtigem kanonischen Tag** | `/index.html` vs. `/` — Canonical zeigt korrekt auf `/`. | Nichts. |
| **Gecrawlt / Gefunden – zurzeit nicht indexiert** | Googles Qualitaets-/Budget-Entscheidung, kein technischer Fehler. Einziger echter SEO-Hebel im Bericht. | Betroffene URL in der URL-Pruefung ansehen, Inhalt schaerfen (eigenstaendiger Text, interne Verlinkung), dann **„Indexierung beantragen"**. Nicht wiederholt beantragen. |

**„Behebung validieren" bei 404 nicht klicken.** GSC validiert nur gegen 200/Redirect.
Solange auch nur eine legitim tote URL in der Gruppe steckt, schlaegt der Lauf
zwangslaeufig fehl — das erklaert den Status „Fehlgeschlagen" vom 25.07.2026, nicht ein
Defekt auf der Seite. Google dropt solche URLs nach ~4–8 Wochen selbst; wer es
beschleunigen will, nimmt `Entfernungen → Neuer Antrag → Praefix` fuer `…/wp-content/`.

**Redirects auf GitHub Pages.** Server-seitige 301 gibt es nicht. Google behandelt den
**Instant-Meta-Refresh** (`content="0; url=…"`) laut Doku als permanenten Redirect und
nennt ihn ausdruecklich als Ersatz, wenn server-seitige Redirects nicht implementierbar
sind. Genau das erzeugt `_generate_redirects.py` — plus `rel=canonical` und einen
sichtbaren Link als No-JS-Fallback.

**Kein `noindex` auf Redirect-Stubs.** `noindex` blockt die URL komplett aus der Suche
und verhindert damit, dass Google den Refresh ueberhaupt als Redirect verarbeitet;
zusammen mit `rel=canonical` sind es widerspruechliche Signale auf derselben URL.
`noindex` gehoert nur auf zurueckgestellte **Inhalts**seiten mit Self-Canonical
(`ausbildung.html`, `sicherheit.html`).

**Sitemap:** `lastmod` beim Deploy auf das tatsaechliche Aenderungsdatum ziehen
(`git log -1 --format=%ad --date=short -- <datei>`) — veraltete Werte kosten Crawl-Prioritaet.

## DNS-Konfiguration (IONOS) — Soll-Stand beider Zonen

**Verifiziert am 17.08.2026 gegen die autoritativen Nameserver.** Diese Tabellen sind die
Wiederherstellungsvorlage: Weicht eine Zone davon ab, ist etwas passiert.

### `secure-galvano-ai.com` (Website, GitHub Pages)

| Typ | Name | Ziel |
|-----|------|------|
| **A** | `@` | `185.199.108.153` |
| **A** | `@` | `185.199.109.153` |
| **A** | `@` | `185.199.110.153` |
| **A** | `@` | `185.199.111.153` |
| **A** | `www` | `185.199.111.153` *(seit 17.08.; vorher CNAME auf `secure-galvano-ai.github.io` — IONOS liess beides nicht gleichzeitig zu, funktional gleichwertig, 301 auf die Hauptdomain)* |
| — | **AAAA** | **keiner.** Ein AAAA auf IONOS bricht HTTPS, siehe Vorfall unten |
| **TXT** | `@` | `v=spf1 -all` |
| **TXT** | `_dmarc` | `v=DMARC1; p=reject;` |

**Spoofing-Schutz seit 17.08.2026:** Von dieser Domain wird **nichts** versendet — alle Kontaktwege
auf der Website sind `mailto:`-Links auf `@rvh.at`, das Hosting ist statisch, es gibt keinen
serverseitigen Mailversand. Deshalb sagen SPF und DMARC hier kompromisslos „niemand darf in meinem
Namen senden", und empfangende Server weisen Fälschungen ab. Der frühere `_dmarc`-CNAME auf
`dmarc.ionos.de` (`p=none`) wurde dafür gelöscht — ein CNAME und ein TXT können nicht auf demselben
Hostnamen stehen. **Muss zurückgedreht werden, falls jemals von `@secure-galvano-ai.com` gesendet
werden soll.** Die MX-Einträge bleiben bewusst stehen; SPF regelt nur den Versand, nicht den Empfang.

### `rvh.at` (Mail, Microsoft 365)

| Typ | Name | Ziel | Prio |
|-----|------|------|------|
| **MX** | `@` | `rvh-at.mail.protection.outlook.com` | **0** |
| **TXT** | `@` | `v=spf1 include:_spf-eu.ionos.com include:spf.protection.outlook.com ~all` | — |
| **TXT** | `_dmarc` | `v=DMARC1; p=none; rua=mailto:dmarc@rvh.at; fo=1` | — |
| **CNAME** | `autodiscover` | `autodiscover.outlook.com` | — |
| **CNAME** | `selector1._domainkey` | `selector1-rvh-at._domainkey.phonixdata.a-v1.dkim.mail.microsoft` | — |
| **CNAME** | `selector2._domainkey` | `selector2-rvh-at._domainkey.phonixdata.a-v1.dkim.mail.microsoft` | — |

DKIM ist seit 17.08.2026 aktiv (`Get-DkimSigningConfig -Identity rvh.at` → `Enabled True`,
`Status Valid`). Versandtest über mail-tester.com am 17.08.2026: **9,5/10**.

**Warum `rvh.at` anders behandelt wird als die Markendomain:** Hier laeuft produktiver Mailverkehr.
Ein hartes `-all` / `p=reject` ohne Belege koennte legitime Mails abweisen — etwa von einem System,
an das gerade niemand denkt. Deshalb steht DMARC bewusst auf `p=none` **mit `rua`**, die Berichte
gehen an das freigegebene Postfach `dmarc@rvh.at` (angelegt 17.08.2026). Eskalationsplan:

| Wann | Schritt |
|---|---|
| erledigt 17.08.2026 | `p=none` + `rua` — sammelt Belege, aendert nichts an der Zustellung |
| nach 2–4 Wochen | Berichte auswerten. Sendet nur Microsoft 365, kann `include:_spf-eu.ionos.com` raus |
| dann | `~all` → `-all` und `p=none` → `p=quarantine` |
| nochmals 2–4 Wochen spaeter | `p=quarantine` → `p=reject` |

Das Schaerfen ist seit dem 17.08. deutlich sicherer, weil DKIM aktiv ist: DMARC gilt schon als
bestanden, wenn **entweder** SPF **oder** DKIM passt. Bei Weiterleitungen bricht SPF regelmaessig,
die DKIM-Signatur ueberlebt sie.

#### Wiedervorlage — Outlook-Serientermin *(angelegt 17.08.2026)*

Erinnernde Aufgabe mit Urteilsbedarf, deshalb Kalendertermin und **kein** Task-Scheduler-Eintrag.
Serie: monatlich am zweiten Montag, **erster Termin 14.09.2026**, endet nach 3 Terminen
(14.09. · 12.10. · 09.11.), Erinnerung 1 Tag vorher. Termintext hier hinterlegt, damit er einen
Kalenderwechsel ueberlebt:

```
Betreff: DMARC rvh.at — Berichte pruefen und naechste Stufe setzen

Berichte liegen im freigegebenen Postfach dmarc@rvh.at (XML-Anhaenge).

SCHRITT 1 — Auswerten
Welche Systeme senden unter rvh.at? Erwartet wird ausschliesslich
Microsoft 365 (spf.protection.outlook.com).
Taucht etwas Unbekanntes auf: NICHT verschaerfen, erst klaeren.

SCHRITT 2 — Nur wenn Schritt 1 sauber ist, im IONOS-DNS setzen:
  TXT @       v=spf1 include:spf.protection.outlook.com -all
              (der IONOS-Include kann raus, wenn nichts darueber sendet)
  TXT _dmarc  v=DMARC1; p=quarantine; rua=mailto:dmarc@rvh.at; fo=1

SCHRITT 3 — Beim uebernaechsten Termin, wenn weiterhin nichts auffaellt:
  TXT _dmarc  v=DMARC1; p=reject; rua=mailto:dmarc@rvh.at; fo=1

PRUEFEN nach jeder Aenderung:
  nslookup -type=TXT rvh.at ns1027.ui-dns.de
  nslookup -type=TXT _dmarc.rvh.at ns1027.ui-dns.de
  Danach eine Testmail ueber mail-tester.com, Ziel weiterhin >= 9/10.

ABBRUCHKRITERIUM: Wenn nach einer Verschaerfung eine legitime Mail
nicht ankommt, sofort eine Stufe zurueck.

Hintergrund und Soll-Konfiguration beider Zonen:
homepage/README.md, Abschnitt DNS-Konfiguration.
```

## IONOS — Vertrag, Zugang, Vorfall *(Stand 17.08.2026)*

**Vertrag:** `100185485` (WordPress Hosting Grow) gekuendigt, am 08.06.2026 per Tarifwechsel in
einen **reinen Domain-Vertrag** ueberfuehrt — keine Grundgebuehr, nur die jaehrliche Domaingebuehr.
Zusatzartikel (Domain Guard, Mail Business, SSL) gekuendigt. `secure-galvano-ai.com` laeuft bis
**15.05.2027** mit **automatischer Verlaengerung**; beide Domains bei IONOS registriert, Nameserver
`ns*.ui-dns.*`. **Zahlungsmethode im Blick behalten** — fehlt sie, scheitert die Verlaengerung lautlos.

### Wenn der Login nicht mehr geht

Am 06.07.2026 wurde die Kontakt-Adresse auf `smaier@rvh.at` umgestellt. Seither meldet ein Login mit
der alten Kennung *„Ihr IONOS Login wurde geloescht"* — **irrefuehrend, sagt nichts ueber den Bestand
der Domains aus.** Weder die Kundennummer aus den ICANN-Mails noch der Domainname `secure-galvano-ai.com`
werden akzeptiert; ueber `rvh.at` kommt man bis zur Identifikation.

**Der Weg, der funktioniert:** telefonisch (**0721 170 555**) eine **„Kontozugangs-Wiederherstellung"**
verlangen — **nicht** die „Umschreibung der Kundennummer", das ist der Prozess fuer einen
Inhaberwechsel und hier falsch. Kein Formular unterschreiben, das nach Inhaberwechsel aussieht.
Identifikationsmerkmale: Vertrag 100185485, Tarifwechsel 08.06.2026, beide Domainnamen,
Kontaktadresse `smaier@rvh.at`. *(Kundennummer steht bewusst nicht im Repo, nur im Postfach.)*

### Der Vorfall — und was daraus folgt

Bei der Wiederherstellung des Zugangs fuehrte IONOS am 17.08. um 15:39–15:45 einen **„Domain-Umzug
innerhalb Ihrer Kundennummer"** durch und setzte dabei **beide Zonen auf Standardwerte zurueck**:
A/AAAA auf die IONOS-Standardseite, MX auf `mx00/mx01.ionos.de`, SPF ohne Outlook-Include,
`autodiscover` auf IONOS, `www`-CNAME ersatzlos weg.

Die Website meldete `ERR_SSL_PROTOCOL_ERROR`, spaeter 404. **Beim Mailverkehr gab es keine sichtbaren
Symptome** — eingehende Post waere still zu IONOS gelaufen, sobald die gecachten MX-Werte ablaufen
(TTL 3600 s). Das ist der gefaehrlichere Teil: Ein kaputtes Zertifikat sieht man, verlorene Antworten
nicht.

**Diagnose, in dieser Reihenfolge:**
1. `nslookup -type=A/AAAA/MX <domain> <autoritativer NS>` — **nicht** ueber den lokalen Resolver
   oder 8.8.8.8; deren Caches verschleiern den Zustand.
2. `curl --resolve <domain>:443:<GitHub-IP> https://<domain>` — trennt DNS- von TLS-Problem.
3. `gh api repos/secure-galvano-ai/homepage/pages` — zeigt, ob GitHub das Zertifikat noch fuehrt.
   Es war durchgehend `approved`; der Fehler lag ausschliesslich im DNS.

**Zwei Fallstricke der IONOS-Maske:** Eintraege tragen eine Spalte `Service` (`Default Site`, `Mail`).
Einzelne Zeilen lassen sich dann nicht aendern — man deaktiviert den **ganzen Dienst**, wodurch alle
zugehoerigen Zeilen verschwinden. Das Entfernen *eines* MX loescht also auch SPF, DMARC, DKIM und
autodiscover; danach alles neu anlegen. Und ein neuer A-Eintrag auf `@` kann einen bestehenden
`www`-CNAME verdraengen — IONOS meldet das im Bestaetigungsdialog, den man lesen muss.

**Nach jeder IONOS-Vertrags- oder Kontoaktion beide Zonen pruefen** (Routine-Check unten). Die
Verlagerung des DNS zu einem eigenen Anbieter wurde **geprueft und verworfen** *(Stefan, 17.08.2026)*:
nicht guenstiger, nicht spuerbar schneller, nicht pflegeleichter (zwei Systeme statt einem). Der
einzige Gewinn waere der Schutz vor genau diesem Reset — und dessen teurer Teil, die zweistuendige
Diagnose, ist mit den Soll-Tabellen oben erledigt. **Neu bewerten, wenn IONOS erneut in die Zone
eingreift**, dann mit einem EU-Anbieter (Hetzner DNS, deSEC) statt Cloudflare.

## Systeme und Abhängigkeiten

Wer hängt woran. Diese Übersicht existiert, weil am 17.08.2026 ein einziger DNS-Vorgang bei IONOS
gleichzeitig Website und Mailempfang lahmgelegt hat — der Zusammenhang war nicht offensichtlich.

| Baustein | Anbieter / Ort | Wichtige Fakten |
|---|---|---|
| **Domain-Registrierung** | IONOS SE | `secure-galvano-ai.com` läuft bis **15.05.2027**, **automatische Verlängerung aktiv**. `rvh.at` ebenfalls bei IONOS. Beide im selben Domain-Vertrag |
| **DNS-Zonen** | IONOS (`ns*.ui-dns.*`) | Beide Zonen. **Einziger Single Point of Failure** — siehe Vorfall oben |
| **Website-Hosting** | GitHub Pages | Repo `secure-galvano-ai/homepage`, Branch `main`, Root. Datei **`CNAME`** im Repo-Root enthält `secure-galvano-ai.com` — **nicht löschen**, sonst verliert Pages die Custom Domain |
| **TLS-Zertifikat** | GitHub Pages (Let's Encrypt) | Automatisch, deckt apex **und** `www`, gültig bis **04.11.2026**, erneuert sich selbst. Status: `gh api repos/secure-galvano-ai/homepage/pages` |
| **Mail** | Microsoft 365, Tenant **PhonixData** | Postfach `smaier@rvh.at`. Absenderadresse aller Geschäfts- und Akquisemails — **bleibt bewusst `@rvh.at`**, obwohl die Marke `secure-galvano-ai.com` lautet *(Entscheidung Stefan, 17.08.2026)* |
| **Terminbuchung** | Microsoft Bookings | Läuft auf dem **rvh.at-Tenant**. Hängt damit am selben Microsoft-365-Konto wie die Mail |
| **Analyse** | Microsoft Clarity | Projekt `wql3vpgrxl`, Opt-in |
| **Indexierung** | Google Search Console | Property auf `secure-galvano-ai.com` — bei DNS-Ausfall meldet sie Crawl-Fehler |

### Was bricht was

| Ursache | Folge | Sichtbar? |
|---|---|---|
| A-Records auf `@` fehlen oder falsch | Website komplett unerreichbar | ja, sofort |
| **AAAA-Eintrag vorhanden** (auf etwas anderes als GitHub) | HTTPS bricht für alle IPv6-Clients, `ERR_SSL_PROTOCOL_ERROR` | ja, aber nur für einen Teil der Besucher — leicht zu übersehen |
| `CNAME`-Datei im Repo gelöscht | Pages verliert Custom Domain, Zertifikat wird ungültig | verzögert |
| **MX von `rvh.at` falsch** | eingehende Mail geht verloren oder landet woanders | **nein** — sieht aus wie „keine Antwort" |
| SPF/DKIM fehlen | ausgehende Mails landen im Spam, DMARC schlägt fehl | nein |
| `autodiscover` falsch | Outlook-Neueinrichtung schlägt fehl, bestehende Clients laufen weiter | verzögert |
| Microsoft-365-Konto gesperrt | Mail **und** Terminbuchung auf der Website gleichzeitig tot | ja |

### Routine-Check

Nach **jeder** Vertrags- oder Kontoänderung bei IONOS beide Zonen gegen die Soll-Tabellen oben
prüfen — und zwar gegen den **autoritativen** Nameserver, nicht über den lokalen Resolver:

```bash
nslookup -type=A   secure-galvano-ai.com ns1093.ui-dns.com
nslookup -type=AAAA secure-galvano-ai.com ns1093.ui-dns.com
nslookup -type=MX  rvh.at ns1027.ui-dns.de
nslookup -type=TXT rvh.at ns1027.ui-dns.de
```

## Corporate Design Assets

| Asset | Pfad |
|-------|------|
| **Logo (groß)** | `brand/logo.png` |
| **Logo (Header)** | `brand/logo_header.png` |
| **Porträt** | Quelle: `Stefan Maier - Dokumente/02_Unterlagen/04_Fotos/MICHAELKREYER/` |
| **Corporate Design Doku** | `brand/corporate_design.md` |
| **Canva Workflow** | `brand/canva_workflow.md` |

### Farben

**Single Source: `assets/css/base.css :root`** (kanonisch aus `corporate_design.md`).
Farbe ändern = nur dort editieren, gilt sofort site-weit. Ad-hoc-Hex im Seiten-CSS
vermeiden — stattdessen Token `var(--name)` nutzen.

| Farbe | Token / Hex | Verwendung |
|-------|-----|------------|
| Schild-Blau | `--schild-blau` `#2B5EA7` | Primär — Headlines, Buttons |
| Dunkelblau | `--dunkelblau` `#1B2A4A` | Hintergründe, Text |
| Logo-Grün | `--logo-gruen` `#3D8C3E` | Akzent — Checkmarks, Erfolg |
| Silber | `--silber` `#D4D8DC` | Trennlinien, dezente Flächen |
| Hellgrau | `--hellgrau` `#F5F7FA` | Sektions-Hintergrund |
| Cyan | `--cyan-akzent` `#00D4FF` | Tech-Akzent (sparsam) |
| (abgeleitet) | `--schild-blau-hover` `--dunkelblau-mid` `--dunkelblau-deep` `--blau-tint` `--text-body` `--text-light` | Hover, Verläufe, Footer-BG, Fließtext |

### Fonts

- **Headlines:** Montserrat (Bold/SemiBold) — **lokal self-hosted** in `fonts/` (OFL-lizenziert)
- **Body:** Open Sans (Regular/Light) — **lokal self-hosted** in `fonts/` (OFL-lizenziert)
- **Fallback:** Arial
- Einbindung in jeder Page über `<link href="fonts/fonts.css" rel="stylesheet">` — kein Google-Fonts-Request, DSGVO-freundlich

## Externe Services

| Service | Zweck | Link |
|---------|-------|------|
| Microsoft 365 | Mail `smaier@rvh.at`, Tenant **PhonixData** | `admin.microsoft.com` · DKIM: `security.microsoft.com` |
| Microsoft Bookings | Erstgespräch buchen — **läuft auf dem rvh.at-Tenant** | `outlook.office.com/book/DatenintegrationKIEntwicklung@rvh.at/` |
| Microsoft Clarity | Web-Analyse (Opt-in, Projekt `wql3vpgrxl`) | `clarity.microsoft.com` |
| Google Search Console | SEO / Indexierung | `search.google.com/search-console` |
| GitHub Pages | Hosting + TLS-Zertifikat | `github.com/secure-galvano-ai/homepage/settings/pages` |
| IONOS | **Domain-Registrar und DNS-Betreiber** — Login über Kundennummer, nicht über die Mailadresse | `my.ionos.de` · Service `0721 170 555` |

> Alle Abhängigkeiten zwischen diesen Diensten stehen im Abschnitt
> [Systeme und Abhängigkeiten](#systeme-und-abh%C3%A4ngigkeiten).

## Deployment

Push auf `main` → GitHub Pages deployed automatisch (~1 Min).

```bash
cd homepage
git add -A
git commit -m "Beschreibung"
git push
```

**KEIN GPG-Signing in diesem Repo.** Die Homepage ist ein reines Content-Repo
(HTML/CSS/Assets) — Commit-Signing ist nur für Code-Repos vorgesehen. Lokal per
`git config commit.gpgsign false` deaktiviert; Commits laufen ohne Yubikey-PIN-Dialog.

### GitHub Pages — bekannte Fallstricke (Anti-Patterns)

*Aus der Deploy-Panne 2026-07-02 gelernt. Symptom war: Pages meldet `Page build failed`/`errored`, die Live-Seite bleibt aber (korrekt) auf dem letzten guten Stand. In ~2 h Debugging stellte sich heraus: **der `build`-Job gelingt praktisch immer — es scheitert nur der `deploy`-Job, und zwar GitHub-seitig.***

1. **Zuerst herausfinden, WAS failt — Build oder Deploy.** Der Legacy-Endpoint `pages/builds/latest` ist laggy/irreführend. Autoritativ ist der Actions-Run:
   ```bash
   RID=$(gh api "repos/secure-galvano-ai/homepage/actions/runs?per_page=1" --jq '.workflow_runs[0].id')
   gh api "repos/secure-galvano-ai/homepage/actions/runs/$RID/jobs" --jq '.jobs[] | "\(.name): \(.conclusion)"'
   gh run view "$RID" --log-failed | tail -30
   ```
   - `deploy` + `Deployment cancelled` → **Concurrency** (Punkt 2).
   - `deploy` + `Timeout reached, aborting!` → **Pages-Backend-Timeout** (GitHub-seitig, transient) → abwarten + EINMAL neu deployen.
2. **NIEMALS mehrere Pages-Deploys schnell hintereinander triggern.** Die Concurrency-Gruppe `pages` hat **Queue-Tiefe 1** — jeder neue Deploy **cancelt den vorher wartenden**. Rapides `git push` + wiederholtes `gh api --method POST .../pages/builds` erzeugt eine Kaskade aus `Deployment cancelled`/`failure`. → **EINMAL pushen, dann 2–10 Min ungestört warten. Nicht nachtreten.**
3. **Bei Fehler zuerst die LIVE-Seite prüfen, nicht blind retrien** (letzter guter Build bleibt live, meist schon korrekt): `curl -s https://secure-galvano-ai.com/ | grep -o '<h1>[^<]*'`
4. **`.nojekyll` NICHT reflexartig hinzufügen.** Der Jekyll-`build` gelingt hier (getestet); `.nojekyll` löst das Deploy-Problem NICHT und liefert zusätzlich `_generate_*.py` **öffentlich** aus (Jekyll schließt `_`-Dateien sonst aus). → **ohne `.nojekyll` bleiben.**
5. **Kein `{{ … }}` / `{% … %}` im HTML** — Jekyll/Liquid parst das und failt den *Build* (war hier NICHT die Ursache, ist aber die klassische echte Build-Bremse).

Assets neu generieren (Favicon, OG-Image):
```bash
cd homepage
py _generate_assets.py
```

Leistungsbausteine ändern/ergänzen (Karten auf `leistungen.html` + Teaser auf `index.html`):
```bash
cd homepage
# 1. Baustein in der LEISTUNGEN-Liste in _generate_leistungen.py bearbeiten
# 2. Neu rendern:
py _generate_leistungen.py
```
**Eine Datenquelle:** die `LEISTUNGEN`-Liste in `_generate_leistungen.py`. Der
Generator schreibt statisches HTML zwischen die `<!-- BEGIN/END leistungen:* -->`
-Marker (crawlbar, kein JS nötig). Das HTML zwischen den Markern **nicht von Hand
bearbeiten** — es wird beim nächsten Lauf überschrieben. Kategorie-Chips (`data-cat`)
sind gesetzt, ein Filter lässt sich später ohne Datenänderung ergänzen.

Nachweise neu rendern (wenn das Quell-PDF aktualisiert wird):
```bash
cd homepage
py credentials/_generate_credentials.py
```
Quelle: `Business Development/resources/credentials/20260512_Lebenslauf & Nachweise_Stefan Maier.pdf`.
Metadaten (Titel, Untertitel, Kategorie pro Seite) sind in `credentials/_generate_credentials.py` definiert — Reihenfolge dort ändern, Seiten 6-28 des PDFs werden zu 23 JPG-Paaren (Seite 28: WKO-Workshop NISG 2026, ergänzt 05/2026).

## WhatsApp-Kontakt

Floating-Button unten rechts auf jeder Page, verlinkt auf `wa.me/4368181483538` mit voreingestelltem Greeting. Funktioniert mit normaler WhatsApp-App **und** WhatsApp Business — keine separate Konfiguration nötig.

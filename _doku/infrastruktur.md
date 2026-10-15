# Domains, DNS, Mail und IONOS

*Ausgelagert aus `README.md` am 15.10.2026 — dort steht nur noch der Verweis. Der Ordner beginnt
mit einem Unterstrich, damit Jekyll ihn nicht auf die Website ausliefert; **nicht nach `docs/`
verschieben**, das wird öffentlich ausgeliefert (`_config.yml`).*

---

## Systeme und Abhängigkeiten

Wer hängt woran. Diese Übersicht existiert, weil am 17.08.2026 ein einziger DNS-Vorgang bei IONOS
gleichzeitig Website und Mailempfang lahmgelegt hat — der Zusammenhang war nicht offensichtlich.

| Baustein | Anbieter / Ort | Wichtige Fakten |
|---|---|---|
| **Domain-Registrierung** | IONOS SE | `secure-galvano-ai.com` läuft bis **15.05.2027**, **automatische Verlängerung aktiv**. `rvh.at` ebenfalls bei IONOS. Beide im selben Domain-Vertrag (§ *IONOS* unten) |
| **DNS-Zonen** | IONOS (`ns*.ui-dns.*`) | Beide Zonen. **Einziger Single Point of Failure** — siehe Vorfall unten |
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

---

## DNS-Konfiguration (IONOS) — Soll-Stand beider Zonen

**Verifiziert gegen die autoritativen Nameserver** (`secure-galvano-ai.com` am 17.08.2026,
`rvh.at` am 21.09.2026). Diese Tabellen sind die Wiederherstellungsvorlage: Weicht eine Zone davon
ab, ist etwas passiert. **Sie taugen nur vollständig** — bis 21.09.2026 fehlten in der
`rvh.at`-Tabelle vier von zehn Einträgen, und beim Wiederaufbau fehlen genau die Lücken, die
niemand vermutet.

### `secure-galvano-ai.com` (Website, GitHub Pages)

| Typ | Name | Ziel |
|-----|------|------|
| **A** | `@` | `185.199.108.153` |
| **A** | `@` | `185.199.109.153` |
| **A** | `@` | `185.199.110.153` |
| **A** | `@` | `185.199.111.153` |
| **A** | `www` | `185.199.111.153` *(A statt CNAME auf `secure-galvano-ai.github.io` — IONOS ließ beides nicht gleichzeitig zu; funktional gleichwertig, 301 auf die Hauptdomain)* |
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
| **TXT** | `@` | `v=spf1 include:spf.protection.outlook.com -all` | — |
| **TXT** | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:dmarc@rvh.at; fo=1` | — |
| **CNAME** | `autodiscover` | `autodiscover.outlook.com` | — |
| **CNAME** | `selector1._domainkey` | `selector1-rvh-at._domainkey.phonixdata.a-v1.dkim.mail.microsoft` | — |
| **CNAME** | `selector2._domainkey` | `selector2-rvh-at._domainkey.phonixdata.a-v1.dkim.mail.microsoft` | — |
| **A** | `@` | `217.160.0.44` (IONOS) — trägt die alte Website | — |
| **AAAA** | `@` | `2001:8d8:100f:f000::200` | — |
| **TXT** | `_dep_ws_mutex` | `662c36c6d49d5b61323ce2e6d3ba421a7ef3…` — IONOS-intern, **Finger weg** | — |
| **CNAME** | `_domainconnect` | `_domainconnect.ionos.com` — IONOS-Einrichtungsautomatik | — |

*Zum AAAA-Eintrag:* Bei der Markendomain ist ein AAAA der Grund für einen HTTPS-Ausfall gewesen
(Vorfall unten), hier steht einer. Er stört aktuell nicht, weil auf `rvh.at` ohnehin kein
Zertifikat liegt und die Seite nur über HTTP antwortet (geprüft 21.09.2026). **Wer hier je
HTTPS aktiviert, prüft zuerst diesen Eintrag** — sonst wiederholt sich der Vorfall.

DKIM ist seit 17.08.2026 aktiv (`Get-DkimSigningConfig -Identity rvh.at` → `Enabled True`,
`Status Valid`). Zustelltest bei mail-tester.com nach der Verschärfung: **10/10**, SpamAssassin
sauber, keine Blocklist.

### Absenderauthentifizierung `rvh.at` — Endstand und Begründung

**Endstand: SPF `-all`, DMARC `p=quarantine`; `p=reject` ist gestrichen** *(Stefan, 01.10.2026)*.
`rvh.at` wird vorsichtiger behandelt als die Markendomain, weil hier produktiver Mailverkehr läuft:
Ein hartes `-all` / `p=reject` ohne Belege könnte legitime Mails eines Systems abweisen, an das
gerade niemand denkt. Deshalb lief DMARC ab 17.08.2026 zuerst auf `p=none` mit `rua` an
`dmarc@rvh.at`, und verschärft wurde erst nach der Auswertung (21.09.2026, Entscheidung Stefan).
**Ohne Belege wird nicht verschärft.**

**Die Belege (21.09.2026): 37 Berichte, 101 gemeldete Nachrichten, kein einziger
Fälschungsversuch.** 94 Nachrichten stammen von Microsoft 365 und bestehen DMARC; die beiden
auffälligen Quellen sind zugeordnet und harmlos:

| Quelle | Nachrichten | Erklärung |
|---|---|---|
| `52.212.19.177` (`eu.cloud-sec-av.com`) | 6 | **Mail-Gateway der Förderstelle aws.at.** An allen drei Berichtstagen war `aws.at` unter den Empfängern. Das Gateway verändert die Mail beim Scannen, deshalb bricht die DKIM-Signatur mit **unserem** Selector `selector1`. |
| `149.72.126.203` (`o48.sg.ascendbywix.com`) | 1 | **Kontaktformular über Wix/SendGrid** beim Empfänger `karrierequer.com` (Google Workspace). DKIM und SPF bestanden — aber für `wixemails.com`, nicht für `rvh.at`. |

**IONOS sendet nichts** — der frühere Include `_spf-eu.ionos.com` tauchte in keinem Bericht auf
und ist raus. Er gab **7 IPv4- und 2 IPv6-Bereiche** von IONOS-Shared-Mailservern frei: Jeder
IONOS-Kunde dort hätte unter `rvh.at` senden und SPF bestehen können. Der SPF verbraucht jetzt
**1 von 10** erlaubten DNS-Lookups.

**Warum nicht `p=reject`:** Die Berichte vom 22.09. bis 30.09.2026 zeigen **jede** Mail an `aws.at`
(vier Stück) über das aws-Gateway mit DKIM und SPF `fail` und `disposition=quarantine` beim
Empfänger. Sie kamen an — die Antworten liegen vor —, aber nur, weil Quarantäne dort Junk heißt;
bei `reject` würden sie abgewiesen. Der Fehler sitzt im Gateway der Förderstelle und ist von hier
nicht zu beheben. **Neu aufgreifen nur, wenn ein Bericht aws-Mails mit `disposition=none` zeigt**
(dann hat aws das Gateway umgestellt). Eine monatliche Wiedervorlage gibt es nicht.
**Restrisiko, bewusst getragen:** Geht doch eine Mail an aws verloren, ist die Gegenmaßnahme eine
Zeile im Panel zurück auf `p=none`. Dass DKIM aktiv ist, macht die Verschärfung sicherer: DMARC
gilt als bestanden, wenn **entweder** SPF **oder** DKIM passt — bei Weiterleitungen bricht SPF
regelmäßig, die DKIM-Signatur überlebt sie.

**Berichte holen und auswerten:** `dmarc_berichte_holen.py` und `dmarc_auswerten.py` in
`Business Development/areas/compliance/scripts/`. Das Holen läuft über MS Graph und braucht
`dmarc@rvh.at` deshalb **nicht** im Outlook-Profil — genau daran scheiterte der erste Termin am
14.09.2026. Voraussetzungen, beide seit 21.09.2026 erfüllt: **Vollzugriff von `smaier@rvh.at` auf
`dmarc@rvh.at`** (hatte gefehlt) und die Zustimmung zu `Mail.Read.Shared` (Token im Cache des
Mailversands). **Neu gesetzte Postfachrechte wirken erst nach Stunden** — Graph meldete eine
Stunde nach dem Setzen noch 404, am Morgen darauf ging es ohne Eingriff. Also erst schlicht
wiederholen, nichts umstellen.

⚠ **Zwei Fallstricke im IONOS-Panel, beide am 21.09.2026 belegt:**

1. **Panel ist `my.ionos.de`** — die `.at`-Varianten (`my.ionos.at`, `login.ionos.at`) existieren
   **nicht**, das Kundenkonto liegt zentral auf `.de`.
2. **IONOS führt SPF und DMARC als getrennte Record-Typen**, obwohl beides TXT ist. Ein Record,
   der als SPF angelegt wurde, nimmt **keinen** DMARC-Wert an: Das Formular antwortet mit „Der
   Wert ist nicht gültig. Ein Fehler wurde im folgenden Teil gefunden: v=DMARC1;" — und zwar
   erst nach dem Speichern, ohne dass die Liste sich ändert. Wer einen Wert in die falsche Zeile
   getragen hat, **löscht den Record und legt ihn über „Record hinzufügen → DMARC (TXT)" neu
   an**; Bearbeiten führt in eine Sackgasse. Anlass: Der DMARC-Wert war versehentlich durch
   einen SPF-Wert ersetzt worden, DMARC war dadurch rund eine Stunde außer Kraft.

Zum Prüfen nach einer DNS-Änderung gegen die autoritativen Nameserver, nicht gegen das Panel:
`nslookup -type=TXT _dmarc.rvh.at ns1093.ui-dns.com` (weitere Befehle im Routine-Check unten).

---

## IONOS — Vertrag, Zugang, Vorfall *(Stand 17.08.2026)*

**Vertrag:** `100185485` (WordPress Hosting Grow) gekündigt, am 08.06.2026 per Tarifwechsel in
einen **reinen Domain-Vertrag** überführt — keine Grundgebühr, nur die jährliche Domaingebühr.
Zusatzartikel (Domain Guard, Mail Business, SSL) gekündigt. `secure-galvano-ai.com` läuft bis
**15.05.2027** mit **automatischer Verlängerung**; beide Domains bei IONOS registriert, Nameserver
`ns*.ui-dns.*`. **Zahlungsmethode im Blick behalten** — fehlt sie, scheitert die Verlängerung lautlos.

### Wenn der Login nicht mehr geht

Am 06.07.2026 wurde die Kontakt-Adresse auf `smaier@rvh.at` umgestellt. Seither meldet ein Login mit
der alten Kennung *„Ihr IONOS Login wurde gelöscht"* — **irreführend, sagt nichts über den Bestand
der Domains aus.** Weder die Kundennummer aus den ICANN-Mails noch der Domainname `secure-galvano-ai.com`
werden akzeptiert; über `rvh.at` kommt man bis zur Identifikation.

**Der Weg, der funktioniert:** telefonisch (**0721 170 555**) eine **„Kontozugangs-Wiederherstellung"**
verlangen — **nicht** die „Umschreibung der Kundennummer", das ist der Prozess für einen
Inhaberwechsel und hier falsch. Kein Formular unterschreiben, das nach Inhaberwechsel aussieht.
Identifikationsmerkmale: Vertrag 100185485, Tarifwechsel 08.06.2026, beide Domainnamen,
Kontaktadresse `smaier@rvh.at`. *(Kundennummer steht bewusst nicht im Repo, nur im Postfach.)*

### Der Vorfall — und was daraus folgt

Bei der Wiederherstellung des Zugangs führte IONOS am 17.08. um 15:39–15:45 einen **„Domain-Umzug
innerhalb Ihrer Kundennummer"** durch und setzte dabei **beide Zonen auf Standardwerte zurück**:
A/AAAA auf die IONOS-Standardseite, MX auf `mx00/mx01.ionos.de`, SPF ohne Outlook-Include,
`autodiscover` auf IONOS, `www`-CNAME ersatzlos weg.

Die Website meldete `ERR_SSL_PROTOCOL_ERROR`, später 404. **Beim Mailverkehr gab es keine sichtbaren
Symptome** — eingehende Post wäre still zu IONOS gelaufen, sobald die gecachten MX-Werte ablaufen
(TTL 3600 s). Das ist der gefährlichere Teil: Ein kaputtes Zertifikat sieht man, verlorene Antworten
nicht.

**Diagnose, in dieser Reihenfolge:**
1. `nslookup -type=A/AAAA/MX <domain> <autoritativer NS>` — **nicht** über den lokalen Resolver
   oder 8.8.8.8; deren Caches verschleiern den Zustand.
2. `curl --resolve <domain>:443:<GitHub-IP> https://<domain>` — trennt DNS- von TLS-Problem.
3. `gh api repos/secure-galvano-ai/homepage/pages` — zeigt, ob GitHub das Zertifikat noch führt.
   Es war durchgehend `approved`; der Fehler lag ausschließlich im DNS.

**Zwei Fallstricke der IONOS-Maske:** Einträge tragen eine Spalte `Service` (`Default Site`, `Mail`).
Einzelne Zeilen lassen sich dann nicht ändern — man deaktiviert den **ganzen Dienst**, wodurch alle
zugehörigen Zeilen verschwinden. Das Entfernen *eines* MX löscht also auch SPF, DMARC, DKIM und
autodiscover; danach alles neu anlegen. Und ein neuer A-Eintrag auf `@` kann einen bestehenden
`www`-CNAME verdrängen — IONOS meldet das im Bestätigungsdialog, den man lesen muss.

**Nach jeder IONOS-Vertrags- oder Kontoaktion beide Zonen prüfen** (Routine-Check unten). Die
Verlagerung des DNS zu einem eigenen Anbieter wurde **geprüft und verworfen** *(Stefan, 17.08.2026)*:
nicht günstiger, nicht spürbar schneller, nicht pflegeleichter (zwei Systeme statt einem). Der
einzige Gewinn wäre der Schutz vor genau diesem Reset — und dessen teurer Teil, die zweistündige
Diagnose, ist mit den Soll-Tabellen oben erledigt. **Neu bewerten, wenn IONOS erneut in die Zone
eingreift**, dann mit einem EU-Anbieter (Hetzner DNS, deSEC) statt Cloudflare.

---

## Routine-Check

Nach **jeder** Vertrags- oder Kontoänderung bei IONOS beide Zonen gegen die Soll-Tabellen oben
prüfen — und zwar gegen den **autoritativen** Nameserver, nicht über den lokalen Resolver:

```bash
nslookup -type=A   secure-galvano-ai.com ns1093.ui-dns.com
nslookup -type=AAAA secure-galvano-ai.com ns1093.ui-dns.com
nslookup -type=MX  rvh.at ns1027.ui-dns.de
nslookup -type=TXT rvh.at ns1027.ui-dns.de
```

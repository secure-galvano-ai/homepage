"""Klicktest gegen die LIVE-Seite — wie ein Besucher, am Bildschirm und am Handy.

Warum es die Datei gibt: `check_site.py` prueft die Dateien vor dem Push und kann prinzipiell
nicht sehen, was live steht (README § Deployment). Nach einem groesseren Umbau (21.10.2026:
Angebotskacheln, Unterlagen je Angebot, englische Seiten ohne deutsche Downloads) wurde derselbe
Test dreimal von Hand zusammengestellt — jetzt ist er ein Befehl.

Was er prueft, je Seite aus `sitemap.xml`:
  * HTTP 200, keine Konsolenfehler, kein seitliches Verrutschen (Bildschirm 1440 px, Handy 390 px)
  * jeden Link: Ziel erreichbar, Sprunganker vorhanden (auch auf der Zielseite)
  * jede Angebotskachel und jede Frage klappt auf
  * jedes eingebettete Video antwortet
  * am Handy: wie viele Bildschirme bis zu den Angeboten (#ablauf) — Kennzahl, kein Fehler

Bekannte Sperren gegen automatische Abrufe (kein Befund): Microsoft Bookings antwortet mit 417,
LinkedIn mit 999. Die Buchungsseiten deshalb nach einer Aenderung von Hand im Browser oeffnen.

    py -X utf8 _scripts/check_live.py              # gegen https://secure-galvano-ai.com
    py -X utf8 _scripts/check_live.py --basis http://127.0.0.1:8000   # gegen einen lokalen Server

Exit 1 bei Befunden. Braucht Python-Playwright mit Chromium (`py -m playwright install chromium`).
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GERAETE = {"Bildschirm": (1440, 900, False), "Handy": (390, 844, True)}
GESPERRT_ERWARTET = {("outlook.office.com/book", 417), ("linkedin.com", 999)}
_status: dict[str, object] = {}


def seiten() -> list[str]:
    pfade = re.findall(r"<loc>https?://[^/]+(/[^<]*)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
    return pfade or ["/"]


def erreichbar(url: str) -> object:
    if url not in _status:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0) Chrome/120"})
            with urllib.request.urlopen(req, timeout=20) as r:
                _status[url] = r.status
        except urllib.error.HTTPError as e:
            _status[url] = e.code
        except Exception as e:  # noqa: BLE001
            _status[url] = type(e).__name__
    return _status[url]


def erwartet_gesperrt(url: str, code: object) -> bool:
    return any(teil in url and code == c for teil, c in GESPERRT_ERWARTET)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--basis", default="https://secure-galvano-ai.com")
    basis = ap.parse_args().basis.rstrip("/")
    from playwright.sync_api import sync_playwright

    befunde: list[str] = []
    kennzahlen: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for geraet, (w, h, mobil) in GERAETE.items():
            ctx = browser.new_context(viewport={"width": w, "height": h}, is_mobile=mobil, has_touch=mobil)
            for pfad in seiten():
                page = ctx.new_page()
                fehler: list[str] = []
                page.on("console", lambda m, f=fehler: f.append(m.text) if m.type == "error" else None)
                page.on("pageerror", lambda e, f=fehler: f.append(str(e)))
                antwort = page.goto(basis + pfad, wait_until="networkidle", timeout=60000)
                if not antwort or antwort.status != 200:
                    befunde.append(f"{geraet} {pfad}: HTTP {antwort.status if antwort else '?'}")
                ueber = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                if ueber > 2:
                    befunde.append(f"{geraet} {pfad}: seitliches Verrutschen um {ueber} px")
                befunde += [f"{geraet} {pfad}: Konsole: {f[:160]}" for f in fehler]
                if mobil and page.evaluate("!!document.getElementById('ablauf')"):
                    top = page.evaluate("document.getElementById('ablauf').getBoundingClientRect().top + scrollY")
                    kennzahlen.append(f"Handy {pfad}: Angebote nach {top / h:.1f} Bildschirmen")
                if not mobil:
                    befunde += _links_und_klicks(page, ctx, basis, pfad)
                page.close()
            ctx.close()
        browser.close()

    for k in kennzahlen:
        print(k)
    print(f"{len(seiten())} Seiten je Geraet geprueft, {len(befunde)} Befunde")
    for b in befunde:
        print(" -", b)
    return 1 if befunde else 0


def _links_und_klicks(page, ctx, basis: str, pfad: str) -> list[str]:
    befunde: list[str] = []
    hier = (basis + pfad).split("#")[0].rstrip("/")
    links = page.evaluate("""() => Array.from(document.querySelectorAll('a[href]')).map(a =>
        ({href: a.href, raw: a.getAttribute('href'), text: (a.innerText || a.title || '').trim().slice(0, 50)}))""")
    for ln in links:
        if ln["raw"].startswith(("mailto:", "tel:", "javascript:")):
            continue
        ziel, _, anker = ln["href"].partition("#")
        if ziel.rstrip("/") == hier:
            if anker and not page.evaluate("a => !!document.getElementById(a)", anker):
                befunde.append(f"{pfad}: Sprunganker fehlt #{anker} ({ln['text']})")
            continue
        code = erreichbar(ziel)
        if code != 200 and not erwartet_gesperrt(ziel, code):
            befunde.append(f"{pfad}: Link {code} -> {ziel} ({ln['text']})")
        if anker and ziel.startswith(basis) and code == 200:
            p2 = ctx.new_page()
            p2.goto(ziel, wait_until="domcontentloaded")
            if not p2.evaluate("a => !!document.getElementById(a)", anker):
                befunde.append(f"{pfad}: Anker fehlt auf der Zielseite {ln['href']} ({ln['text']})")
            p2.close()
    for sel in ("details.angebot-karte > summary", "details.faq-item > summary"):
        knoepfe = page.locator(sel)
        for i in range(knoepfe.count()):
            knoepfe.nth(i).click()
            if not knoepfe.nth(i).evaluate("s => s.parentElement.open"):
                befunde.append(f"{pfad}: {sel.split(' ')[0]} Nr. {i + 1} klappt nicht auf")
            knoepfe.nth(i).click()
    for src in page.evaluate("() => Array.from(document.querySelectorAll('iframe')).map(f => f.src || f.dataset.src || '')"):
        if src and erreichbar(src) != 200:
            befunde.append(f"{pfad}: Video/Einbettung antwortet {erreichbar(src)} -> {src}")
    return befunde


if __name__ == "__main__":
    sys.exit(main())

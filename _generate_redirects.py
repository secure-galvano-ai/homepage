"""Render redirect stubs for the WordPress-era URLs that Google still crawls.

GitHub Pages serves static files only -- no server-side 301. Google documents
the instant `meta refresh` as the supported substitute: "Google Search
interprets instant meta refresh redirects as permanent redirects", and names it
the recommended fallback when server-side redirects are not implementable.
So each old path becomes <old-path>/index.html carrying:

    meta refresh 0  -> the browser moves immediately
    rel=canonical   -> the signal consolidation for Search
    a visible link  -> the documented no-JS/no-refresh fallback

Deliberately NO `noindex` here: noindex "will completely block the page from
Search" and would stop Google from processing the stub as a redirect at all --
canonical and noindex are conflicting signals on the same URL.

Only paths that have a real successor belong in REDIRECTS. Dead PDFs and
bot-scanned /wp-*.php probes stay 404 (correct terminal state, 404.html catches
the user side).

Usage:
    py _generate_redirects.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).parent

# old WordPress path (directory, served as /<key>/) -> (target URL, label)
REDIRECTS = {
    "impressum": ("/impressum.html", "Impressum"),
    "stefan-maier": ("/ueber-mich.html", "Über mich"),
    "kontakt": ("/index.html#kontakt", "Kontakt"),
    "trusted-ai": ("/forschung.html", "Forschung & TÜV-Modellprüfung"),
    "data-analytics": ("/leistungen.html", "Leistungen"),
}

SITE = "https://secure-galvano-ai.com"

TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={target}">
    <link rel="canonical" href="{site}{canonical}">
    <title>{label} — Weiterleitung · secure galvano ai</title>
    <meta name="description" content="Diese Adresse ist umgezogen. Der Inhalt liegt jetzt unter {label}.">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; padding: 60px 24px; text-align: center; color: #1B2A4A; }}
        a {{ color: #2B5EA7; font-weight: 600; }}
    </style>
</head>
<body>
    <p>Diese Adresse ist umgezogen.</p>
    <p><a href="{target}">Weiter zu {label} &rarr;</a></p>
    <script>window.location.replace('{target}');</script>
</body>
</html>
"""


def main() -> None:
    print(f"Rendering {len(REDIRECTS)} redirect stubs...")
    for path, (target, label) in REDIRECTS.items():
        # canonical must not carry a fragment -- Google strips it anyway
        canonical = target.split("#")[0]
        out = ROOT / path / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            TEMPLATE.format(target=target, canonical=canonical, label=label, site=SITE),
            encoding="utf-8",
        )
        print(f"  /{path}/ -> {target}")
    print("Done.")


if __name__ == "__main__":
    main()

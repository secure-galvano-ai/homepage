/* Dienst-Arbeiter fuer den Anlagencheck -- erzeugt von veroeffentlichen.py, nicht von
   Hand aendern.

   Wozu: In der Halle gibt es kein WLAN. Ohne diese Datei kommt ein frischer Aufruf der
   Adresse ohne Netz nicht durch -- gemessen am 26.09.2026 im iPhone-Profil (WebKit), sowohl
   mit frischem als auch mit abgelaufenem Zwischenspeicher. Ein Symbol auf dem
   Startbildschirm waere damit eine Fehlerseite. Mit ihr laeuft das Werkzeug aus dem
   Zwischenspeicher weiter (Messtabelle in docs/AUSLIEFERUNG.md).

   Netz zuerst, Zwischenspeicher darunter -- nicht umgekehrt: Wer Netz hat, bekommt immer
   die aktuelle Fassung. Das ist hier wichtiger als der schnellere Start, weil ein neues
   Passwort eine neue Datei bedeutet: Eine alte Fassung aus dem Speicher wuerde sich mit dem
   alten Passwort oeffnen und niemand wuesste, warum das neue nicht passt.

   LAGER haengt am Inhalt der Seite. Jede Veroeffentlichung hat damit einen eigenen Namen,
   und beim Aktivieren wird jeder andere weggeraeumt. */
"use strict";

const LAGER = "anlagencheck-15b71b3045fe";
const SEITE = "./";

self.addEventListener("install", (e) => {
  e.waitUntil(
    (async () => {
      const lager = await caches.open(LAGER);
      await lager.put(SEITE, await fetch(SEITE, { cache: "reload" }));
      await self.skipWaiting();
    })()
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    (async () => {
      for (const name of await caches.keys()) {
        if (name !== LAGER) await caches.delete(name);
      }
      await self.clients.claim();
    })()
  );
});

self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  /* Ein Aufruf der Adresse mit und ohne "index.html" ist derselbe Aufruf -- deshalb liegt
     jede Navigation unter EINEM Schluessel im Speicher. */
  const schluessel = e.request.mode === "navigate" ? SEITE : e.request;
  e.respondWith(
    (async () => {
      try {
        const antwort = await fetch(e.request);
        if (antwort && antwort.ok) {
          const lager = await caches.open(LAGER);
          await lager.put(schluessel, antwort.clone());
        }
        return antwort;
      } catch (fehler) {
        const treffer = await caches.match(schluessel, { ignoreSearch: true });
        if (treffer) return treffer;
        throw fehler;
      }
    })()
  );
});

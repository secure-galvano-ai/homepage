/* Dienst-Arbeiter der Aufgabenuebersicht -- erzeugt von aufgaben_dashboard.py, nicht von
   Hand aendern.

   Wozu: Ohne diese Datei kommt ein frischer Aufruf der Adresse ohne Netz nicht durch (gemessen
   am 26.09.2026 im iPhone-Profil, siehe lehrmittel/demos/anlagencheck/docs/AUSLIEFERUNG.md).
   Ein Symbol auf dem Startbildschirm waere damit im Funkloch eine Fehlerseite.

   Netz zuerst, Zwischenspeicher darunter -- nicht umgekehrt: Wer Netz hat, bekommt immer den
   aktuellen Stand. Das ist hier der ganze Zweck der Seite; ein schnellerer Start waere ein
   schlechter Tausch gegen eine veraltete Uebersicht.

   LAGER haengt am Inhalt der Seite. Jede Veroeffentlichung hat damit einen eigenen Namen, und
   beim Aktivieren wird jeder andere weggeraeumt -- ein Passwortwechsel kann nicht als alte
   Fassung weiterleben. */
"use strict";

const LAGER = "aufgaben-247bb6b1a164";
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

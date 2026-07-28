// This service worker intentionally does nothing.
// It exists only so previously registered SW can be replaced.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', () => self.clients.claim());

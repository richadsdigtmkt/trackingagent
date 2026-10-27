---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-10-27
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 5
relevancia_alta: 1
tags: [Meta Pixel, consent/privacy, otros, server-side]
---

# Novedades del sector — 2026-10-27

- **Con novedades hoy:** ObservePoint Blog, PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (1)

### Meta Pixel contará más conversiones desde 12 nov; opt-out obligatorio

- **Fuente:** PPC Land · **Area:** Meta Pixel
- **Implicacion:** Meta activa por defecto la recuperación de conversiones en dispositivos cliente para datasets existentes. Revisa cuentas Meta Ads antes del 12 nov para evaluar si desactivas (afecta atribución y billing) y valida con legal/consent si es compatible con tu estrategia de consentimiento.
- **Deja obsoleto:** No directamente, pero la opción 'desactivación automática' de eventos de conversión ya no es viable para nuevos datasets.
- **Enlace:** https://ppc.land/meta-pixel-will-count-more-conversions-from-nov-12-unless-advertisers-opt-out/

## Relevancia media (3)

### SB 690 California: clarificación sobre tracking web y obligaciones reales

- **Fuente:** ObservePoint Blog · **Area:** consent/privacy
- **Implicacion:** SB 690 aclara qué sí y qué no es obligatorio en tracking de California, pero no cambia implementación técnica de GTM/GA4/Pixel. Revisar si el cliente opera en CA para ajustar política de privacidad y consent, no código.
- **Enlace:** https://www.observepoint.com/blog/what-californias-sb-690-means-for-website-tracking-and-what-it-doesnt/

### Safari 27.2 corrige límite de 7 días en cookies CNAME

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** Afecta a server-side tracking con CNAME (ej. subdominios personalizados). Verifica si tus implementaciones de server-side en dominios de primer nivel con CNAME ahora persisten correctamente; si antes compensabas el bug, ajusta la lógica.
- **Deja obsoleto:** Workarounds manuales para extender vida de cookies CNAME en Safari <27.2
- **Enlace:** https://ppc.land/safari-27-2-drops-a-mistaken-7-day-cap-on-cookies-of-cname-hosted-sites/

### Ströer integra Utiq (telco ID) en plataformas programáticas

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Utiq es un identificador consent-based alternativo a cookies third-party en DACH/Europa. Si trabajas con The Trade Desk, Equativ o Active Agent, valida si tus clientes pueden activarlo; afecta a cobertura de audiencias pero sin impacto inmediato en tracking técnico.
- **Enlace:** https://ppc.land/stroers-os-data-solutions-adds-utiq-telco-id-to-audiences-on-3-platforms/

## Relevancia baja (1)

### Amazon prueba chat en tiempo real entre vendedores y compradores

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Feature de UX en Amazon Seller Central, no afecta tracking ni implementación de GTM/GA4/pixels. Monitorear si genera nuevos eventos de conversión a trackear en futuro.
- **Enlace:** https://ppc.land/amazon-tests-real-time-chat-between-sellers-and-shoppers-in-seller-central/

---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-10-18
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 4
relevancia_alta: 1
tags: [consent/privacy, otros]
---

# Novedades del sector — 2026-10-18

- **Con novedades hoy:** PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), ObservePoint Blog, Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (1)

### Google Limited Ads: modo sin cookies para usuarios EU que rechazan TCF

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Google sirve anuncios sin personalización ni cookies de dispositivo cuando usuarios europeos rechazan almacenamiento bajo TCF. Requiere validar que GTM/GA4/Meta Pixel están configurados para respetar este modo y que el Consent Mode está correctamente mapeado (ad_storage: denied).
- **Deja obsoleto:** Implementaciones antiguas de consentimiento que no distinguen entre ad_storage y analytics_storage quedan parcialmente obsoletas; Google ahora fuerza Limited Ads en rechazo explícito de device storage.
- **Enlace:** https://ppc.land/limited-ads/

## Relevancia media (2)

### Google muestra banner de consentimiento fallback si falta TC String

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Verificar que GTM/GA4 envía correctamente el TC String en ad requests para EEA/UK/CH; si falta, Google despliega su propio banner, reduciendo control sobre el flujo de consentimiento. Revisar implementación de Consent Mode y validar string en Network tab.
- **Enlace:** https://ppc.land/fallback-consent-message/

### Global Vendor List: referencia IAB Europe para vendors y propósitos

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** El GVL es el registro oficial que consultan plataformas de consent para validar vendors y purposes declarados. Revisar si tus implementaciones (Consent Mode, CMP) referencia correctamente los vendor IDs y purposes del GVL actual; cambios semanales pueden requerir actualización.
- **Enlace:** https://ppc.land/global-vendor-list/

## Relevancia baja (1)

### Google vende Pixel 9 reacondicionados con descuento en EE.UU.

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Noticia de producto de Google, no afecta implementaciones de tracking, GA4, GTM, Meta Pixel ni consent mode. Sin impacto operativo para consultor de conversion tracking.
- **Enlace:** https://ppc.land/google-adds-refurbished-pixel-9-phones-at-up-to-45-off-in-the-us/

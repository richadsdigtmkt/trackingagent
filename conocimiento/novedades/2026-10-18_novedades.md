---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-10-18
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 4
relevancia_alta: 2
tags: [consent/privacy, otros]
---

# Novedades del sector — 2026-10-18

- **Con novedades hoy:** PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), ObservePoint Blog, Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (2)

### Google CMP muestra banner fallback cuando falta TC String

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Google despliega automáticamente un banner de consentimiento si tu ad request no lleva TC String válido (EEA/UK/CH). Verifica que tu implementación de Consent Mode v2 y CMP genera y envía correctamente el TC String en cada request para evitar fricciones de usuario.
- **Deja obsoleto:** Implementaciones que asumían que la ausencia de TC String no requería manejo automático de Google CMP (fallback implícito ahora activo).
- **Enlace:** https://ppc.land/fallback-consent-message/

### Limited Ads: modo de Google sin cookies cuando usuarios EU rechazan almacenamiento

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Google activa automáticamente Limited Ads cuando usuarios europeos rechazan cookies de dispositivo bajo TCF. Debes verificar que tu Consent Mode v2 está configurado correctamente para señalizar rechazos de storage y que GA4/Meta Pixel funcionan en modo restringido sin identificadores persistentes.
- **Deja obsoleto:** Las implementaciones de Consent Mode v1 que no diferenciaban rechazos de storage son parcialmente obsoletas; v2 es obligatorio para cumplir con Limited Ads.
- **Enlace:** https://ppc.land/limited-ads/

## Relevancia media (1)

### Global Vendor List: registro semanal de vendors IAB Europe

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Asegura que tus vendors de ad tech estén registrados y actualizados en la GVL para que las plataformas de consent los reconozcan. Verifica mensualmente que tus partners (GA4, Meta Pixel server-side, etc.) aparezcan con purposes correctos.
- **Enlace:** https://ppc.land/global-vendor-list/

## Relevancia baja (1)

### Google vende Pixel 9 reacondicionados con descuento en EE.UU.

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Noticia de producto de hardware sin impacto en tracking, GA4, GTM o consent. No requiere acción.
- **Enlace:** https://ppc.land/google-adds-refurbished-pixel-9-phones-at-up-to-45-off-in-the-us/

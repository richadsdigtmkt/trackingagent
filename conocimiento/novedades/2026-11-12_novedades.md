---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-11-12
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 9
relevancia_alta: 3
tags: [GA4, consent/privacy, otros, server-side]
---

# Novedades del sector — 2026-11-12

- **Con novedades hoy:** PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), ObservePoint Blog, Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (3)

### Google Ads tags exponen IPs completas desde 11 ene sin acción en sGTM

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** Los tags de Google Ads (DV360, SA360, CM360) enviarán IPs sin enmascarar a menos que implementes consent mode en sGTM antes del 11 de enero. Acción: revisar containers server-side y activar IP masking condicional al consentimiento.
- **Deja obsoleto:** El enmascaramiento automático de IPs en Google Ads sin consent mode explícito queda obsoleto; ahora es responsabilidad del propietario del sGTM garantizar que los tags respeten el estado de consentimiento.
- **Enlace:** https://ppc.land/google-ad-tags-gain-full-ips-on-january-11-unless-sgtm-owners-build-a-fix-2/

### Google Ads tags enviarán IPs completas desde 11 ene si no configuras sGTM

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** A partir del 11 de enero, Google Ads, DV360, SA360 y CM360 enviarán direcciones IP completas por defecto en sGTM. Debes implementar consent mode o bloqueos en sGTM para enmascarar el último octeto si aplica RGPD/LSSI; verifica tu Consent Mode v2 y ajusta consent decision logic en GTM.
- **Deja obsoleto:** El método anterior de confiar en el opt-out automático de Google para ofuscación de IPs en estos tags deja de funcionar; ahora requiere configuración explícita en sGTM.
- **Enlace:** https://ppc.land/google-ad-tags-gain-full-ips-on-january-11-unless-sgtm-owners-build-a-fix/

### EDPB cierra puerta a tracking cross-site por interés legítimo

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** El EDPB rechaza tracking cross-site bajo 'interés legítimo' en DACH/España/UK: obliga a requerir consentimiento explícito o cesar esta práctica. Revisar inmediatamente implementaciones que se apoyan en LI para perfilar entre sitios.
- **Deja obsoleto:** Queda obsoleta la estrategia de justificar cross-site tracking (sin consentimiento previo) basándose únicamente en 'interés legítimo' del anunciante.
- **Enlace:** https://ppc.land/cross-site-ad-tracking-will-rarely-pass-legitimate-interest-test-edpb-says/

## Relevancia media (1)

### Google Ads oculta uplift de datos propios si no supera 1%

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Google ahora solo muestra el impacto de first-party data en Google Ads cuando mejora resultados >1%. Relevante para auditar reporting de campañas y calibrar expectativas de attribution lift, pero no cambia implementación técnica de tracking.
- **Enlace:** https://ppc.land/google-ads-shows-its-first-party-data-uplift-only-when-it-tops-1/

## Relevancia baja (5)

### India: retraso en designación de miembros de junta de datos

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** India aún no ha designado miembros de su junta reguladora de datos (1 año después), aunque el registro de consent managers comienza nov 2026. No afecta operaciones en DACH/España/UK; monitorear solo si tienes clientes con tráfico indio significativo.
- **Enlace:** https://ppc.land/a-year-after-india-fixed-its-data-board-at-4-members-none-are-appointed/

### IAB define estándar de 'views' para creadores; impacto indirecto en tracking

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Este estándar es para la industria de creadores y medición de contenido, no afecta directamente implementaciones de GA4, GTM, Meta Pixel o server-side. Monitorear si genera cambios en cómo plataformas reportan métricas de video/contenido.
- **Enlace:** https://ppc.land/iab-moves-to-define-creator-views-as-66-ask-for-a-common-standard/

### Google Ads Developer Blog migra a nuevo feed; cambio administrativo

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Solo afecta si suscrives a notificaciones de cambios en Google Ads API. Actualiza tu fuente RSS al nuevo feed si dependes de esas actualizaciones para tracking/conversiones.
- **Enlace:** https://ppc.land/googles-old-ads-developer-blog-feed-gets-no-new-posts-after-november-10/

### Gemini integra apps de comida y transporte en 3 países (beta)

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Ampliación de capacidades de Gemini AI en dispositivos móviles específicos. No afecta infraestructura de tracking (GTM, GA4, pixels) ni consent/privacy compliance en mercados DACH/UK principal.
- **Enlace:** https://ppc.land/googles-gemini-can-now-use-food-and-ride-apps-for-people-in-3-more-countries/

### TikTok añade mediciones de calidad Zefr en TopView y CapCut

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** TikTok expande verificación de calidad de anuncios con Zefr en formatos TopView y CapCut. Relevante solo si gestionas campañas en TikTok ads; no afecta tracking server-side, GA4 o consent mode.
- **Enlace:** https://ppc.land/capcut-and-tiktok-topview-ads-gain-4-zefr-ad-quality-measurements/

---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-11-12
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 8
relevancia_alta: 2
tags: [Meta Pixel, consent/privacy, otros, server-side]
---

# Novedades del sector — 2026-11-12

- **Con novedades hoy:** PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), ObservePoint Blog, Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (2)

### Google Ads tags enviarán IPs completas desde 11-ene sin acción en sGTM

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** Los tags de Google Ads (Ads, DV360, SA360, CM360) en sGTM enviarán direcciones IP sin anonimizar a menos que implementes un opt-out explícito antes del 11 de enero. Requiere revisar tu sGTM y aplicar el bloqueo de consentimiento si aún no lo has hecho.
- **Deja obsoleto:** La práctica de confiar en la anonimización automática de IPs en Google Ads tags sin consentimiento explícito queda obsoleta.
- **Enlace:** https://ppc.land/google-ad-tags-gain-full-ips-on-january-11-unless-sgtm-owners-build-a-fix/

### EDPB: cross-site tracking raramente cumple interés legítimo

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** El EDPB (autoridad de privacidad de la UE) cierra la puerta al tracking cross-site bajo base legal de interés legítimo. Afecta DACH y España: revisar inmediatamente consentimiento explícito en pixel configs y server-side tracking; el interés legítimo ya no es viable como fallback.
- **Deja obsoleto:** Implementaciones de tracking cross-site basadas en interés legítimo (sin consentimiento explícito) quedan obsoletas en mercados GDPR.
- **Enlace:** https://ppc.land/cross-site-ad-tracking-will-rarely-pass-legitimate-interest-test-edpb-says/

## Relevancia media (1)

### Google Ads solo muestra uplift de first-party data si supera 1%

- **Fuente:** PPC Land · **Area:** Meta Pixel
- **Implicacion:** Google cambió el umbral de visibilidad para métricas de first-party data en Ads: requiere 100 conversiones en 14 días y excluye enhanced conversions. Revisa si tus cuentas cumplen el umbral para confiar en estos reportes.
- **Enlace:** https://ppc.land/google-ads-shows-its-first-party-data-uplift-only-when-it-tops-1/

## Relevancia baja (5)

### India: retraso en implementación de Data Board, sin impacto en DACH/UK/Spain

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Afecta solo a operadores en India. Los mercados DACH, España y UK no dependen de esta regulación. Monitorear si hay cambios futuros en estándares globales, pero sin acción inmediata.
- **Enlace:** https://ppc.land/a-year-after-india-fixed-its-data-board-at-4-members-none-are-appointed/

### IAB busca estandar para medir 'views' en contenido de creadores

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Iniciativa de la IAB para definir metricas comunes en creator economy. No impacta implementacion actual de tracking en GTM, GA4 o Meta Pixel; espera actualizaciones 2027.
- **Enlace:** https://ppc.land/iab-moves-to-define-creator-views-as-66-ask-for-a-common-standard/

### Google Ads Developer Blog migra a nuevo feed; cambio de suscripción

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Es una reorganización administrativa de canales de comunicación de Google Ads API, no un cambio funcional de tracking o implementation. Relevante solo si monitoreas activamente cambios en Google Ads API; actualiza tu feed de suscripción si lo haces.
- **Enlace:** https://ppc.land/googles-old-ads-developer-blog-feed-gets-no-new-posts-after-november-10/

### Gemini integra apps de food/ride en UK, India, Japón (beta)

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Expansión de capacidades de IA en Gemini para interacción con apps. Sin impacto directo en tracking, consent mode o medición de conversiones en GTM/GA4/Pixel.
- **Enlace:** https://ppc.land/googles-gemini-can-now-use-food-and-ride-apps-for-people-in-3-more-countries/

### TikTok/CapCut integran mediciones Zefr de calidad de anuncios

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Noticia sobre expansión de verificación de anuncios en TikTok/CapCut con Zefr. Relevante solo si gestionas campañas en esas plataformas; sin fechas ni mercados específicos DACH/ES/UK, es información incompleta.
- **Enlace:** https://ppc.land/capcut-and-tiktok-topview-ads-gain-4-zefr-ad-quality-measurements/

---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-11-13
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 8
relevancia_alta: 2
tags: [GA4, consent/privacy, otros, server-side]
---

# Novedades del sector — 2026-11-13

- **Con novedades hoy:** PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), ObservePoint Blog, Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (2)

### Google Ads tags exponen IPs completas desde 11 ene si no hay fix en sGTM

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** Los tags de Google Ads (DV360, SA360, CM360) enviarán IPs sin anonimizar a menos que se implemente un fix en server-side GTM antes del 11 de enero. Requiere acción inmediata en implementaciones sGTM con consent mode activo.
- **Deja obsoleto:** El anonimizado automático de IPs en client-side tags de Google Ads para estos productos queda obsoleto; ahora depende de lógica custom en sGTM.
- **Enlace:** https://ppc.land/google-ad-tags-gain-full-ips-on-january-11-unless-sgtm-owners-build-a-fix-2/

### Google Ads tags envían IPs completas desde 11 ene a menos que sGTM implemente fix

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** A partir del 11 de enero, los tags de Google Ads (Ads, DV360, SA360, CM360) en sGTM enviarán direcciones IP completas si no hay consentimiento explícito de opt-out. Debe revisar implementación de consent mode en sGTM y aplicar la solución de Google para anonimizar el último octeto IPv4.
- **Deja obsoleto:** El flujo anterior de consent mode en sGTM (sin configuración específica de full IP) queda obsoleto; requiere actualización a nueva lógica de Google.
- **Enlace:** https://ppc.land/google-ad-tags-gain-full-ips-on-january-11-unless-sgtm-owners-build-a-fix/

## Relevancia media (1)

### Google confirma: Analytics no coincidirá con Search Console clicks

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Las discrepancias entre GA4 y Search Console son estructurales, no errores. Comunicar a clientes que no deben esperar matching exacto entre plataformas; documentar en auditorías para evitar falsas alarmas.
- **Enlace:** https://ppc.land/google-explains-why-analytics-wont-match-search-console-click-counts/

## Relevancia baja (5)

### Conversion path: definición y concepto básico

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Es un artículo educativo que explica qué es un conversion path (secuencia de interacciones antes de conversión). Útil como referencia teórica pero no introduce cambios en plataformas ni políticas que requieran acción inmediata.
- **Enlace:** https://ppc.land/conversion-path/

### Data-driven attribution: método estadístico de reparto de crédito

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Es un concepto general de atribución (no un cambio de plataforma). Útil para contexto, pero no obliga a cambios inmediatos en implementación de tracking.
- **Enlace:** https://ppc.land/data-driven-attribution/

### Analytics 360: tier enterprise de GA con mayores límites y datos sin muestreo

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Información de producto existente (GA360 lleva años disponible). Relevante solo si el cliente está evaluando upgrade desde GA4 estándar por volumen de datos o SLAs. No requiere acción inmediata.
- **Enlace:** https://ppc.land/analytics-360/

### Google Marketing Platform: resumen de suite empresarial

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Contenido informativo sobre la arquitectura de herramientas de Google (DV360, SA360, CM360, GA360). No implica cambio de política o implementación inmediata en tracking.
- **Enlace:** https://ppc.land/google-marketing-platform/

### India: retraso en constitución de junta de protección de datos

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Afecta solo si opera en India; el retraso en la aprobación de consent managers (Rule 4) puede ralentizar implementaciones locales. Monitorear si se cumple plazo de diciembre 2026.
- **Enlace:** https://ppc.land/a-year-after-india-fixed-its-data-board-at-4-members-none-are-appointed/

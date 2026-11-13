---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-11-13
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 9
relevancia_alta: 3
tags: [GA4, consent/privacy, otros, server-side]
---

# Novedades del sector — 2026-11-13

- **Con novedades hoy:** PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), ObservePoint Blog, Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (3)

### Google Ads tags revelan IPs completas desde enero 11 sin consent

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** Si usas sGTM con tags de Google Ads/DV360/SA360/CM360, debes implementar lógica de consent ANTES del 11/01 para enmascarar el último octeto IPv4 en territorios con restricciones (DACH, España, UK). Sin acción, transmites IPs completas incumpliendo GDPR/RGPD.
- **Deja obsoleto:** Implementaciones de sGTM que asumen enmascaramiento automático de IPs en Ads tags quedan obsoletas; ahora requieren consent mode explícito o template personalizado para bloquear/modificar requests.
- **Enlace:** https://ppc.land/google-ad-tags-gain-full-ips-on-january-11-unless-sgtm-owners-build-a-fix-2/

### Google Ads tags expondrán IPs completas desde 11 ene si no configuras sGTM

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** A partir de enero, los tags de Google Ads (DV360, SA360, CM360) enviarán IPs completas a menos que implementes una solución en sGTM. Debes revisar tu arquitectura de consent mode y agregar lógica de enmascaramiento de IP en el servidor antes de esa fecha.
- **Deja obsoleto:** El enfoque tradicional de confiar solo en el consentimiento del lado del cliente para proteger IPs en Ads tags quedará insuficiente.
- **Enlace:** https://ppc.land/google-ad-tags-gain-full-ips-on-january-11-unless-sgtm-owners-build-a-fix/

### EDPB: tracking cross-site por interés legítimo raramente válido

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** El EDPB (noviembre 2024) restringe drásticamente el uso de 'legitimate interest' para tracking multiplataforma en DACH/España/UK. Revisar inmediatamente consentimiento vs. legitimidad en implementaciones GA4, Meta Pixel y server-side; probablemente necesitarás consentimiento explícito donde antes usabas LI.
- **Deja obsoleto:** Implementaciones que confían en 'legitimate interest' para cross-site profiling sin consentimiento quedan obsoletas.
- **Enlace:** https://ppc.land/cross-site-ad-tracking-will-rarely-pass-legitimate-interest-test-edpb-says/

## Relevancia media (3)

### Data-driven attribution: modelo estadístico para asignación de crédito

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Método complementario a GA4 attribution models para entender contribución real de cada touchpoint. Útil si auditas rendimiento de campañas multi-canal, pero no cambia implementación de tracking ni consent.
- **Enlace:** https://ppc.land/data-driven-attribution/

### Google: Analytics no coincidirá con Search Console por datos de referrer limitados

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Los clics de Google Search, Discover e Images llegan a Analytics sin query string, solo dominio. Revisar dashboards de reconciliación y ajustar expectativas de matching con Search Console.
- **Enlace:** https://ppc.land/google-explains-why-analytics-wont-match-search-console-click-counts/

### Google Ads solo muestra uplift de datos propios si supera 1%

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Google ahora restringe la visualización de mejoras por datos first-party a casos donde el uplift supera 1%, requiriendo 100 conversiones en 14 días. Verificar en tus cuentas GA4+Google Ads si las conversiones enhanced llegan a este umbral para ver datos reales de mejora.
- **Enlace:** https://ppc.land/google-ads-shows-its-first-party-data-uplift-only-when-it-tops-1/

## Relevancia baja (3)

### Analytics 360: tier empresarial de GA con límites altos y datos sin muestreo

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Información de producto Google Analytics 360 (versión enterprise). Solo relevante si cliente tiene volumen muy alto (>10M hits/mes) o necesita datos sin muestreo; no cambia estrategia de tracking ni consent.
- **Enlace:** https://ppc.land/analytics-360/

### Google Marketing Platform: suite enterprise de compra y medición de ads

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Información descriptiva de la arquitectura de productos Google para agencias enterprise. No introduce cambios de política ni obliga a modificar implementaciones actuales de tracking.
- **Enlace:** https://ppc.land/google-marketing-platform/

### India: retraso en designación de miembros de Data Board; impacto futuro en CMs

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Afecta solo si trabajas con clientes en India. La ausencia de junta retrasará aprobaciones de consent managers desde nov 2026, pero aún hay margen. No requiere acción inmediata en DACH/España/UK.
- **Enlace:** https://ppc.land/a-year-after-india-fixed-its-data-board-at-4-members-none-are-appointed/

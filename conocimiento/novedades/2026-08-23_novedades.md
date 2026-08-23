---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-08-23
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 6
relevancia_alta: 1
tags: [GA4, GTM, consent/privacy, otros]
---

# Novedades del sector — 2026-08-23

- **Con novedades hoy:** PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), ObservePoint Blog, Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (1)

### Google Ads ignora conversiones offline subidas tras 7 días en atribución

- **Fuente:** PPC Land · **Area:** GTM
- **Implicacion:** Las conversiones offline cargadas después de 7 días no se incluyen en modelos de atribución, aunque sí en reportes estándar. Requiere revisar SLAs de carga de datos offline y ajustar ventanas de análisis en modelos de atribución si usas este tipo de datos.
- **Deja obsoleto:** Prácticas que asumen paridad total entre conversiones estándar y atribuidas para offline data quedan obsoletas.
- **Enlace:** https://ppc.land/google-ads-attribution-ignores-offline-conversions-uploaded-after-7-days/

## Relevancia media (4)

### Controles de puja reducen; medición de anuncios afectada (Google, Microsoft)

- **Fuente:** PPC Land · **Area:** GA4
- **Implicacion:** Monitorizar cambios en Google Ads y Microsoft Advertising que limitan opciones de puja y medición. Revisar dashboards de GA4 y Meta para validar integridad de datos de conversión.
- **Enlace:** https://ppc.land/bid-controls-shrink-as-ad-measurement-breaks-week-of-august-17/

### Visual tagging de Google: limitado a conversiones purchase, sin gtag config

- **Fuente:** PPC Land · **Area:** GTM
- **Implicacion:** El visual tagging beta de Google Ads solo cubre casos simples (70-80%) y está restringido a purchase conversions. Útil para implementaciones rápidas pero insuficiente para tracking complejo; requiere gtag manual para casos avanzados.
- **Enlace:** https://ppc.land/googles-visual-tagging-covers-the-easy-70-to-80-of-cases-zambon-says/

### Google Shopping rechazará imágenes <500x500px desde enero 2027

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Afecta a feeds de productos en Google Shopping/Merchant Center, no a tracking directo. Audita ahora tamaños en clientes e-commerce; prepara revalidación de feeds antes de enero 2027 para evitar desaprobaciones.
- **Enlace:** https://ppc.land/google-blocks-product-images-under-500-x-500-pixels-from-31-january-2027/

### ID5: alternativa de identificación universal sin cookies de terceros

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Conocer ID5 como solución de identity graph post-cookies es relevante para contextos de consent mode y server-side tracking. Evaluar si aplica en estrategias DACH/España/UK según requisitos de privacidad local, pero no es cambio de plataforma que obligue a implementar.
- **Enlace:** https://ppc.land/explaining-id5/

## Relevancia baja (1)

### 72% de compradores eliminan apps retail tras primer uso

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Dato de comportamiento consumer sobre retención de apps, relevante para estrategia de marketing pero no afecta implementación técnica de tracking. Informativo para contexto de campañas, sin cambios operacionales en GTM/GA4/pixels.
- **Enlace:** https://ppc.land/adobe-finds-72-of-shoppers-delete-retail-apps-after-one-use/

---
tema: conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)
fecha: 2026-10-17
fuentes_escaneadas: 5
fuentes_caidas: 0
novedades: 9
relevancia_alta: 1
tags: [QA, consent/privacy, otros, server-side]
---

# Novedades del sector — 2026-10-17

- **Con novedades hoy:** ObservePoint Blog, PPC Land
- **Leidas sin novedades (OK, sin publicaciones en la ventana):** Simo Ahava, David Vallejo (Thyngster), Google Analytics Blog
- **Caidas / no leidas (revisar URL si persiste):** ninguna

## Relevancia alta (1)

### Safari limita cookies server-set a 7 días en subdominios de tracking enmascarados

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** Afecta directamente server-side tracking: Safari ahora degrada cookies en subdominios de tracking que no compartan suficientes bits IPv4 con el dominio principal. Requiere revisar arquitectura de dominios de tracking y considerar migrar a paths en lugar de subdominio separado.
- **Deja obsoleto:** Implementaciones de server-side tracking con subdominio dedicado (ej. tracking.tudominio.com) pierden persistencia en Safari; la práctica de usar subdominio separado para tracking primera-parte queda parcialmente obsoleta.
- **Enlace:** https://ppc.land/safari-cuts-server-set-cookies-to-7-days-on-cloaked-tracking-subdomains/

## Relevancia media (5)

### Floodlight integra datos de usuarios autenticados para recuperar conversiones

- **Fuente:** PPC Land · **Area:** server-side
- **Implicacion:** Google amplia Floodlight en DV360/SA360/CM360 usando datos de usuarios en sesión para atribuir conversiones previamente no contabilizadas. Revisa si tus cuentas en estas plataformas pueden beneficiarse; espera fluctuaciones en recuentos de conversión al activarse.
- **Enlace:** https://ppc.land/floodlight-gains-google-signed-in-data-to-recover-unattributed-conversions/

### Investigación: agentes IA desafían marcos de consentimiento actuales

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Documento académico que anticipa fricciones futuras entre automatización IA y regulación de consentimiento (GDPR, ePrivacy). Monitorea evolución de normas pero no requiere acción inmediata en implementaciones actuales.
- **Enlace:** https://ppc.land/consent-cant-keep-up-with-ai-agents-65-google-led-researchers-argue/

### Solo 7% ceden datos a IA voluntariamente; Germany 24% reluctante

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Datos de consentimiento por mercado (DACH vs UK/US) para calibrar expectativas en estrategias de consent mode y audiences. Monitorea si tus tasas de opt-in reflejan estas tendencias regionales.
- **Enlace:** https://ppc.land/16-grant-ai-data-access-reluctantly-7-willingly-usercentrics-finds/

### Lacuna obtiene ID TCF 1648 para señales de consentimiento europeo

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Un intercambio publicitario nuevo (Lacuna) está registrado en TCF para Europa. Relevante si trabajas con este exchange o necesitas validar vendors TCF en implementaciones de consent mode; verifica que tus consent strings incluyan este ID si Lacuna es parte de tu stack.
- **Enlace:** https://ppc.land/singapores-lacuna-gains-tcf-vendor-id-1648-for-european-consent-signals/

### AdSense traslada errores TCF del reporte a Policy Center

- **Fuente:** PPC Land · **Area:** consent/privacy
- **Implicacion:** Google AdSense cambió dónde reporta errores de consent string (EEA/UK/CH): ahora están en Policy Center bajo 'Regulatory issue'. Revisa si tus clientes monitorean estos errores en la ubicación antigua y migra el seguimiento.
- **Deja obsoleto:** El reporte TCF error específico de AdSense queda reemplazado por Policy Center; dejas de consultar la herramienta anterior para estos datos.
- **Enlace:** https://ppc.land/adsense-drops-tcf-error-report-as-consent-errors-move-to-policy-center/

## Relevancia baja (3)

### Puntos de dolor comunes en compliance de privacy

- **Fuente:** ObservePoint Blog · **Area:** QA
- **Implicacion:** Artículo educativo sobre desafíos genéricos (gestión de consentimiento, auditoría de tags, documentación). Lectura contextual útil pero sin cambios operacionales inmediatos que afecten implementaciones actuales.
- **Enlace:** https://www.observepoint.com/blog/3-common-pain-points-of-privacy-compliance/

### Smart Bidding en Google Ads: estrategias automatizadas con ML

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Contenido educativo sobre estrategias de pujas automáticas de Google Ads. Útil para contexto, pero no es un cambio de plataforma ni política que obligue a actuar de inmediato.
- **Enlace:** https://ppc.land/smart-bidding/

### Customer Match: explicación de targeting con listas propias

- **Fuente:** PPC Land · **Area:** otros
- **Implicacion:** Es un tutorial sobre Customer Match de Google Ads. Útil para recordar la mecánica, pero no representa cambio de plataforma ni nueva política que requiera acción inmediata.
- **Enlace:** https://ppc.land/customer-match/

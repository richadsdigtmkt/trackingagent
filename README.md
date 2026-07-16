# TrackingAgent

Base de conocimiento y pipeline de novedades para un consultor senior de **conversion
tracking** (GTM, GA4, Meta Pixel, server-side tracking, consent/privacy) en mercados DACH,
Espana y UK. Es el equivalente, para tracking, del proyecto `richadsagent` (SEA/SEO):
misma arquitectura, tema adaptado.

## Como funciona

Cada dia, un workflow de GitHub Actions ejecuta `scripts/ingest_tracking_news.py`, que:

1. Lee 5 feeds RSS del sector (Simo Ahava, Google Analytics Blog, Analytics Mania,
   MeasureSchool, ObservePoint).
2. Filtra las entradas publicadas en las ultimas **26 horas**.
3. Resume cada entrada con **Claude Haiku** (`claude-haiku-4-5-20251001`), clasificandola
   por relevancia (alta/media/baja) y marcando si deja **obsoleta** alguna practica previa.
4. Escribe un markdown diario en `conocimiento/novedades/YYYY-MM-DD_novedades.md` con
   frontmatter YAML y secciones por relevancia.
5. Hace commit automatico del nuevo archivo.

## Requisito de configuracion

El script necesita la variable de entorno **`ANTHROPIC_API_KEY`**. En GitHub se configura
como secreto del repositorio:

> **Settings > Secrets and variables > Actions > New repository secret**
> Nombre: `ANTHROPIC_API_KEY` · Valor: tu clave de la API de Anthropic.

La clave **nunca** se escribe en el codigo.

## Operacion

- **Automatico:** el workflow corre a diario (cron doble 05:00 y 06:00 UTC para cubrir el
  horario de verano/invierno de Madrid, ambos = 07:00 hora local).
- **Manual (primera prueba / bajo demanda):** en GitHub, pestana **Actions** >
  workflow **"Novedades del sector (tracking)"** > boton **"Run workflow"**.
  Tras el primer run, revisa el log: cada fuente indica cuantas entradas encontro. Si
  alguna devuelve 0 de forma **persistente**, su URL de RSS puede haber cambiado —
  actualizala en la lista `FUENTES` de `scripts/ingest_tracking_news.py`.

## Coste

Se usa Claude Haiku, el modelo mas barato, y solo sobre las entradas nuevas de cada dia
(tipicamente unas pocas). El gasto diario es de centimos; el consumo se puede seguir en el
panel de uso de la API de Anthropic.

## Base de conocimiento destilada (manual)

Ademas de las novedades automaticas, el repo mantiene conocimiento redactado a mano:

- `conocimiento/criterios/` — reglas de diagnostico de tracking (que es, como detectarlo,
  como corregirlo).
- `conocimiento/clientes/` — destilados por cliente (contexto, hallazgos, criterios
  aplicados, pendientes, preguntas abiertas), con frontmatter YAML.
- `conocimiento/novedades/` — generado automaticamente por el pipeline (no editar a mano).

## Estructura

```
trackingagent/
├── scripts/
│   └── ingest_tracking_news.py
├── .github/workflows/
│   └── novedades-diarias.yml
├── conocimiento/
│   ├── novedades/    # automatico
│   ├── criterios/    # manual
│   └── clientes/     # manual
├── requirements.txt
└── README.md
```

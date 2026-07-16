#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/ingest_tracking_news.py

Lee feeds RSS del sector de conversion tracking (GTM, GA4, Meta Pixel,
server-side, consent/privacy), filtra las entradas de las ultimas 26 horas,
las resume con Claude (Haiku) y escribe un markdown diario en
conocimiento/novedades/YYYY-MM-DD_novedades.md.

Equivalente, para tracking, del pipeline de richadsagent (SEA/SEO).

Requisitos: feedparser, requests. La API key se lee de ANTHROPIC_API_KEY
(nunca va en el codigo).
"""

import os
import sys
import json
import time
import datetime as dt
from calendar import timegm

import feedparser
import requests

# --------------------------------------------------------------------------- #
# Configuracion
# --------------------------------------------------------------------------- #

TEMA = "conversion tracking (GTM, GA4, Meta Pixel, server-side, consent/privacy)"

FUENTES = [
    {"nombre": "Simo Ahava",             "url": "https://www.simoahava.com/rss.xml",                            "area": "GTM/GA4"},
    {"nombre": "Google Analytics Blog",  "url": "https://blog.google/products/marketingplatform/analytics/rss/", "area": "GA4"},
    {"nombre": "Analytics Mania",        "url": "https://www.analyticsmania.com/feed/",                         "area": "GTM/GA4"},
    {"nombre": "MeasureSchool",          "url": "https://measureschool.com/feed/",                              "area": "Tracking general"},
    {"nombre": "ObservePoint Blog",      "url": "https://www.observepoint.com/blog/feed/",                      "area": "Tag governance/QA"},
]

VENTANA_HORAS = 26

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"
MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 700

# Carpeta de salida: conocimiento/novedades relativa a la raiz del repo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE_DIR, "conocimiento", "novedades")

SYSTEM_PROMPT = (
    "Eres el analista de novedades de un consultor senior de conversion tracking "
    "(GTM, GA4, Meta Pixel, server-side, consent mode) que trabaja mercados DACH, "
    "Espana y UK. Resume para que el consultor decida en 10 segundos si le afecta y "
    "que hacer. Distingue cambio real de plataforma/politica vs. ruido/opinion. Si algo "
    "deja obsoleta una practica anterior (ej. un metodo de implementacion de Consent "
    "Mode), dilo explicitamente.\n\n"
    "Devuelve EXCLUSIVAMENTE un objeto JSON valido, sin texto alrededor ni bloques de "
    "codigo, con exactamente estas claves:\n"
    '  "relevancia": "alta" | "media" | "baja",\n'
    '  "titular": string (max 90 caracteres, en espanol),\n'
    '  "implicacion": string (1-2 frases: que significa para el consultor y que hacer),\n'
    '  "obsolescencia": string ("" si no aplica; si aplica, que practica queda obsoleta),\n'
    '  "area": string (una de: GTM, GA4, Meta Pixel, server-side, consent/privacy, QA, otros).\n'
    "Marca relevancia 'alta' solo si es un cambio real de plataforma o politica que "
    "obliga a actuar; 'media' si conviene conocerlo; 'baja' si es opinion o tutorial menor."
)


# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #

def log(msg):
    print("[ingest] " + str(msg), flush=True)


def entrada_reciente(entry, limite_epoch):
    """True si la entrada tiene fecha dentro de la ventana."""
    for campo in ("published_parsed", "updated_parsed"):
        t = entry.get(campo)
        if t:
            try:
                return timegm(t) >= limite_epoch
            except Exception:
                continue
    # Sin fecha fiable: la incluimos (mejor de mas que perder una novedad real)
    return True


def texto_entrada(entry):
    """Extrae un resumen textual de la entrada para pasar al modelo."""
    for campo in ("summary", "description"):
        if entry.get(campo):
            return entry[campo]
    if entry.get("content"):
        try:
            return entry["content"][0].get("value", "")
        except Exception:
            pass
    return ""


def limpiar_html(texto, limite=1500):
    """Quita etiquetas HTML de forma simple y recorta."""
    import re
    txt = re.sub(r"<[^>]+>", " ", texto or "")
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt[:limite]


def resumir_con_claude(api_key, fuente, entry):
    """Llama a Claude Haiku y devuelve el dict con el resumen, o None si falla."""
    titulo = entry.get("title", "(sin titulo)")
    enlace = entry.get("link", "")
    cuerpo = limpiar_html(texto_entrada(entry))

    user_msg = (
        "Fuente: " + fuente["nombre"] + " (area: " + fuente["area"] + ")\n"
        "Titulo: " + titulo + "\n"
        "Enlace: " + enlace + "\n"
        "Extracto: " + cuerpo + "\n\n"
        "Resume segun las instrucciones y devuelve solo el JSON."
    )

    payload = {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_msg}],
    }
    headers = {
        "x-api-key": api_key,
        "anthropic-version": ANTHROPIC_VERSION,
        "content-type": "application/json",
    }

    for intento in range(2):
        try:
            r = requests.post(ANTHROPIC_API_URL, headers=headers,
                              data=json.dumps(payload), timeout=60)
            if r.status_code == 200:
                data = r.json()
                texto = "".join(
                    b.get("text", "") for b in data.get("content", [])
                    if b.get("type") == "text"
                ).strip()
                resumen = _parse_json(texto)
                if resumen:
                    resumen["titulo_original"] = titulo
                    resumen["enlace"] = enlace
                    resumen["fuente"] = fuente["nombre"]
                    return resumen
                log("  ! respuesta no parseable para: " + titulo[:60])
                return None
            elif r.status_code in (429, 500, 502, 503, 529):
                log("  ! " + str(r.status_code) + ", reintentando en 5s...")
                time.sleep(5)
                continue
            else:
                log("  ! error API " + str(r.status_code) + ": " + r.text[:200])
                return None
        except requests.RequestException as e:
            log("  ! excepcion de red: " + str(e) + "; reintento " + str(intento + 1) + "/2")
            time.sleep(5)
    return None


def _parse_json(texto):
    """Extrae el primer objeto JSON de un texto, tolerando fences ```json."""
    if not texto:
        return None
    t = texto.strip()
    if t.startswith("```"):
        t = t.strip("`")
        if t.lower().startswith("json"):
            t = t[4:]
    ini, fin = t.find("{"), t.rfind("}")
    if ini == -1 or fin == -1 or fin <= ini:
        return None
    try:
        return json.loads(t[ini:fin + 1])
    except json.JSONDecodeError:
        return None


# --------------------------------------------------------------------------- #
# Escritura del markdown
# --------------------------------------------------------------------------- #

def escribir_markdown(resumenes, fuentes_ok, fuentes_vacias, fecha):
    os.makedirs(OUT_DIR, exist_ok=True)
    ruta = os.path.join(OUT_DIR, fecha + "_novedades.md")

    por_rel = {"alta": [], "media": [], "baja": []}
    for r in resumenes:
        rel = (r.get("relevancia") or "baja").lower()
        if rel not in por_rel:
            rel = "baja"
        por_rel[rel].append(r)

    tags = sorted({(r.get("area") or "otros") for r in resumenes})

    # Frontmatter YAML
    L = ["---"]
    L.append("tema: " + TEMA)
    L.append("fecha: " + fecha)
    L.append("fuentes_escaneadas: " + str(len(fuentes_ok) + len(fuentes_vacias)))
    L.append("novedades: " + str(len(resumenes)))
    L.append("relevancia_alta: " + str(len(por_rel["alta"])))
    L.append("tags: [" + ", ".join(tags) + "]")
    L.append("---")
    L.append("")
    L.append("# Novedades del sector — " + fecha)
    L.append("")
    L.append(
        "Fuentes con entradas: " + (", ".join(fuentes_ok) if fuentes_ok else "ninguna") + ". "
        "Sin entradas en la ventana: " + (", ".join(fuentes_vacias) if fuentes_vacias else "ninguna") + "."
    )
    L.append("")

    if not resumenes:
        L.append("_Sin novedades en las ultimas " + str(VENTANA_HORAS) + " horas._")
    else:
        for rel, titulo_sec in (("alta", "Relevancia alta"),
                                ("media", "Relevancia media"),
                                ("baja", "Relevancia baja")):
            items = por_rel[rel]
            L.append("## " + titulo_sec + " (" + str(len(items)) + ")")
            L.append("")
            if not items:
                L.append("_Nada en esta categoria._")
                L.append("")
                continue
            for r in items:
                L.append("### " + (r.get("titular") or r.get("titulo_original") or "(sin titulo)"))
                L.append("")
                L.append("- **Fuente:** " + str(r.get("fuente")) + " · **Area:** " + str(r.get("area", "otros")))
                L.append("- **Implicacion:** " + (r.get("implicacion", "") or "").strip())
                obs = (r.get("obsolescencia") or "").strip()
                if obs:
                    L.append("- **Deja obsoleto:** " + obs)
                if r.get("enlace"):
                    L.append("- **Enlace:** " + r["enlace"])
                L.append("")

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\n".join(L).rstrip() + "\n")
    return ruta


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        log("ERROR: falta la variable de entorno ANTHROPIC_API_KEY.")
        sys.exit(1)

    ahora = dt.datetime.now(dt.timezone.utc)
    limite_epoch = timegm((ahora - dt.timedelta(hours=VENTANA_HORAS)).utctimetuple())
    fecha = ahora.strftime("%Y-%m-%d")

    resumenes = []
    fuentes_ok, fuentes_vacias = [], []

    for fuente in FUENTES:
        log("Leyendo " + fuente["nombre"] + " -> " + fuente["url"])
        try:
            feed = feedparser.parse(fuente["url"])
        except Exception as e:
            log("  ! no se pudo parsear el feed: " + str(e))
            fuentes_vacias.append(fuente["nombre"])
            continue

        if getattr(feed, "bozo", 0) and not feed.entries:
            log("  ! feed invalido o inaccesible (bozo). Revisar la URL del RSS.")
            fuentes_vacias.append(fuente["nombre"])
            continue

        recientes = [e for e in feed.entries if entrada_reciente(e, limite_epoch)]
        log("  " + str(len(recientes)) + " entrada(s) en la ventana de " +
            str(VENTANA_HORAS) + "h (de " + str(len(feed.entries)) + " totales)")

        if not recientes:
            fuentes_vacias.append(fuente["nombre"])
            continue

        fuentes_ok.append(fuente["nombre"])
        for entry in recientes:
            resumen = resumir_con_claude(api_key, fuente, entry)
            if resumen:
                resumenes.append(resumen)
            time.sleep(1)  # cortesia con la API

    ruta = escribir_markdown(resumenes, fuentes_ok, fuentes_vacias, fecha)
    log("Escrito: " + ruta)
    log("Resumen: " + str(len(resumenes)) + " novedad(es); fuentes con entradas: " +
        str(len(fuentes_ok)) + "; sin entradas: " + str(len(fuentes_vacias)))

    if fuentes_vacias:
        log("NOTA: fuentes sin entradas hoy (verificar la URL del RSS si es persistente): "
            + ", ".join(fuentes_vacias))


if __name__ == "__main__":
    main()

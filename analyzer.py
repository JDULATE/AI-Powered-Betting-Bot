import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import (
    FECHA, BANCA_ACTUAL, OBJETIVO_FINAL, CASA_APUESTAS,
    MODO, PARTIDOS_ESPECIFICOS, LIGAS_NUCLEO,
    LIGAS_SECUNDARIAS, ETAPA_CONFIG
)

load_dotenv()

def construir_system_prompt():
    return """Eres un analista cuantitativo profesional de apuestas deportivas.
Debes generar un reporte COMPLETO y DETALLADO sin interrupciones.
NO hagas introducciones largas. Ve directo al análisis.
NO uses frases como "simularé" o "asumo". Actúa como si tuvieras los datos.
Usa SIEMPRE el formato estructurado con todas las secciones numeradas.
El reporte debe incluir números, probabilidades y cuotas concretas en cada sección."""


def construir_user_prompt(partidos_del_dia=None):
    etapa = ETAPA_CONFIG

    partidos_texto = ""
    if PARTIDOS_ESPECIFICOS:
        partidos_texto = "PARTIDOS A ANALIZAR:\n"
        for i, p in enumerate(PARTIDOS_ESPECIFICOS, 1):
            partidos_texto += f"{i}. {p}\n"
    else:
        partidos_texto = "Selecciona los mejores partidos disponibles hoy en las ligas núcleo."

    return f"""Genera el reporte COMPLETO de análisis de apuestas para hoy.

DATOS DE SESIÓN:
- Fecha: {FECHA}
- Casa: {CASA_APUESTAS}
- Banca: ₡{BANCA_ACTUAL:,}
- Objetivo: ₡{OBJETIVO_FINAL:,}
- Etapa: {etapa['etapa']} — {etapa['nota']}
- Cuota objetivo: {etapa['cuota_objetivo']} (rango {etapa['rango'][0]}–{etapa['rango'][1]})
- Stake: {int(etapa['stake_pct']*100)}% = ₡{int(BANCA_ACTUAL * etapa['stake_pct']):,}
- Ligas núcleo: {', '.join(LIGAS_NUCLEO)}
- Ligas secundarias: {', '.join(LIGAS_SECUNDARIAS)}
- Modo: {MODO}

{partidos_texto}

INSTRUCCIÓN CRÍTICA: Genera el reporte COMPLETO con TODAS estas secciones.
No omitas ninguna. Incluye números reales en cada una.

---
## 1. RESUMEN DEL DÍA
(partidos analizados, ligas, etapa detectada, stake sugerido)

## 2. ANÁLISIS DE PARTIDOS CANDIDATOS
(para cada partido: forma reciente, xG, marcadores probables, mercados evaluados con probabilidades %)

## 3. TOP 5 PICKS DEL DÍA
(partido, mercado, probabilidad estimada %, cuota, estabilidad, liga)

## 4. PARLEY PRINCIPAL RECOMENDADO
(pick 1 y pick 2 con justificación, cuota total, probabilidad combinada, stake en ₡, nivel de riesgo)

## 5. PARLEY ALTERNATIVO CONSERVADOR
(versión más segura con cuota menor)

## 6. MEJOR PICK INDIVIDUAL
(el pick más sólido del día)

## 7. CONCLUSIÓN FINAL
(recomendación, pick más fuerte, pick más delicado, si vale apostar hoy)
---

Empieza directamente con la Sección 1. Sin preámbulos."""


def ejecutar_analisis(partidos_del_dia=None):
    print("⏳ Enviando análisis a Gemini... (puede tomar 30-60 segundos)")

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt_completo = construir_system_prompt() + "\n\n" + construir_user_prompt(partidos_del_dia)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_completo,
        config=types.GenerateContentConfig(
            max_output_tokens=8192,      # ← duplicado de 4096 a 8192
            temperature=0.2,             # ← más bajo = más consistente
        )
    )

    return response.text
import os
import requests
from datetime import date
from dotenv import load_dotenv

load_dotenv()

FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": FOOTBALL_API_KEY
}

# IDs de ligas en API-Football
LIGAS_IDS = {
    "UEFA Champions League": 2,
    "UEFA Europa League":    3,
    "UEFA Conference League": 848,
    "Premier League":        39,
    "La Liga":               140,
    "Serie A":               135,
    "Bundesliga":            78,
    "Ligue 1":               61,
    "English Championship":  40,
    "Eredivisie":            88,
}

TEMPORADA = 2025  # temporada actual


def obtener_partidos_hoy():
    """
    Obtiene todos los partidos de hoy en las ligas núcleo via API-Football.
    Retorna lista de strings con contexto para el prompt.
    """
    hoy = date.today().strftime("%Y-%m-%d")
    partidos_encontrados = []

    print(f"🔍 Buscando partidos reales del {hoy}...")

    try:
        url = f"{BASE_URL}/fixtures"
        params = {"date": hoy}
        response = requests.get(url, headers=HEADERS, params=params, timeout=15)

        if response.status_code != 200:
            print(f"  ⚠ Error HTTP {response.status_code} en API-Football")
            return []

        data = response.json()

        # Verificar errores de autenticación
        if data.get("errors"):
            errores = data["errors"]
            print(f"  ⚠ Error de API: {errores}")
            return []

        fixtures = data.get("response", [])
        print(f"  Total fixtures hoy en API: {len(fixtures)}")

        # Filtrar solo nuestras ligas núcleo
        ligas_ids_set = set(LIGAS_IDS.values())

        for fixture in fixtures:
            liga_id   = fixture["league"]["id"]
            liga_name = fixture["league"]["name"]

            if liga_id not in ligas_ids_set:
                continue

            home   = fixture["teams"]["home"]["name"]
            away   = fixture["teams"]["away"]["name"]
            hora   = fixture["fixture"]["date"][11:16]
            estado = fixture["fixture"]["status"]["short"]

            # Solo partidos programados o en juego
            if estado in ["NS", "1H", "HT", "2H", "ET", "BT", "P"]:
                partidos_encontrados.append(
                    f"{home} vs {away} — {liga_name} — {hora} UTC"
                )

    except requests.exceptions.RequestException as e:
        print(f"  ⚠ Error de conexión: {e}")
        return []

    if partidos_encontrados:
        print(f"✅ {len(partidos_encontrados)} partidos encontrados en ligas núcleo.\n")
    else:
        print("⚠ No hay partidos en ligas núcleo hoy.\n")

    return partidos_encontrados


def formatear_para_prompt(partidos):
    if not partidos:
        return "No hay partidos en ligas núcleo hoy. Analiza opciones de ligas secundarias si las hay."

    texto = f"PARTIDOS REALES DE HOY ({date.today().strftime('%d/%m/%Y')}):\n"
    for i, p in enumerate(partidos, 1):
        texto += f"{i}. {p}\n"
    return texto
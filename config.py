from datetime import date

# ============================================================
# EDITAR SOLO ESTA SECCIÓN CADA DÍA
# ============================================================

FECHA = date.today().strftime("%d/%m/%y")   # o pon la fecha manual: "31/3/26"

BANCA_ACTUAL = 5000          # en colones
OBJETIVO_FINAL = 500000      # meta
CASA_APUESTAS = "DoradoBet"
MODO = "ULTRA CONSERVADOR Y DE MÁXIMA PRECISIÓN"

# Partidos específicos (dejar vacío para búsqueda automática)
PARTIDOS_ESPECIFICOS = [
    # "Real Madrid vs Barcelona",
    # "Liverpool vs Arsenal",
]

# ============================================================
# NO EDITAR — Lógica de etapa automática
# ============================================================

LIGAS_NUCLEO = [
    "UEFA Champions League", "UEFA Europa League",
    "Premier League", "La Liga", "Serie A",
    "Bundesliga", "Ligue 1", "English Championship", "Eredivisie"
]

LIGAS_SECUNDARIAS = [
    "UEFA Conference League", "UEFA Champions League Femenina",
    "Eliminatorias UEFA", "Liga Promerica Costa Rica",
    "Torneo de Copa Costa Rica"
]

def detectar_etapa(banca):
    if banca < 20000:
        return {
            "etapa": 0,
            "nota": "Banca por debajo de Etapa 1. Modo ultra-conservador.",
            "cuota_objetivo": 1.80,
            "rango": (1.70, 1.95),
            "picks": 2,
            "stake_pct": 0.30
        }
    elif banca < 80000:
        return {
            "etapa": 1,
            "nota": "Etapa 1: crecimiento disciplinado.",
            "cuota_objetivo": 2.00,
            "rango": (1.90, 2.10),
            "picks": 2,
            "stake_pct": 0.40
        }
    elif banca < 200000:
        return {
            "etapa": 2,
            "nota": "Etapa 2: reducción de varianza.",
            "cuota_objetivo": 1.90,
            "rango": (1.85, 2.00),
            "picks": 2,
            "stake_pct": 0.40
        }
    elif banca < 500000:
        return {
            "etapa": 3,
            "nota": "Etapa 3: proteger capital.",
            "cuota_objetivo": 1.85,
            "rango": (1.75, 1.95),
            "picks": 2,
            "stake_pct": 0.30
        }
    else:
        return {
            "etapa": 4,
            "nota": "Etapa 4: preservación de ganancias.",
            "cuota_objetivo": 1.77,
            "rango": (1.70, 1.85),
            "picks": 2,
            "stake_pct": 0.20
        }

ETAPA_CONFIG = detectar_etapa(BANCA_ACTUAL)
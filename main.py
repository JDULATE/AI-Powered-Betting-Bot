import os
from datetime import datetime
from config import FECHA, BANCA_ACTUAL, OBJETIVO_FINAL, ETAPA_CONFIG
from analyzer import ejecutar_analisis
from data_fetcher import obtener_partidos_hoy


def guardar_reporte(reporte, fecha):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/reporte_{fecha.replace('/', '-')}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"REPORTE DE ANÁLISIS — {fecha}\n")
        f.write("=" * 60 + "\n\n")
        f.write(reporte)
    return filename


def mostrar_resumen_config():
    etapa = ETAPA_CONFIG
    falta = OBJETIVO_FINAL - BANCA_ACTUAL
    print("\n" + "="*55)
    print("  BETTING BOT — ANÁLISIS DEL DÍA")
    print("="*55)
    print(f"  Fecha        : {FECHA}")
    print(f"  Banca actual : ₡{BANCA_ACTUAL:,}")
    print(f"  Objetivo     : ₡{OBJETIVO_FINAL:,}")
    print(f"  Faltante     : ₡{falta:,}")
    print(f"  Etapa        : {etapa['etapa']} — {etapa['nota']}")
    print(f"  Cuota target : {etapa['cuota_objetivo']}")
    print(f"  Stake suger. : {int(etapa['stake_pct']*100)}% = ₡{int(BANCA_ACTUAL * etapa['stake_pct']):,}")
    print("="*55 + "\n")


def main():
    mostrar_resumen_config()

    confirm = input("¿Ejecutar análisis? (s/n): ").strip().lower()
    if confirm != 's':
        print("Análisis cancelado.")
        return

    # Obtener partidos reales del día
    partidos = obtener_partidos_hoy()

    # Pasar partidos reales al análisis
    reporte = ejecutar_analisis(partidos)

    archivo = guardar_reporte(reporte, FECHA)

    print("\n" + "="*55)
    print("  REPORTE COMPLETO")
    print("="*55 + "\n")
    print(reporte)
    print(f"\n✅ Reporte guardado en: {archivo}")


if __name__ == "__main__":
    main()
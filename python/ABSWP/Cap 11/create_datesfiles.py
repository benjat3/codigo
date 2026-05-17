from pathlib import Path

# 1. Creamos una carpeta de prueba
carpeta_prueba = Path('laboratorio_ensayos')
carpeta_prueba.mkdir(exist_ok=True)

# 2. Diseñamos nuestros casos de prueba (Regla 3: Casos contrastantes)
archivos_ficticios = [
    'ensayo_termo_04-28-2026_final.xlsx',  # Fecha americana válida
    'resultados_05-10-2026.csv',           # Fecha americana válida
    'manual_bomba_vacio.pdf',              # ¡Cuidado! No tiene fecha
    'calibracion_sensor_12-31-2026.xlsx'   # Fecha americana válida
]

# 3. Creamos los archivos físicos vacíos en tu disco duro
for nombre in archivos_ficticios:
    ruta_completa = carpeta_prueba / nombre
    ruta_completa.write_text('Datos de prueba ficticios')
    print(f'Archivo creado: {ruta_completa}')

print("\n¡Túnel de viento listo para la prueba!")

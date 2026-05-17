import serial
import re
import logging
import time
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.fft import rfft, rfftfreq

# ==========================================
# 1. CONFIGURACIÓN INICIAL (La Plomería)
# ==========================================

# Configuro el logging para que guarde los errores de forma silenciosa
logging.basicConfig(filename='skid_errores.log', level=logging.ERROR, 
                    format='%(asctime)s - %(message)s')

# Creo la carpeta para guardar los archivos Parquet usando pathlib
carpeta_datos = Path('datos_historicos')
carpeta_datos.mkdir(exist_ok=True)

# Configuración del puerto USB en Debian
PUERTO = '/dev/ttyUSB0'
BAUD_RATE = 115200 # Velocidad de comunicación con el ESP32

# Patrón Regex: Acepta solo números con decimales, positivos o negativos, separados por comas
# Ejemplo válido: "12.5,-0.3,9.8" | Ejemplo inválido: "12.5, &Error, 9.8"
patron_valido = re.compile(r'^-?\d+\.\d+,-?\d+\.\d+,-?\d+\.\d+$')

# Tamaño de la "Ventana" (Cuántos datos juntamos antes de procesar)
TAMANO_VENTANA = 1024
buffer_datos = [] # La "caja" temporal en la memoria RAM

# ==========================================
# 2. EL BUCLE PRINCIPAL (Tiempo Real)
# ==========================================

print("Iniciando Skid Predictivo... Presioná Ctrl+C para detener.")

try:
    # Abro la conexión con el cable USB
    with serial.Serial(PUERTO, BAUD_RATE, timeout=1) as esp32:
        
        while True: # Bucle infinito de lectura
            # 1. Leer la línea del ESP32 y limpiarle los saltos de línea (\n)
            linea_cruda = esp32.readline().decode('utf-8').strip()
            
            # 2. El Escudo Regex (Ignorar basura electromagnética)
            if not patron_valido.match(linea_cruda):
                logging.error(f'Basura detectada y filtrada: {linea_cruda}')
                continue # Salta a la siguiente vuelta del bucle ignorando el error
            
            # 3. Convertir el texto a números y guardarlos en el buffer temporal
            valores_str = linea_cruda.split(',')
            valores_float = [float(x) for x in valores_str]
            buffer_datos.append(valores_float)
            
            # ==========================================
            # 3. PROCESAMIENTO POR LOTES (El Motor)
            # ==========================================
            if len(buffer_datos) == TAMANO_VENTANA:
                # ¡La ventana se llenó! Congelamos la lectura un milisegundo.
                
                # Pasamos la lista normal a una matriz hiper-rápida de NumPy
                matriz_datos = np.array(buffer_datos)
                
                # Separar las columnas (0: X, 1: Y, 2: Z)
                eje_z = matriz_datos[:, 2] 
                
                # --- MATEMÁTICA EN VIVO (NumPy) ---
                # Detrending: Restar el promedio para centrar la onda en cero
                z_limpio = eje_z - np.mean(eje_z)
                
                # Transformada de Fourier (FFT) para buscar el desbalanceo
                # (Acá luego pondrás la lógica para graficar o buscar picos)
                espectro = np.abs(rfft(z_limpio)) 
                
                # --- GUARDADO EFICIENTE (Pandas y Parquet) ---
                # Convertimos el bloque de 1024 datos en un DataFrame
                df = pd.DataFrame(matriz_datos, columns=['Accel_X', 'Accel_Y', 'Accel_Z'])
                
                # Generamos un nombre de archivo único con la fecha y hora exacta
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                archivo_salida = carpeta_datos / f'lote_{timestamp}.parquet'
                
                # Guardamos en Parquet (Una sola línea, ocupa bytes y es rapidísimo)
                df.to_parquet(archivo_salida)
                
                print(f"Paquete de {TAMANO_VENTANA} datos procesado y guardado en {archivo_salida.name}")
                
                # 4. Vaciar la caja para la siguiente ronda
                buffer_datos.clear()

except KeyboardInterrupt:
    print("\nAdquisición detenida por el usuario. Cerrando puerto seguro.")
except Exception as e:
    print(f"Error fatal: {e}")
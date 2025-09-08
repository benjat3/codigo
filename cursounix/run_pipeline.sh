#!/usr/bin/env bash
# run_pipeline.sh - pipeline completo
set -euo pipefail #para evitar errores


# Defino variables que luego voy a usar
IMG_DIR="dataset"
RESULTADO="resultado"
SELECCIONADO="resultado/seleccionado"
RESUMEN="$RESULTADO/resumen.csv"

#Definir trayectoria del video.
TRAYECTORIA="circle"
#Trayectoria puede ser circle o line
	#Uso ejemplo:
	#python3 select_trajectory.py circle cx cy r n > traj_list.txt
	#python3 select_trajectory.py line ax ay bx by n > traj_list.txt
CX=135
CY=40
R=30
NPTS=150

mkdir -p "$RESULTADO" "$SELECCIONADO"

# encabezado csv
echo "archivo,indice,i,j,alfa,beta,peso" > "$RESUMEN"

# 1) generar metadatos para cada imagen
# Tarea: Ejecutar el archivo "analyze_images.py" en el directorio dataset
# y enviar la salida a RESUMEN.csv en la carpeta resultado
python3 scripts/analyze_images.py "$IMG_DIR" >> "$RESUMEN" #Esta línea se borraría para el estudiante


# 2) Mostrar al usuario cuantas imagenes han sido procesadas
nimages=$(($(wc -l < "$RESUMEN") - 1)) 
echo "Imagenes procesadas: $nimages" #Esta línea se borraría para el estudiate

# 3) filtrar alfa entre 30 y 60 (cerrado,cerrado)
# CSV: filename,index,i,j,alpha,beta,size
# 
#
awk -F, 'NR>1 && $5>=30 && $5<=60 {print $1}' "$RESUMEN" > "$RESULTADO/alfa_alto.txt"
echo "Imagenes con Alfa Alto: $(wc -l < "$RESULTADO/alfa_alto.txt")"

# 4) copiar imagenes seleccionadas a SELECCIONADO
mkdir -p "$SELECCIONADO" #Esta línea se borraría para el estudiante
while IFS= read -r f; do
    cp "$IMG_DIR/$f" "$SELECCIONADO/"
done < "$RESULTADO/alfa_alto.txt"

# 5) Crear trayectoria paramétrica con select_trajectory.py
python3 scripts/select_trajectory.py "$TRAYECTORIA" "$CX" "$CY" "$R" "$NPTS" > traj_list.txt #Esta línea se borraría para el estudiante
echo "Puntos de trayectoria: $(wc -l < traj_list.txt)"

# 6) Preparar imagenes para ffmpeg
TMPSEQ="$RESULTADO/seq"
mkdir -p "$TMPSEQ"
rm -f "$TMPSEQ"/*

i=0
while IFS= read -r img; do
    i=$((i+1))
    src="$IMG_DIR/$img"
    dst="$TMPSEQ/$(printf "%05d.png" $i)"
    cp "$src" "$dst"
done < traj_list.txt

# 7) generate video with ffmpeg (15 fps)
VIDEO="$RESULTADO/trajectory_video.mp4"
ffmpeg -y -framerate 15 -i "$TMPSEQ/%05d.png" -c:v libx264 -pix_fmt yuv420p "$VIDEO"

# 8) Generar reporte
#
# Ejecutar report.py desde RESUMEN.csv y enviar los 
# resultados a el archivo reporte.txt en la carpeta resultado
python3 scripts/report.py "$RESUMEN" > "$RESULTADO/reporte.txt"

echo "Terminado. resumen: $RESUMEN, SELECCIONADO: $SELECCIONADO, Video: $VIDEO"

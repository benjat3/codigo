#!/usr/bin/env bash
 #uso de $
fecha=$(date)
echo "hoy es $fecha"

lista=(a b c)
echo ${lista[1]}
echo ${#lista[1]}
echo ${lista[@]}
echo ${#lista[@]}

echo "El script se llama $0"
echo "Primer argumento: $@"


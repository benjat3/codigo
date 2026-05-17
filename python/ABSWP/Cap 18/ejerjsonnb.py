import json

datos_skid = {
    "sensor_id": "SKID-01",
    "estado": "activo",
    "mediciones": {
        "temperatura": 45.5,
        "vibraciones_z": [0.02, 0.05, 9.81]
    }
}
datos_json = json.dumps(datos_skid, indent=2)

with open('skid_estado.json', 'w', encoding='UTF-8') as archivo:
    archivo.write(datos_json)
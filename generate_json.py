import os
import json
from pathlib import Path

# Configuración
CARPETAS = ['B1', 'B2', 'B3', 'B4']
EXTENSIONES = ['.md', '.markdown']
ARCHIVO_JSON = 'markdown_files.json'

def listar_archivos():
    estructura = {}

    for carpeta in CARPETAS:
        if not os.path.exists(carpeta):
            print(f"⚠ Advertencia: La carpeta '{carpeta}' no existe")
            estructura[carpeta] = []
            continue

        archivos = []
        for archivo in Path(carpeta).iterdir():
            if archivo.is_file() and archivo.suffix.lower() in EXTENSIONES:
                archivos.append({
                    'nombre': archivo.name,
                    'ruta': str(archivo)
                })

        estructura[carpeta] = archivos

    return estructura

def guardar_json(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON generado en '{ARCHIVO_JSON}'")

if __name__ == '__main__':
    datos = listar_archivos()
    guardar_json(datos)
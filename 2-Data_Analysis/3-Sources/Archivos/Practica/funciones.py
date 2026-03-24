#2. funciones.py:
#Aquí reside la lógica de creación de carpetas y el movimiento de archivos:
import os
import shutil
from variables import downloads_path, doc_types, img_types, software_types, folders

def crear_carpetas():
    """Crea los directorios de destino si no existen"""
    for folder in folders:
        path = os.path.join(downloads_path, folder)
        os.makedirs(path, exist_ok=True)

def clasificar_y_mover():
    """Recorre la carpeta de descargas y organiza los archivos"""
    for file in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file)

        #Saltar si es una carpeta o el propio script:
        if os.path.isdir(file_path):
            continue

        nombre_lower = file.lower()

        #Determinar carpeta de destino:
        if nombre_lower.endswith(img_types):
            destino = "Imagenes"
        elif nombre_lower.endswith(doc_types):
            destino = "Documentos"
        elif nombre_lower.endswith(software_types):
            destino = "Software"
        else:
            destino = "Otros"

        #Mover el archivo:
        try:
            shutil.move(file_path, os.path.join(downloads_path, destino, file))
        except Exception as e:
            print(f"Error moviendo {file}: {e}")
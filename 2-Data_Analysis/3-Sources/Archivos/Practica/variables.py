#1. variables.py:
#Aquí definimos las rutas y las extensiones para que sea fácil editarlas en el futuro:

import os

#Ruta específica solicitada:
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

#Extensiones de archivos (Tuplas obligatorias para .endswith):
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py', '.ipynb')

#Lista de carpetas de destino:
folders = ["Imagenes", "Documentos", "Software", "Otros"]
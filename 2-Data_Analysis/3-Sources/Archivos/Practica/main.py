#3. main.py:
#Este es el archivo que se va a ejecutar (el principal). Aquí se hace la llamada a todas las funciones definidas:

from funciones import crear_carpetas, clasificar_y_mover

def main():
    print("Iniciando organización de archivos...")
    crear_carpetas()
    clasificar_y_mover()
    print("¡Proceso completado con éxito!")
    input("Presiona Enter para salir...") # Mantiene la consola abierta al terminar

if __name__ == "__main__":
    main()
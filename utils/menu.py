# utils/menu.py
def leer_opcion(mensaje="Seleccione una opción: "):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return None

def mostrar_menu(titulo, opciones):
    print(f"\n--- {titulo} ---")
    for clave, descripcion in opciones.items():
        print(f"{clave}. {descripcion}")
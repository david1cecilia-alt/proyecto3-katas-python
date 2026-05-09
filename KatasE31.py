# Ejercicio 31:
# Esta función solicita nombres al usuario
# y busca un nombre específico en la lista.
# Si no existe, lanza una excepción.


def buscar_nombre():
    nombres = input("Ingresa nombres separados por comas: ").split(",")
    nombres = [n.strip() for n in nombres]

    busqueda = input("Nombre a buscar: ").strip()

    if busqueda in nombres:
        print(f"{busqueda} encontrado.")
    else:
        raise Exception(f"{busqueda} no está en la lista.")

try:
    buscar_nombre()
except Exception as e:
    print(f"Error: {e}")


if __name__ == "__main__": buscar_nombre()
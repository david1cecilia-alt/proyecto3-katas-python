# Ejercicio 9:
# Esta función elimina de la lista las mascotas prohibidas en España
# usando filter().


def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista_mascotas))

if __name__ == "__main__": print(filtrar_mascotas(["Perro", "Tigre", "Gato"]))
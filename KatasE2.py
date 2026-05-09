# Ejercicio 2:
# Este ejercicio usa map() para crear una nueva lista
# con el doble de cada número de la lista original.

def doblar_valores(lista):
    return list(map(lambda x: x * 2, lista))

if __name__ == "__main__": print(doblar_valores([1, 2, 3]))
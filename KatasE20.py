# Ejercicio 20:
# Este ejercicio usa filter() para obtener únicamente
# los valores enteros de una lista mixta.

def solo_enteros(lista):
    # Evita incluir booleanos (True/False)
    return list(filter(lambda x: type(x) == int, lista))

if __name__ == "__main__": print(solo_enteros([1, "hola", 2, "mundo"]))
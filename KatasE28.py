# Ejercicio 28:
# Esta función busca y devuelve
# el primer elemento duplicado de una lista.

def primer_duplicado(lista):
    vistos = set()
    for item in lista:
        if item in vistos:
            return item
        vistos.add(item)
    return None

if __name__ == "__main__": print(primer_duplicado([1, 2, 3, 2, 4]))
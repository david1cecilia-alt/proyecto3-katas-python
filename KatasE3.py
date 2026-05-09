# Ejercicio 3:
# Esta función filtra las palabras que contienen
# una palabra objetivo dentro de una lista.


def buscar_palabra_objetivo(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

if __name__ == "__main__": print(buscar_palabra_objetivo(["casa", "coche", "casita"], "casa"))
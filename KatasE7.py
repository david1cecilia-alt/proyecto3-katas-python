# Ejercicio 7:
# Esta función convierte una lista de tuplas
# en una lista de strings utilizando map().

def tuplas_a_strings(lista_tuplas):
    # Convertimos cada tupla a su representación en string
    return list(map(str, lista_tuplas))

if __name__ == "__main__": print(tuplas_a_strings([(1, 2), (3, 4)]))
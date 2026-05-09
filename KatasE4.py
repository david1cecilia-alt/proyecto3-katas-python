# Ejercicio 4:
# Esta función calcula la diferencia entre los valores
# de dos listas usando map().

def diferencia_listas(lista1, lista2):
    # Asumimos que las listas tienen la misma longitud
    return list(map(lambda x, y: x - y, lista1, lista2))

if __name__ == "__main__": print(diferencia_listas([10, 20], [3, 5]))
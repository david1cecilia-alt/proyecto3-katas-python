# Ejercicio 24:
# Esta función calcula la diferencia acumulada
# de los elementos de una lista usando reduce().

from functools import reduce
def diferencia_total(lista):
    if not lista:
        return 0
    return reduce(lambda x, y: x - y, lista)

if __name__ == "__main__": print(diferencia_total([100, 20, 10]))
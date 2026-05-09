# Ejercicio 22:
# Este ejercicio usa reduce() para calcular
# el producto total de una lista numérica.

from functools import reduce
def producto_total(lista):
    if not lista:
        return 0
    return reduce(lambda x, y: x * y, lista)

if __name__ == "__main__": print(producto_total([2, 3, 4]))
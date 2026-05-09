# Ejercicio 17:
# Esta función convierte una lista de dígitos
# en un número usando reduce().

from functools import reduce
def digitos_a_numero(lista_digitos):
    # [5, 7, 2] -> 5*10 + 7 = 57 -> 57*10 + 2 = 572
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

if __name__ == "__main__": print(digitos_a_numero([5, 7, 2]))
# Ejercicio 39:
# Esta función calcula el área de distintas figuras
# geométricas según los parámetros recibidos.

import math
def calcular_area(figura, datos):

    if figura == "rectangulo":
        return datos[0] * datos[1]

    elif figura == "circulo":
        return math.pi * (datos[0] ** 2)

    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2

    else:
        raise ValueError("Figura no válida")
    
if __name__ == "__main__": print(calcular_area("rectangulo", (10, 5)))
# Ejercicio 6:
# Esta función calcula el factorial de un número
# usando recursividad.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__": print(factorial(5))
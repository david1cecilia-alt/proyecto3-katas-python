# Ejercicio 16:
# Esta función devuelve las palabras de una cadena
# cuya longitud es mayor que un número dado usando filter().

def palabras_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda p: len(p) > n, palabras)) 

if __name__ == "__main__": print(palabras_largas("Python es un lenguaje potente", 5))
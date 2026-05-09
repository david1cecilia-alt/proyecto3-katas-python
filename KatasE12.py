# Ejercicio 12:
# Esta función devuelve una lista con la longitud
# de cada palabra de una frase usando map().

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

if __name__ == "__main__": print(longitud_palabras("Hola que tal"))
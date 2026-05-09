def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

if __name__ == "__main__": print(longitud_palabras("Hola que tal"))
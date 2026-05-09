def transformar_caracteres(caracteres):
    # Set elimina repetidos, luego map crea las tuplas
    unicos = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), unicos))

if __name__ == "__main__": print(transformar_caracteres("abcabc"))
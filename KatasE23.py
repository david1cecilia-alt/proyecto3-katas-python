from functools import reduce
def concatenar_palabras(lista):
    if not lista:
        return ""
    return reduce(lambda x, y: x + " " + y, lista)

if __name__ == "__main__": print(concatenar_palabras(["Hola", "mundo", "Python"]))
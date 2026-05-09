def buscar_palabra_objetivo(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

if __name__ == "__main__": print(buscar_palabra_objetivo(["casa", "coche", "casita"], "casa"))
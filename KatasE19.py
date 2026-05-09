filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

if __name__ == "__main__": print(filtrar_impares([1, 2, 3, 4, 5]))
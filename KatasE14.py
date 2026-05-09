def filtrar_por_letra(lista, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista))

if __name__ == "__main__": print(filtrar_por_letra(["Arbol", "Barco", "Avion"], "A"))
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

if __name__ == "__main__": print(promedio([10, 20, 30]))
class ListaVaciaError(Exception):
    pass

def promedio_lista(lista):
    if not lista:
        raise ListaVaciaError("La lista no puede estar vacía.")
    return sum(lista) / len(lista)

try:
    print(promedio_lista([]))
except ListaVaciaError as e:
    print(f"Error: {e}")

if __name__ == "__main__": print(promedio_lista([10, 20, 30]))
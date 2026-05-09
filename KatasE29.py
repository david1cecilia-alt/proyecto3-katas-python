# Ejercicio 29:
# Esta función convierte un valor en string
# y enmascara todos los caracteres excepto los últimos cuatro.

def enmascarar(valor):
    s = str(valor)
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]

if __name__ == "__main__": print(enmascarar("1234567890"))
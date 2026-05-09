# Ejercicio 1:
# Esta función recibe una cadena de texto y devuelve un diccionario
# con la frecuencia de cada letra, ignorando los espacios.

def frecuencia_letras(cadena):
    # Filtramos espacios y convertimos a minúsculas para uniformidad
    cadena = cadena.replace(" ", "").lower()
    frecuencias = {}
    for letra in cadena:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

if __name__ == "__main__": print(frecuencia_letras("Hola Mundo"))
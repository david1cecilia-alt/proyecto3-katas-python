def contar_palabras(texto):
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)


def eliminar_palabra(texto, palabra):
    return texto.replace(palabra, "").replace("  ", " ").strip()


def procesar_texto(texto, opcion, *args):
    # Uso de *args para pasar parámetros dinámicos a cada subfunción
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida")


if __name__ == "__main__":
    texto_prueba = "el gato corre tras el raton"

    print(f"Contar: {procesar_texto(texto_prueba, 'contar')}")
    print(f"Reemplazar: {procesar_texto(texto_prueba, 'reemplazar', 'gato', 'perro')}")
    print(f"Eliminar: {procesar_texto(texto_prueba, 'eliminar', 'raton')}")

    try:
        procesar_texto(texto_prueba, "invertir")
    except ValueError as e:
        # Captura de error para opciones no implementadas
        print(f"Verificación de error capturado: {e}")

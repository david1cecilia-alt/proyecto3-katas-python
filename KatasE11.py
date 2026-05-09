# Ejercicio 11:
# Este programa solicita la edad del usuario
# y valida que sea un número dentro de un rango válido.

def validar_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if 0 <= edad <= 120:
            print(f"Edad válida: {edad}")
        else:
            print("Error: Edad fuera de rango (0-120).")
    except ValueError:
        print("Error: Debes ingresar un número entero.")

if __name__ == "__main__": validar_edad()
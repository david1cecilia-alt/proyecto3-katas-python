# Ejercicio 8:
# Este programa solicita dos números al usuario,
# intenta dividirlos y maneja errores como división por cero
# o entradas no numéricas.

def division_segura():
    try:
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        resultado = n1 / n2
        print(f"Éxito. Resultado: {resultado}")
    except ValueError:
        print("Error: Debes introducir un valor numérico.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

if __name__ == "__main__":
    division_segura()
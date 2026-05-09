# Ejercicio 38:
# Este programa convierte una calificación numérica
# en una descripción textual.

def calificacion_texto(nota):
    if 0 <= nota <= 69: return "insuficiente"
    elif 70 <= nota <= 79: return "bien"
    elif 80 <= nota <= 89: return "muy bien"
    elif 90 <= nota <= 100: return "excelente"
    else: return "Nota inválida"

if __name__ == "__main__": print(calificacion_texto(85))    
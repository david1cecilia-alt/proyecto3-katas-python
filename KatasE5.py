def calcular_estado(lista_notas, nota_aprobado=5):
    if not lista_notas: return (0, "suspenso")
    media = sum(lista_notas) / len(lista_notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

if __name__ == "__main__": print(calcular_estado([7, 8, 4, 10], 5))
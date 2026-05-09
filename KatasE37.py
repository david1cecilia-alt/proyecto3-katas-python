def momento_del_dia():

    try:
        hora = int(input("Introduce la hora (0-23): "))

        if 6 <= hora <= 11:
            print("Es de día (mañana)")

        elif 12 <= hora <= 19:
            print("Es de tarde")

        elif (20 <= hora <= 23) or (0 <= hora <= 5):
            print("Es de noche")

        else:
            print("Hora no válida")

    except ValueError:
        print("Entrada no válida.")

if __name__ == "__main__": momento_del_dia()
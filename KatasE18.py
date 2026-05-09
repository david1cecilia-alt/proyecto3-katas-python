# Ejercicio 18:
# Este programa crea una lista de estudiantes
# y filtra aquellos con calificación mayor o igual a 90.


def filtrar_excelencia(estudiantes):
    return list(filter(lambda e: e['calificacion'] >= 90, estudiantes))

if __name__ == "__main__": print(filtrar_excelencia([{"nombre": "A", "calificacion": 95}, {"nombre": "B", "calificacion": 80}]))
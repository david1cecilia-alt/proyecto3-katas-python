def filtrar_excelencia(estudiantes):
    return list(filter(lambda e: e['calificacion'] >= 90, estudiantes))

if __name__ == "__main__": print(filtrar_excelencia([{"nombre": "A", "calificacion": 95}, {"nombre": "B", "calificacion": 80}]))
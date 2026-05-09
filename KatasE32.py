# Ejercicio 32:
# Esta función busca un empleado en una lista
# y devuelve su puesto si existe.

def buscar_empleado(nombre_completo, lista_empleados):
    # lista_empleados es un dict tipo {"Nombre": "Puesto"}
    return lista_empleados.get(nombre_completo, "Esa persona no trabaja aquí")

if __name__ == "__main__": print(buscar_empleado("Juan Perez", {"Juan Perez": "Analista"}))
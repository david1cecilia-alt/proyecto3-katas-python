# Ejercicio 34:
# Esta clase representa un árbol con tronco y ramas,
# permitiendo modificar y consultar su estructura.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        # Validar existencia de la rama antes de eliminar
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas
        }

if __name__ == "__main__":
    # Pruebas de funcionalidad de la clase
    mi_arbol = Arbol()
    mi_arbol.crecer_tronco()
    mi_arbol.nueva_rama()
    mi_arbol.crecer_ramas()
    mi_arbol.nueva_rama()
    mi_arbol.nueva_rama()
    mi_arbol.quitar_rama(2)

    print(mi_arbol.info_arbol())

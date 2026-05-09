class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # Si retirar_dinero falla, la transferencia no se completa
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)
        print(f"Transferencia realizada: {self.nombre} → {otro_usuario.nombre} ({cantidad})")

if __name__ == "__main__":
    try:
        alicia = UsuarioBanco("Alicia", 100, True)
        bob = UsuarioBanco("Bob", 50, True)

        bob.agregar_dinero(20)
        bob.transferir_dinero(alicia, 80)
        alicia.retirar_dinero(50)

    except ValueError as e:
        # Manejo de excepciones para evitar el cierre inesperado
        print(f"Operación cancelada: {e}")

    print(f"Estado final -> Alicia: {alicia.saldo} | Bob: {bob.saldo}")

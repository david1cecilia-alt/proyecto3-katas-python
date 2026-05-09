# Ejercicio 40:
# Este programa calcula el precio final de una compra
# aplicando un descuento si el usuario tiene un cupón válido.

def simulador_compra():
    try:
        precio = float(input("Precio original: "))
        tiene_cupon = input("¿Tienes cupón? (sí/no): ").lower()
        
        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Valor del cupón: "))
            if valor_cupon > 0:
                # Evitar que el descuento sea mayor al precio
                precio_final = max(0, precio - valor_cupon)
                print(f"Descuento aplicado. Precio final: {precio_final}")
            else:
                print(f"Cupón no válido. Precio final: {precio}")
        else:
            print(f"Precio final: {precio}")
    except ValueError:
        print("Error en los datos introducidos.")

if __name__ == "__main__": simulador_compra()
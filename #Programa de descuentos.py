#Programa de descuentos
def montototalfinal(monto_compra, vip):
    if monto_compra >= 1000:
        descuento = monto_compra * 0.10
    elif monto_compra >= 500:
        descuento = monto_compra * 0.05
    else:
        descuento = 0

    totalmasdescuento = monto_compra - descuento

    if vip.lower() == 'si':
        totalmasdescuento -= totalmasdescuento * 0.05

    return totalmasdescuento

# pedimos monto total de la compra

monto_compra = float(input("Ingrese el monto total de la compra: $"))

vip = input("El cliente es VIP? (si/no): ")

totalfinal = montototalfinal(monto_compra, vip)

print(f"El total final a pagar es: ${totalfinal:.2f}")
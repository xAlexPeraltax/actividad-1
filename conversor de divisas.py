print("Conversión de monedas")
# Definir las tasas de conversión
dolar = 19.50
peso = 1

print("¿Qué deseas hacer?")
print("1. Convertir de pesos a dólares")
print("2. Convertir de dólares a pesos")

opcion = input()
if opcion == "1":
    pesos = float(input("¿Cuántos pesos cambiarás a dólar? "))
    conversionadolar = pesos / dolar 
    print("Su conversión a dólar sería de: $",round(conversionadolar,2), "dólares.")
if opcion == "2":
    dolares =float(input("¿Cuántos dólares cambiarás a pesos? "))
    conversionapeso = dolares*dolar
    print("Su conversión a pesos sería de: $",round(conversionapeso,2), "pesos.")



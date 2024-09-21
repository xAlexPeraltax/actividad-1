#Programa para determinar si una persona conduce o no
#defenimos la funcion puedeConducir

def puedeConducir (edad,tien_licencia):
    if edad >= 18 and tien_licencia.lower()== 'si':
        return True
    else:
        return False
    
#Solicitar edad
edad = int(input("Ingrese su dedad: "))

#pregunar si tiene licencia o no
licencia = input("¿Tiene licencia de conducir? (si/no): ")

# Llamar la funcion

if puedeConducir(edad, licencia):
    print("Puede conducir.")

else:
    print("No pude conducir.")
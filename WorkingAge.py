"""
03/10/2023
ASIXc M03 UF1 A2
Descripció: Revision edad para trabajar.
"""
try:
    edad=int(input("Introduce tu edad:"))

except:
    print("Introduzca un numero entero")
    edad = int(input("Introduce tu edad:"))
if edad < 16:
    print("Aun no tienes edad para trabajar")
elif edad < 65:
    print("Puedes trabajar")
elif edad >= 65:
    print("Ya no tienes edad para trabajar")

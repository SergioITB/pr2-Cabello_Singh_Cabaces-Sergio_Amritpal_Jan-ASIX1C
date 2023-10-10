"""
Jan Cabaces Batalle
03/10/2023
ASIXc M03 UF1 A2
Descripció:
"""
try:
    edad=int(input("Introduce tu edad:"))

except:
    print("Introduzca un nombre entero")
    edad = int(input("Introduce tu edad:"))

if edad < 16:
    print("Aun no puedes trabajar")
elif edad >= 16:
    print("Puedes trabajar")
elif edad >= 65:
    print("Ya no tienes edad para trabajar")
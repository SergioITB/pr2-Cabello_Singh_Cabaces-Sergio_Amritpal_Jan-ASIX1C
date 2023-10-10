"""
Sergio Cabello Simón
10/10/2023
ASIXc1C M03 UF1
Descripción: Calcula el volumen de un aula
"""
#Variables
largo = 0
ancho = 0
alto = 0
def pedirDatos():
    global largo
    global ancho
    global alto
    largo = float(input("Dime el largo del aula en metros ej:3.50 "))
    ancho = float(input("Dime el ancho del aula en metros ej:1.50 "))
    alto = float(input("Dime el alto del aula en metros ej:2.50 "))
try:
    pedirDatos()
except:
    print("Los datos introducidos no son validos, numeros con decimales separado por punto")
    pedirDatos()

volumen = ancho*largo*alto
print (volumen,"M³")
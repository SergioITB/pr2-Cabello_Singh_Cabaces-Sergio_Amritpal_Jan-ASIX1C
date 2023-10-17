"""
03/10/2023
ASIXc M03 UF1 A2
Descripció: Encripta las palabaras o frase por numeros.
"""
#En primer lugar pedimos al usuaruio que introduzca una palabra o frase
texto = str(input("Introduzca una palabra o frase "))
#Esta linia hace un print de la palara introducida por la palabra o frase
print(texto)
#Ahora defino un diccionario con el valor de cada vocal
listaVocales = {
        'a': '1', 'A': '1',
        'e': '2', 'E': '2',
        'i': '3', 'I': '3',
        'o': '4', 'O': '4',
        'u': '5', 'U': '5'}
#En esta lineas usamos dos funciones pre-definidas: vocal,item y replace. Entonces le indicamos que por cada vocal en la lista coja su valor y lo sustituya.
for vocal, valor in listaVocales.items():
    texto = texto.replace(vocal, valor)
print(texto)

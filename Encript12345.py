"""
Jan Cabaces Batalle
03/10/2023
ASIXc M03 UF1 A2
Descripció: Encripta las palabaras por numeros.
"""
texto = str(input("Introduzca una palabra"))
print(texto)
listaLetras = {
    'a': '1', 'A': '1',
    'e': '2', 'E': '2',
    'i': '3', 'I': '3',
    'o': '4', 'O': '4',
    'u': '5', 'U': '5',
}
for vocal, valor in listaLetras.items():
    texto = texto.replace(vocal, valor)

print(texto)
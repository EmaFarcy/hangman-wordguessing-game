# Código Juego Ahorcado

import os

palabraOculta = []
palabra = []
cantidad = 0
letra = ""
fin = False
aciertos = 0
fallos = 0

cantidad = int(
    input("Ingresar cantidad de letras: ")
)  # Jugador uno que ingresa la palabra oculta y se agrega al vector palabra.
for i in range(0, cantidad):
    msj = "Ingresar letra " + str(i + 1) + " : "
    letra = input(msj)
    palabraOculta.append(letra)
    palabra.append("-")
    os.system("cls")

msj = ""
while fin == False:
    msj = ""
    for i in range(0, len(palabra)):
        msj = msj + " " + palabra[i]

    print(msj)
    b = 0
    letra = input("Ingresar letra: ")
    for i in range(0, len(palabraOculta)):
        if letra == palabraOculta[i] and palabra[i] == "-":
            palabra[i] = letra
            aciertos = aciertos + 1
            b = 1
        if letra == palabraOculta[i]:
            b = 1
    if b == 0:
        fallos = fallos + 1

    if fallos == 5:
        fin = True
    if aciertos == cantidad:
        fin = True

msj = ""
for i in range(0, len(palabraOculta)):
    msj = msj + " " + palabraOculta[i]
print("La palabra era: ", msj)

if aciertos == cantidad:
    print("Felicitaciones, adivinaste!")
else:
    print("Lo siento. Vuelve a intentarlo")

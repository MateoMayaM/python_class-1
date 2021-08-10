# list1 = []
# list2 = []
# list3 = list1
# if list1 == list2:
#    print("True")
# else:
#    print("False")
# if list1 is list2:
#    print("True")
# else:
#    print("False")
# if list1 is list3:
#    print("True")
# else:
#    print("False")

# Script para jugar piedra, papel o tijera (tomando una librería que dé valores al azar y comparar palabras).
# 1. Descargar la librería.
import random

# 2. Pedirle algo al usuario.
jugar_de_nuevo = "si"
counter = 0
while jugar_de_nuevo == "si" and counter <= 3:
    print("Escoja piedra, papel o tijeras: ")
    usuario = input()

# 3. Definir opciones.
    posibilidades = ["piedra", "papel", "tijeras"]

# 4. Elegir opción con la computadora.
    computadora = random.choice(posibilidades)

# Imprimir resultado.
    print("El usuario eligió " + str(usuario) + " y la computadora eligió " + str(computadora))

# Hacer comparaciones.
    if usuario == computadora:
        print("Es un empate")
    elif usuario == "piedra":
        if computadora == "tijeras":
            print("Piedra gana a tijeras: ¡El usuario ganó! :D")
        else:
            print("Papel gana a piedra: Gana la computadora :(")
    elif usuario == "papel":
        if computadora == "tijeras":
            print("Tijeras gana a papel: Gana la computadora :(")
        else:
            print("Papel gana a piedra: ¡El usuario ganó! :D")
    elif usuario == "tijeras":
        if computadora == "piedra":
            print("Piedra gana a tijeras: Gana la computadora :(")
        else:
            print("Tijeras gana a papel: ¡El usuario ganó! :D")

    print("¿Quiere jugar de nuevo? si/no")
    jugar_de_nuevo = input()
    counter += 1

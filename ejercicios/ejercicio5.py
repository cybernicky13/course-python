# Adivina el número: Escribe un programa que genere un número aleatorio y le pida al usuario que adivine qué número es. 
# El programa debe indicar si el número ingresado es demasiado alto o demasiado bajo, y permitir al usuario seguir adivinando hasta que adivine el número correcto.

import random

numero_secreto = random.randint(1, 100)
adivinanza = False

while not adivinanza:
    intento = int(input("Adivina el numero (entre 1 y 100): "))

    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        adivinanza = True
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta nuevamente.")
    else:
        print("Demasiado alto. Intenta nuevamente.")


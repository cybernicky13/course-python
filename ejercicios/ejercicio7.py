#Comprobador de palíndromos: Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo.
# Un palíndromo es una palabra que se lee igual de izquierda a derecha y de derecha a izquierda.

palabra = input("Ingrese una palabra: ")

reversa = palabra[::-1]

if palabra == reversa:
    print("La palabra", palabra, "es un palíndromo.")
else:
    print("La palabra", palabra, "no es un palíndromo.")

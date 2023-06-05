# Calculadora de factorial: Escribe un programa que solicite al usuario un número entero y calcule su factorial. 
# El factorial de un número se calcula multiplicando todos los números enteros desde 1 hasta el número dado.

numero = int(input("Ingrese un número entero: "))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print("El factorial de", numero, "es:", factorial)

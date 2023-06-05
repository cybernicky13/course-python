# Conversor de temperatura: Escribe un programa que convierta una temperatura en grados Celsius a grados Fahrenheit. 
# El programa debe solicitar al usuario la temperatura en grados Celsius y mostrar la equivalente en grados Fahrenheit.

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("La temperatura equivalente en grados Fahrenheit es: ", fahrenheit)
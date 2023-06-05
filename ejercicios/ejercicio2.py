# Contador de palabras: Crea un programa que solicite al usuario una oración y cuente cuántas palabras contiene. 
# Puedes asumir que las palabras están separadas por espacios.

oracion = input("Ingrese una oracion: ")
palabras = oracion.split()

cantidad_palabras = len(palabras)

print("La cantidad de palabras en la oracion es: ", cantidad_palabras)
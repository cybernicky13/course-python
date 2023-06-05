# Generador de contraseñas: Crea un programa que genere contraseñas aleatorias. 
# El programa debe permitir al usuario especificar la longitud de la contraseña y mostrar la contraseña generada.

import random
import string

logitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
contrasenia = ''.join(random.choice(caracteres) for _ in range(logitud))

print("La contraseña generada es: ", contrasenia)
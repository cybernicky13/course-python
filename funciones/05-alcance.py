saludo = "Hola Global"


def saludar():
    global saludo
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


print(saludo)
saludar()
print(saludo)

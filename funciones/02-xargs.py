def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(13, 7, 21)
suma(13, 7)
suma(13, 7, 21, 66, 77)

numeros = [2, 13, 7, 11, 21, 23]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)


usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)

# lista = [1, 2, 3, 4]
# tupla = (1, 2, 3, 4)
# print(1, 2, 3, 4)
# print(*lista)
# print(*tupla)

# lista2 = [5, 6]

# combinada = ["hola", *lista, "mundo", *lista2, "chanchito"]
# print(combinada)


punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}
print(nuevoPunto)

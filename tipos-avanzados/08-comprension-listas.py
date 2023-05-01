usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]

# nombres = []
# for usuario in usuarios:
# nombres.append(usuarios[0])
# print(nombres)

# nombres = [usuario[0] for usuario in usuarios]

# filtrar
# nombres = [usuario for usuario in usuarios if usuario[0] > 2]

# nombres = list(map(lambda usuario: usuario[0], usuarios))

menos_usuarios = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(menos_usuarios)

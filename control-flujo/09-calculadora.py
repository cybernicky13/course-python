"""CyberCalculadora by Nicolas Del Valle"""

# OPERACIONES = "Las Operaciones son suma, resta, multi, div"

# print("""Bienvenidos a la CyberCalculadora :)
#          Para salir escribe Salir
#          """ + OPERACIONES)

# RESULTADO = input("Ingresa el primer numero: ")
# RESULTADO = int(RESULTADO)
# OP = "salir"
# N2 = ""

# while OP.lower() or N2.lower() != "salir":
#     OP = input("Ingrese la operacion: ")
#     N2 = input("Ingrese el siguiente numero: ")
#     if OP.lower() == "suma":
#         RESULTADO += int(N2)
#     elif OP.lower() == "resta":
#         RESULTADO -= int(N2)
#     elif OP.lower() == "multi":
#         RESULTADO *= int(N2)
#     elif OP.lower() == "div":
#         RESULTADO /= int(N2)
#     elif OP.lower() or N2.lower() == "salir":
#         break
#     else:
#         RESULTADO = "Debe Ingresar una operación valida" + OPERACIONES
#     print(RESULTADO)


# """CyberCalculadora Resuelto by Nicolas Del Valle"""

print("Bienvenidos a la CyberCalculadora :D")
print("Para salir escribe salir")
print("Las Operaciones son suma, resta, multi, div")

RESULTADO = ""

while True:
    if not RESULTADO:
        RESULTADO = input("Ingrese el primer número: ")
        if RESULTADO.lower() == "salir":
            break
        RESULTADO = int(RESULTADO)
    OP = input("Ingrese la operación: ")
    if OP.lower() == "salir":
        break
    N2 = input("Ingrese siguiente número: ")
    if N2.lower() == "salir":
        break
    N2 = int(N2)

    if OP.lower() == "suma":
        RESULTADO += N2
    elif OP.lower() == "resta":
        RESULTADO -= N2
    elif OP.lower() == "multi":
        RESULTADO *= N2
    elif OP.lower() == "div":
        RESULTADO /= N2
    else:
        print("Operacion no válida")
        break

    print(f"El resultado es: {RESULTADO}")

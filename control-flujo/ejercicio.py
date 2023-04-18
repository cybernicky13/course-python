print("""Bienvenidos a la CyberCalculadora :)
         Para salir escribe Salir
         Las Operaciones son suma, resta, multi, div""")

resultado = input("Ingresa el primer numero: ")
resultado = int(resultado)
op = ""
n2 = ""

while op.lower() or n2.lower() != "salir":
    op = input("Ingrese la operacion: ")
    n2 = input("Ingrese el siguiente numero: ")
    if op.lower() == "suma":
        resultado += int(n2)
    elif op.lower() == "resta":
        resultado -= int(n2)
    elif op.lower() == "multi":
        resultado *= int(n2)
    elif op.lower() == "div":
        resultado /= int(n2)
    print(resultado)

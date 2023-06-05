try:
    n1 = int(input("Ingrese el primer numero: "))
except ValueError as ex:
    print("Ingrese un valor correcto")
except NameError as ex:
    print("Ocurrio un error")   
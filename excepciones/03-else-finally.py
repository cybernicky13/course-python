try:
    n1 = int(input("Ingrese el primer numero: "))
except Exception as ex:
    print("Ocurrio un error")
else:
    print("No ocurrio ningun error")
finally:
    print("Se ejecuta siempre!")   
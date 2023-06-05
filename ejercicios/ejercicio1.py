# Calculadora de propina: Escribe un programa que solicite al usuario el total de una cuenta de restaurante y la cantidad de propina que desea dejar. 
# El programa debe calcular y mostrar el monto total a pagar, incluyendo la propina.

total = float(input("Ingrese el total de la cuenta: "))
propina = float(input("Ingrese el porcentaje de propina a dejar: "))

monto_propina = total * (propina / 100)
total_a_pagar = total + monto_propina

print("El monto total a pagar es: ", total_a_pagar)




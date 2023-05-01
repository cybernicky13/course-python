numeros = [1, 2, 3]

#Horrible
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

primero, *otros = numeros
print(primero, otros)

primero, segundo, *otros = numeros
print(primero, segundo)

primero, *otros, ultimo = numeros
print(primero, ultimo)
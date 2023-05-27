# """CyberFunctions by Nicolas Del Valle"""


# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes
# def deleteSpaces(word):
# newWord = ""
# for char in word:
# if char != " ":
# newWord += char
# return newWord
# return list(newWord)


# print(deleteSpaces("Devil Man"))

# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string


# def countCharacters(word):
# word = word.lower()
# count = {}
# for character in word:
# count[character] = count.get(character, 0) + 1
# return count


# print(countCharacters("Alucard"))

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas


# def sortDictionary(dictionary):
# orderedList = sorted(dictionary.items(), key=lambda x: x[1])
# return orderedList


# diccionario = {"a": 5, "b": 2, "c": 8, "d": 1}
# print(sortDictionary(diccionario))

# 4. De un listado de tuplas, devolver las tuplas
# que tengan el mayor valor


# def superiorTuple(listOfTuples):
# tuples = max(listOfTuples, key=lambda x: x[1])
# return tuples


# listado = [("a", 5), ("b", 2), ("c", 8), ("d", 1)]
# print(superiorTuple(listado))

# 5. Crear un mensaje que diga:
# Los caracteres que mas ser repiten con 4 repeticiones son :
# -C
# -D


# def repeatingCharacters(listOfTuples, repetitions):
# repetitions = max(repetitions, 1)
# characters = [tupla[0] for tupla in listOfTuples if tupla[1] >= repetitions]
# if characters:
# message = f"Los caracteres que se repiten al menos {repetitions} veces son: {', '.join(characters).upper()}"
# else:
# message = f"No hay caracteres que se repitan al menos {repetitions} veces."
# return message


# listado = [("a", 5), ("b", 2), ("c", 8), ("d", 1), ("e", 4), ("f", 3), ("g", 5)]

# mensaje = repeatingCharacters(listado, 4)
# print(mensaje)

# 6. Juntar la solucion de los ejercicios anteriores
# para encontrar los caracteres que mas se repiten
# de un string

# """CyberFunctions Resuelto by Nicolas Del Valle"""

from pprint import pprint

string = "Hola Mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    repuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        repuesta[orden[0]] = orden[1]
        return repuesta


def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje = f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)

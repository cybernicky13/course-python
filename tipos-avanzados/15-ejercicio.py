# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes
def deleteSpaces(word):
    newWord = ""
    for char in word:
        if char != " ":
            newWord += char
    return list(newWord)


print(deleteSpaces("Devil Man"))

# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string


def countCharacters(word):
    word = word.lower()
    count = {}
    for character in word:
        count[character] = count.get(character, 0) + 1
    return count


print(countCharacters("Alucard"))

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas


def sortDictionary(dictionary):
    orderedList = sorted(dictionary.items(), key=lambda x: x[1])
    return orderedList


diccionario = {"a": 5, "b": 2, "c": 8, "d": 1}
print(sortDictionary(diccionario))

# 4. De un listado de tuplas, devolver las tuplas
# que tengan el mayor valor


def superiorTuple(listOfTuples):
    tuple = max(listOfTuples, key=lambda x: x[1])
    return tuple


listado = [("a", 5), ("b", 2), ("c", 8), ("d", 1)]
print(superiorTuple(listado))

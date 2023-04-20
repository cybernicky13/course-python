"""CyberPalindromo by Nicolas Del Valle"""


# def es_palindormo(texto):
#     """Esta es una funcion para saber si un string es palindromo"""
#     texto = texto.replace(" ", "").lower()
#     string_reverse = texto[::-1]

#     is_palindromo = True if string_reverse == texto else False
#     return is_palindromo


# print("abba", es_palindormo("abba"))
# print("amo la paloma", es_palindormo("amo la paloma"))
# print("rock", es_palindormo("rock"))
# print("ReconOcer", es_palindormo("ReconOcer"))
# print("diego", es_palindormo("diego"))


# """CyberPalindromo Resuelto by Nicolas Del Valle"""

def no_space(texto):
    """Esta Funcion es para eliminar espacios"""
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    """Esta funcion es para dar vuelta al texto"""
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    """Esta funcion determina si una palabra es un palindromo"""
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


es_palindromo("abba")
es_palindromo("rock")

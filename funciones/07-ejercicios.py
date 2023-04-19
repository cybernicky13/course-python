"""CyberPalindromo by Nicolas Del Valle"""


def es_palindormo(texto):
    """Esta es una funcion para saber si un string es palindromo"""
    string_reverso = texto[::-1]

    is_palindromo = True if string_reverso == texto else False
    return is_palindromo


print("abba", es_palindormo("abba"))
print("rock", es_palindormo("rock"))

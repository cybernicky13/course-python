"""CyberPalindromo by Nicolas Del Valle"""


def es_palindormo(texto):
    """Esta es una funcion para saber si un string es palindromo"""
    texto = texto.replace(" ", "").lower()
    string_reverse = texto[::-1]

    is_palindromo = True if string_reverse == texto else False
    return is_palindromo


print("abba", es_palindormo("abba"))
print("amo la paloma", es_palindormo("amo la paloma"))
print("rock", es_palindormo("rock"))
print("ReconOcer", es_palindormo("ReconOcer"))
print("diego", es_palindormo("diego"))

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Ciao perro :( {self.nombre}")

    def __str__(self):
        return f"Clase del perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Berserk", 13)
del mi_perro

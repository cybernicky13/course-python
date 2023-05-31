class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice Guau!")


Perro.patas = 5
mi_perro = Perro("guts", 1)
mi_perro.patas = 6
print(Perro.patas)
print(mi_perro.patas)

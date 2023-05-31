class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Caska", 10)


Perro.habla()
perro1 = Perro("Guts", 13)
perro2 = Perro("Puck", 7)
perro3 = Perro.factory()
print(perro3.nombre, perro3.edad)

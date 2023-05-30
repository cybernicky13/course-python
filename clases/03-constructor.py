class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def habla(self):
        print("Guau!")


mi_perro = Perro("guts")
mi_perro2 = Perro("puck")
print(mi_perro.nombre)
print(mi_perro2.nombre)

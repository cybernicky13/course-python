class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


guitarra = Producto("DoomGuitar", 1300)
bateria = Producto("DoomDrums", 6000)
bajo = Producto("DoomBase", 7770)
musica = Categoria("Rock", [guitarra, bateria])
musica.agregar(bajo)
musica.imprimir()

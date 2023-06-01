class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, la tabla no ha sido definida")

    def guardar(self):
        print(f"Guardando {self.tabla} en BD")

    @classmethod
    def buscar_x_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_x_id(13)

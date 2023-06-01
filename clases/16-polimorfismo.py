from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("Guardando usuario en BD")


class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar([usuario, sesion])

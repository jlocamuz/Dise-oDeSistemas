# CLASE ABSTRACTA TV
from abc import ABC, abstractmethod

class AbstractTV(ABC):
    @abstractmethod
    def __init__(self, descripcion, marca, pulgadas, precio, color=''):
        pass
    # como parametro obj clase Tv
    @abstractmethod
    def desc(self, c):
        pass

class LCD(AbstractTV):
    def __init__(self, descripcion, marca, pulgadas, precio, color=''):
        self.descripcion = descripcion
        self.marca = marca
        self.pulgadas = pulgadas
        self.precio = precio
        self.color = color

    # c objeto Color
    def desc(self, c):
        print('LCD de color {}'.format(c))

class Plasma(AbstractTV):
    def __init__(self, descripcion, marca, pulgadas, precio, color=''):
        self.descripcion = descripcion
        self.marca = marca
        self.pulgadas = pulgadas
        self.precio = precio
        self.color = color

    # c objeto Color
    def desc(self, c):
        print('Plasma de color {}'.format(c))


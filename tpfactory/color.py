from abc import ABC, abstractmethod

class AbstractColor(ABC):
    @abstractmethod
    def __init__(self,descripcion):
        pass

    # como parametro obj clase Tv
    @abstractmethod
    def colorea(self, tv):
        pass

class Amarillo(AbstractColor):
    def __init__(self, descripcion):
        self.descripcion = descripcion

    # tv = obj Tv
    def colorea(self, tv): 
        tv.color = 'amarillo'
        print('pintando el {} ({}) de color AMARILLO'.format(tv.descripcion , tv))

class Azul(AbstractColor):
    def __init__(self, descripcion):
        self.descripcion = descripcion

    # tv = obj Tv
    def colorea(self, tv): 
        tv.color = 'azul'
        print('pintando el {} ({}) de color AZUL'.format(tv.descripcion, tv))


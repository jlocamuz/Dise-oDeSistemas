from abc import ABC, abstractmethod
import tv, color

class TvAbstractFactory(ABC):
	@abstractmethod
	def create_color(self):
		pass
	@abstractmethod
	def create_tv(self):
		pass
	@abstractmethod
	def imprimir(self):
		pass


class FactoryPlasmaAzul(TvAbstractFactory):
	def create_color(self):
		self.color = Azul('azul')
		self.color.colorea(self.tv)	
	def create_tv(self):
		self.tv = Plasma("Plasma","Huawei", 42.3 , 10.000, "azul")

	def imprimir(self):
		print('{} marca {} de color {}'.format(self.tv.descripcion, self.tv.marca, self.color.descripcion))
class FactoryLCDAmarillo(TvAbstractFactory):
	def create_color(self):
		self.color = color.Amarillo('amarillo')
		self.color.colorea(self.tv)
	def create_tv(self):
		self.tv = tv.LCD("LCD","Samsung", 47.4 , 20.000, "amarillo")
	def imprimir(self):
		print('{} marca {} de color {}'.format(self.tv.descripcion, self.tv.marca, self.color.descripcion))
if __name__ == '__main__':
	lcd1 = FactoryLCDAmarillo()
	lcd1.create_tv()
	lcd1.create_color()
	lcd1.imprimir()
	print(lcd1.color, lcd1.tv)

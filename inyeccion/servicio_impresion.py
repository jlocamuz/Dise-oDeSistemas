from servicio_envio import ServicioEnvio
from servicio_pdf import ServicioPDF

class ServicioImpresion():
    def __init__(self, A=ServicioEnvio, B=ServicioPDF):
        self.servicioA = A
        self.servicioB = B
    
    def imprimir(self):
        print('Imprimiendo... \nSERVICIO A: {}\nSERVICIO B:{}'.format(self.servicioA, self.servicioB))
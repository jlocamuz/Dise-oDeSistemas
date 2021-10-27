# inyectar las dependencias al ServicioImpresión y que no sea él el que tenga que definirlas en el constructor.

import servicio_impresion
import servicio_envio
import servicio_pdf

if __name__ == '__main__':
    servicioA = servicio_pdf.ServicioPDF()
    servicioB = servicio_envio.ServicioEnvio()
    servicioI = servicio_impresion.ServicioImpresion(servicioB, servicioA)
    servicioI.imprimir()
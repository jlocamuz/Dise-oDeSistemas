# boolean isMutant(String[] dna);

# En donde recibirás como parámetro un array de Strings que representan cada fila de una tabla
# de (NxN) con la secuencia del ADN

# String[] dna = {"ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"};

# Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada
# base nitrogenada del ADN.
# Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras
# iguales, de forma oblicua, horizontal o vertical.

import random
import numpy as np
import generador_dna
import mutant
            

if __name__ == '__main__':
    dna = generador_dna.random_dna(6)
    print(dna , '\n')
    print(mutant.is_mutant(dna))

    #if (mutant.is_mutant(dna)) == True: 
     #   print('ES MUTANTE')
    #else:
     #   print('NO ES MUTANTE')

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

def random_dna():
    base = ['A','T','C','G']
    dna = []
    for _ in range(6):
        lista = []
        for _ in range(6): 
            lista.append(random.choice(base))
        dna.append(lista)
    return np.array(dna) # matriz
            


def is_mutant(dna):
    # diagonales 
    d_inferior_2 = dna.diagonal(-2)
    d_inferior_1 =  dna.diagonal(-1)
    d_ppal = dna.diagonal()
    d_1 = dna.diagonal(1)
    d_2 = dna.diagonal(2)
    
    # diagonales invertidas
    d_inferior_rev_2 = np.fliplr(dna).diagonal(-2)
    d_inferior_rev_1 = np.fliplr(dna).diagonal(-1)
    d_ppal_rev = np.fliplr(dna).diagonal()
    d_rev_1 = np.fliplr(dna).diagonal(1)
    d_rev_2 = np.fliplr(dna).diagonal(-2)

    d_2_list = [d_inferior_2, d_2, d_inferior_rev_2, d_rev_2]
    d_1_list = [d_inferior_1, d_1, d_inferior_rev_1, d_rev_1]
    d_ppal_list = [d_ppal, d_ppal_rev]

    # diagonales 2
    for i in d_2_list:
        if len(set(i)) == 1:
            return True
    #diagonales 1
    for i in d_1_list:
        if len(set(i[0:4])) == 1 or len(set(i[1:5])) == 1: 
            return True
    #diagonales ppales
    for i in d_ppal_list:
        if len(set(i[0:4])) == 1 or len(set(i[1:5])) == 1 or len(set(i[2:6])) == 1: 
            return True
    #filas
    for i in dna:
        if len(set(i[0:4])) == 1 or len(set(i[1:5])) == 1 or len(set(i[2:6])) == 1: 
            return True
    #columnas
    for i in range(len(dna[1,:])):
        if len(set((dna[:, i])[0:4])) == 1 or len(set((dna[:, i])[1:5])) == 1 or len(set((dna[:, i])[2:6])) == 1:
            return True
 

    return False

if __name__ == '__main__':
    dna = random_dna()
    print(dna , '\n')

    if (is_mutant(dna)) == True: 
        print('ES MUTANTE')
    else:
        print('NO ES MUTANTE')

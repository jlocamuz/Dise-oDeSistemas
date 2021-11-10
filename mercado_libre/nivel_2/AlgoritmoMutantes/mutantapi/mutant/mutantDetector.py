import random
import numpy as np


def get_dna(DNA):
    source = DNA
    dna = []
    for i in source:
        lista = []
        for j in i: 
            lista.append(j)
        dna.append(lista)
    return np.array(dna)

def is_mutant(dna):
    # transponer me sirve para iterar mas facil sobre columnas 
    dna_t = np.transpose(dna)
    dimension = (np.shape(dna))[0]
    d = dimension-4 

    for i in range(-d,d+1):
        if len(set(dna.diagonal(i))) == 1 or len(set(np.fliplr(dna).diagonal(i))) ==1:
            return True
    for i in zip(dna, dna_t):
        inicio = 0
        final = 4
        for _ in range(dimension-3):
            fila = (i[0])[inicio:final]
            columna = (i[1])[inicio:final]
            if len(set(fila)) == 1 or len(set(columna)) == 1:
                return True
            inicio += 1
            final += 1 

    return False
if __name__ == "__main__":
    DNA = get_dna()
    print(is_mutant(DNA))

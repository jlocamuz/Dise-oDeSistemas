import random
import numpy as np

def random_dna(n):
    base = ['A','T','C','G']
    dna = []
    for _ in range(n):
        lista = []
        for _ in range(n): 
            lista.append(random.choice(base))
        dna.append(lista)
    return np.array(dna) # matriz
            
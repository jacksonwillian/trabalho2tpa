from algoritmo import heapsort
from algoritmo import quicksort
from algoritmo import insertsort

import math as math_

def introsort(a):
    n = len(a) - 1
    profundidade_max = math_.floor(math_.log2(len(a))) * 2
    introsort_(a, 0, n, profundidade_max)

def introsort_(a, ini, fin, profundidade_max):
    pass




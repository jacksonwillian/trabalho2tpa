from algoritmo import heapsort
from algoritmo import quicksort
from algoritmo import insertsort

import math as math_

def f_introsort(a, arg1, arg2):
    # INICIALIZACAO DO CONTEUDO DAS VARIAVEIS GLOBAIS
    global f_comparacao
    global v_coluna
    f_comparacao = arg1
    v_coluna = arg2
    n = len(a) - 1

    profundidade_max = math_.floor(math_.log2(len(a))) * 2
    introsort_(a, 0, n, profundidade_max)

def introsort_(a,ini, fin, profundidade_max):
    ##Esse 20 depende do que estamos ordenando é o limite em que vale a pena usar o insertion sort
    t_vetor = len(a)
    if t_vetor <= 20:
        insertsort.f_insertsort(a,f_comparacao, v_coluna)
    if profundidade_max == 0:
        heapsort.f_heapsort(a, f_comparacao, v_coluna)
    else:
        if (fin > ini):
            i_part = quicksort.particiona(a,ini, fin, f_comparacao, v_coluna)
            introsort_(a, ini, i_part-1, profundidade_max -1)
            introsort_(a,i_part+1, fin, profundidade_max -1)


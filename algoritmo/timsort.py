# N = Comprimento so vetor de entrada
# RUN = Subvetor ordenado que compõe o vetor de entrada
# Minrun = É o comprimento minimo dos runs.Este numero é calculado baseado no tamanho do vetor.

# DECLARACAO DAS VARIAVEIS GLOBAIS
f_comparacao = None
v_coluna = None
RUN = 0

def calculaRun(tam):
    run = 32
    resultado = (tam // run) % 2 
    while resultado != 0 and (tam > run and run < 64):
        run = run + 1
        resultado = (tam // run) % 2
    return run

def merge(lado_esq,lado_dirt):

    index_dir     = 0
    index_esq     = 0
    tam_esq       = len(lado_esq)
    tam_dir       = len(lado_dirt)
    new_lst       = []
    
    while (index_esq < tam_esq) and (index_dir < tam_dir):
        if(   f_comparacao( lado_esq[index_esq][v_coluna], lado_dirt[index_dir][v_coluna])  == -1) :
            new_lst.append(lado_esq[index_esq])
            index_esq+=1    
        else:
            new_lst.append(lado_dirt[index_dir])
            index_dir+=1
    new_lst += lado_dirt[index_dir:]
    new_lst += lado_esq[index_esq:]
    return new_lst


def insertSort(lista):
    for i in range(1,len(lista)):
        chave = lista[i]
        j = i-1
        while( j >= 0)  and ( f_comparacao( chave[v_coluna], lista[j][v_coluna]) == -1 ):
            lista[j+1] = lista[j]
            j = j -1
        lista[j+1] = chave
    return lista


def f_timsort(lst, arg1, arg2):
    lado_esq     = []
    lado_dirt     = []
    tam         = len(lst)

    # INICIALIZACAO DO CONTEUDO DAS VARIAVEIS GLOBAIS
    global f_comparacao
    global v_coluna
    global RUN
    f_comparacao = arg1
    v_coluna = arg2
    RUN = calculaRun(tam)
    
    resto = tam % RUN  # CALCULA O RESTO
    
    if(tam <= (RUN + resto)):  # SE O TAMANHO DO VETOR É MENOR QUE O RESTO MAIS O TAMANHO, ENTÃO  FAZ UM SUBBLOCO SÓ DO TAMANHO DO VETOR TODO
        lst[0:tam] = insertSort(lst[0:tam])
    else:    
        lst[0:(RUN + resto)] = insertSort(lst[0:(RUN + resto)])  # O primeiro bloco é o RUN + O RESTO
        for i in range ((RUN + resto), tam, RUN): # A posição do segundo comçea com RUN + RESTO, da em diante é normal
            lst[i:i+RUN] = insertSort(lst[i:i+RUN])

    while ((RUN + resto) < tam):
      
        iprincipal = 0
        fprincipal = (2*RUN + resto)
        ei = 0
        ef = RUN + resto
        di = (RUN + resto)
        df = (2*RUN + resto)
    
        lst[ iprincipal : fprincipal] = merge( lst[ ei:  ef], lst[ di : df])
    
        for x in range (df, tam, 2*RUN):
    
            iprincipal = x
            fprincipal = x + 2*RUN
            ei = iprincipal
            ef = x + RUN
            di = ef
            df = fprincipal
    
            lst[iprincipal :  fprincipal ] = merge(lst[ei : ef],  lst[ di: df])  # Intercalar sempre o vetor anterior com o próximo vetor.
        
        RUN += RUN  # Quando acontece o merge o tamanho da RUN vai aumentando até RUN == tamanho do vetor 

    return lst


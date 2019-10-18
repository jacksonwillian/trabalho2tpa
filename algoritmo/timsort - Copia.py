# N = Comprimento so vetor de entrada
# RUN = Subvetor ordenado que compõe o vetor de entrada
# Minrun = É o comprimento minimo dos runs.Este numero é calculado baseado no tamanho do vetor.
import os


RUN = 32
import random

def merge(lado_esq,lado_dirt):

    index_dir     = 0
    index_esq     = 0
    tam_esq        = len(lado_esq)
    tam_dir        = len(lado_dirt)
    new_lst     = []
    
    while index_esq < tam_esq and index_dir < tam_dir:
            
        if(lado_esq[index_esq] < lado_dirt[index_dir]):
            
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

    while( j >= 0 and lista[j] > chave):
    
        lista[j+1] = lista[j]
        j = j -1
  
    lista[j+1] = chave
   
  return lista

def timSort(lst):
    
    sub_lst     = []
    lado_esq     = []
    lado_dirt     = []
    tam         = len(lst)
    
    
    resto = tam % RUN  # CALCULA O RESTO
    
    if(tam <= (RUN + resto)):  # SE O TAMANHO DO VETOR É MENOR QUE O RESTO MAIS O TAMANHO
                             # ENTÃO  FAZ UM SUBBLOCO SÓ DO TAMANHO DO VETOR TODO
        
        lst[0:tam] = insertSort(lst[0:tam])
        
    else:    
        
        lst[0:(RUN + resto)] = insertSort(lst[0:(RUN + resto)])  # o primeiro bloco é o RUN + O RESTO
         
        for i in range ((RUN + resto), tam, RUN): # O segundo em diante é normal, mas o segundo começa apos o primeiro´que é o RUN + RESTO
    
            lst[i:i+RUN] = insertSort(lst[i:i+RUN])
                    



    iprincipal = 0
    fprincipal = (2*RUN + resto)
    
    ei = 0
    ef = RUN + resto
    
    di = (RUN + resto)
    df = (2*RUN + resto)

    lst[ iprincipal : fprincipal] = merge( lst[ ei:  ef], lst[ di : df])

    for x in range ((2*RUN + resto), (tam + RUN ), RUN):
            
            
        iprincipal = 0
        fprincipal = x + RUN
      
        ei = 0
        ef = x
    
        di = x
        df = fprincipal

        lst[iprincipal :  fprincipal ] = merge(lst[ei : ef],  lst[ di: df])  # Intercalar sempre o vetor anterior com o próximo vetor.

        
    return lst    






def ordenado(lista):

    for i in range(len(lista)-1):

        if (lista[i] > lista[i+1]):
            return False
    return True



def main():


    
    while (True):
        # l = [0, 0, 1, 7, 8, 11, 12, 13, 14, 14, 17, 20, 21, 24, 24, 25, 25, 25, 27, 27, 28, 28, 29, 30, 32, 32, 35, 36, 36, 38, 38, 39, 40, 41, 41, 41, 42, 42, 42, 45, 46, 46, 47, 48, 49, 49, 52, 53, 54, 56, 57, 58, 59, 61, 61, 63, 63, 65, 65, 66, 67, 67, 68, 69, 70, 70, 70, 71, 72, 72, 73, 75, 79, 80, 83, 84, 90, 93, 96, 96, 6, 21, 23, 26, 28, 29, 32, 34, 35, 37, 39, 39, 40, 43, 46, 46, 49, 50, 61, 65, 65, 65, 67, 70, 72, 76, 78, 79, 80, 94, 94, 96]
        l = []
        tamanho = random.randint(900000000,9000000000)
        for i in range(tamanho):
        	l.append(random.randint(0,21))
        print(tamanho)
        print(l)
        print("Ordenado lista: {}".format(ordenado(l)))

        print()
        l = timSort(l)
        print(l)
        print("Ordenado lista: {}".format(ordenado(l)))
        input("\nEnter pra gerar outros valores ou CTRL + C para sair")

		

    return 0

main()


#FUNCIONANDO
# RUN = 32
# import random

# def merge(lado_esq,lado_dirt):

#     index_dir     = 0
#     index_esq     = 0
#     tam_esq        = len(lado_esq)
#     tam_dir        = len(lado_dirt)
#     new_lst     = []
    
#     while index_esq < tam_esq and index_dir < tam_dir:
            
#         if(lado_esq[index_esq] < lado_dirt[index_dir]):
            
#             new_lst.append(lado_esq[index_esq])
#             index_esq+=1    
        
#         else:

#             new_lst.append(lado_dirt[index_dir])
#             index_dir+=1
        
#     new_lst += lado_dirt[index_dir:]
#     new_lst += lado_esq[index_esq:]
    
#     return new_lst


# def insertSort(lista):

#   for i in range(1,len(lista)):
    
#     chave = lista[i]
#     j = i-1

#     while( j >= 0 and lista[j] > chave):
    
#         lista[j+1] = lista[j]
#         j = j -1
  
#     lista[j+1] = chave
   
#   return lista

# def timSort(lst):
    
#     sub_lst     = []
#     lado_esq     = []
#     lado_dirt     = []
#     tam         = len(lst)
    
    
#     resto = tam % RUN  # CALCULA O RESTO
    
#     if(tam <= (RUN + resto)):  # SE O TAMANHO DO VETOR É MENOR QUE O RESTO MAIS O TAMANHO
#     						 # ENTÃO  FAZ UM SUBBLOCO SÓ DO TAMANHO DO VETOR TODO
        
#         lst[0:tam] = insertSort(lst[0:tam])
        
#     else:	
        
#         lst[0:(RUN + resto)] = insertSort(lst[0:(RUN + resto)])  # o primeiro bloco é o RUN + O RESTO
         
#         for i in range ((RUN + resto), tam, RUN): # O segundo em diante é normal, mas o segundo começa apos o primeiro´que é o RUN + RESTO
    
#             lst[i:i+RUN] = insertSort(lst[i:i+RUN])
                    



#     iprincipal = 0
#     fprincipal = (2*RUN + resto)
    
#     ei = 0
#     ef = RUN 
    
#     di = (RUN + resto)
#     df = (2*RUN + resto)

#     lst[ iprincipal : fprincipal] = merge( lst[ ei:  ef], lst[ di : df])

#     for x in range (iprincipal + RUN, (tam + RUN ), RUN):
            
            
#         iprincipal = 0
#         fprincipal = x
      
#         ei = 0
#         ef = x - RUN
    
#         di = x - RUN
#         df = fprincipal

#         lst[iprincipal :  fprincipal ] = merge(lst[ei : ef],  lst[ di: df])  # Intercalar sempre o vetor anterior com o próximo vetor.

        
#     return lst    






# def ordenado(lista):

# 	for i in range(len(lista)-1):

# 		if (lista[i] > lista[i+1]):
# 			return False
# 	return True



# def main():


	
# 	while (True):
# 		l = []
# 		tamanho = random.randint(0,101)
# 		for i in range(tamanho):
# 		    l.append(random.randint(0,99))
# 		print(tamanho)
# 		print(l)
# 		print("Ordenado lista: {}".format(ordenado(l)))

# 		print()

# 		l = timSort(l)
# 		print(l)
# 		print("Ordenado lista: {}".format(ordenado(l)))

# 		input("\nEnter pra gerar outros valores ou CTRL + C para sair")

		
# 	return 0

# main()








# RUN = 5
# import random

# def merge(lado_esq,lado_dirt):

#     index_dir     = 0
#     index_esq     = 0
#     tam_esq        = len(lado_esq)
#     tam_dir        = len(lado_dirt)
#     new_lst     = []
    
#     while index_esq < tam_esq and index_dir < tam_dir:
            
#         if(lado_esq[index_esq] < lado_dirt[index_dir]):
            
#             new_lst.append(lado_esq[index_esq])
#             index_esq+=1    
        
#         else:

#             new_lst.append(lado_dirt[index_dir])
#             index_dir+=1
        
#     new_lst += lado_dirt[index_dir:]
#     new_lst += lado_esq[index_esq:]
    
#     return new_lst


# def insertSort(lista):

#   for i in range(1,len(lista)):
    
#     chave = lista[i]
#     j = i-1

#     while( j >= 0 and lista[j] > chave):
    
#         lista[j+1] = lista[j]
#         j = j -1
  
#     lista[j+1] = chave
   
#   return lista

# def timSort(lst):
    
#     sub_lst     = []
#     lado_esq     = []
#     lado_dirt     = []
#     tam         = len(lst)
    
    
#     resto = tam % RUN
    
#     if(tam < (RUN + resto)):
        
#         lst[0:tam] = insertSort(lst[0:tam])
        
#     else:
        
#         lst[0:(RUN + resto)] = insertSort(lst[0:(RUN + resto)])
         
#         for i in range ((RUN + resto), tam, RUN):
    
#             lst[i:i+RUN] = insertSort(lst[i:i+RUN])
                    
#     size = RUN

#     lst[0:(2*RUN + resto) ] = merge( lst[ 0:(size + resto)], lst[ (size + resto) : (2*RUN + resto)])
#     size = size*2
    
#     while size < tam:

#         for x in range ((2*RUN + resto) ,tam, 2*size):

#                 lst[0: (x + 2*RUN) ] = merge(lst[0:(x+size)],lst[(x+size):(x+2*RUN)])

#         size = size*2
            
#     return lst    



# l = []

# for i in range(27):
#     l.append(random.randint(0,99))

# print(l)
# print()
# l = timSort(l)
# print(l)





























# RUN = 32
# import random

# def merge(lado_esq,lado_dirt):

# 	index_dir 	= 0
# 	index_esq 	= 0
# 	tam_esq		= len(lado_esq)
# 	tam_dir		= len(lado_dirt)
# 	new_lst 	= []
	
# 	while index_esq < tam_esq and index_dir < tam_dir:
			
# 		if(lado_esq[index_esq] < lado_dirt[index_dir]):
			
# 			new_lst.append(lado_esq[index_esq])
# 			index_esq+=1	
		
# 		else:

# 			new_lst.append(lado_dirt[index_dir])
# 			index_dir+=1
		
# 	new_lst += lado_dirt[index_dir:]
# 	new_lst += lado_esq[index_esq:]
	
# 	return new_lst


# def insertSort(lista):

#   for i in range(1,len(lista)):
    
#     chave = lista[i]
#     j = i-1

#     while( j >= 0 and lista[j] > chave):
    
#     	lista[j+1] = lista[j]
#     	j = j -1
  
#     lista[j+1] = chave
   
#   return lista

# def timSort(lst):
	
# 	sub_lst 	= []
# 	lado_esq 	= []
# 	lado_dirt 	= []
# 	tam 		= len(lst)






# 	for i in range (0,tam,RUN):

# 		lst[i:i+RUN] = insertSort(lst[i:i+RUN])





				
# 	size = RUN

# 	while size < tam:


# 		for x in range (0,tam,2*size):

# 				lst[x:x + 2*RUN] = merge(lst[x:x+size],lst[x+size:x+2*RUN])

# 		size = size*2
			
# 	return lst	



# l = []

# for i in range(66):
# 	l.append(random.randint(0,99))

# print(l)
# print()
# l = timSort(l)
# print(l)



'''


def timSort(arr):  
   	
	n = len(arr)
    # Classificar sub-matrizes individuais de tamanho RUN
	for i in range(0,n,RUN):
		insertionSort(arr,i,min((i+31),(n-1)))  
    
    # comece a mesclar a partir do tamanho RUN (ou 32). Vai mesclar
    # para formar o tamanho 64, 128, 256 e assim por diante ....
	size = RUN 
	while size < n:  
       
        # escolhe o ponto inicial da sub-matriz esquerda. Nós
        # vão mesclar arr [esquerda .. esquerda + tamanho-1]
        # e arr [esquerda + tamanho, esquerda + 2 * tamanho-1]
        # Após cada mesclagem, aumentamos a esquerda em 2 *
        for left in range(0,n,2*size):

            # encontra o ponto final da sub-matriz esquerda
            # mid + 1 é o ponto inicial da sub-matriz direita
			mid = left + size - 1
			right = min((left + 2*size - 1),(n-1))
    
           	# mesclar sub-matriz arr [esquerda ..... média] &
            # arr [médio + 1 .... certo] 
			merge(arr,left,mid,right)
          
		size = 2*size
'''

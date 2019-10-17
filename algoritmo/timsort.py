# N = Comprimento so vetor de entrada
# RUN = Subvetor ordenado que compõe o vetor de entrada
# Minrun = É o comprimento minimo dos runs.Este numero é calculado baseado no tamanho do vetor.

RUN = 32
import random

def merge(lado_esq,lado_dirt):

	index_dir 	= 0
	index_esq 	= 0
	tam_esq		= len(lado_esq)
	tam_dir		= len(lado_dirt)
	new_lst 	= []
	
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
	
	sub_lst 	= []
	lado_esq 	= []
	lado_dirt 	= []
	tam 		= len(lst)

	for i in range (0,tam,RUN):

		lst[i:i+RUN] = insertSort(lst[i:i+RUN])
				
	size = RUN

	while size < tam:


		for x in range (0,tam,2*size):

				lst[x:x + 2*RUN] = merge(lst[x:x+size],lst[x+size:x+2*RUN])

		size = size*2
			
	return lst	



l = []

for i in range(66):
	l.append(random.randint(0,99))

print(l)
print()
l = timSort(l)
print(l)



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

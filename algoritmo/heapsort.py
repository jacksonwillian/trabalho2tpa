# DECLARACAO DAS VARIAVEIS GLOBAIS
f_comparacao = None
v_coluna = None



# RETORNA O INDICE DO MAIOR FILHO QUE É MAIOR QUE A RAIZ
# RETORNA -1 QUANDO NÃO ENCONTRA ESSE FILHO 
def maxheap(a, i, tam):
	# CALCULA O INDICE DOS FILHOS
	maior  = -1
	
	if (((2*i) + 1) <= tam) and f_comparacao(a[((2*i) + 1)][v_coluna], a[i][v_coluna] ) == 1: 
		maior =  ((2*i) + 1)
	else:
		maior = i
		
	if (((2*i) + 2) <= tam) and f_comparacao(a[((2*i) + 2)][v_coluna], a[maior][v_coluna]) == 1:
		maior = ((2*i) + 2)
	
	if maior != i:
		a[maior], a[i] = a[i], a[maior]
		maxheap(a, maior, tam)


def f_heapsort(a, arg1, arg2):

	# INICIALIZACAO DO CONTEUDO DAS VARIAVEIS GLOBAIS
	global f_comparacao
	global v_coluna
	f_comparacao = arg1
	v_coluna = arg2

	j = len(a) - 1
	tam = len(a) - 1
	while (j > 0):
		meio = tam//2
		while (0 <= meio):
			maxheap(a, meio, j)
			meio -= 1
	
		a[0], a[j] = a[j], a[0] 
		j -= 1

	return a


# # inicial 232
# # depois 221

# # RETORNA O INDICE DO MAIOR FILHO QUE É MAIOR QUE A RAIZ
# # RETORNA -1 QUANDO NÃO ENCONTRA ESSE FILHO 
# def maxheap(a, i, j):
#     # CALCULA O INDICE DOS FILHOS
#     maior  = -1
	
#     if (((2*i) + 1) <= j) and (a[((2*i) + 1)] > a[i] ): 
#         maior =  ((2*i) + 1)
#     else:
#         maior = i
		
#     if (((2*i) + 2) <= j) and (a[((2*i) + 2)] > a[maior] ):
#         maior = ((2*i) + 2)
	
#     if maior != -1:
#         a[maior], a[i] = a[i], a[maior]
#         maxheap(a, maior, j)
		
		
	
# def f_heapsort(a):
#     j = len(a) - 1
#     while (j > 0):
#         meio = j//2
#         while (0 <= meio):
#             maxheap(a, meio, j)
#             meio -= 1
#         a[0], a[j] = a[j], a[0] 
#         j -= 1

#     return a

# #aux = a[j]
# #a[j] = a[0]
# #a[0] = aux
# #j -= 1
	
# a = [3, 8, 5, 7, 7, 7, 9, 8, 6, 4, 3, 6, 6, 4, 4, 4, 6, 9]

# f_heapsort(a)

	















# # RETORNA O INDICE DO MAIOR FILHO QUE É MAIOR QUE A RAIZ
# # RETORNA -1 QUANDO NÃO ENCONTRA ESSE FILHO 
# def posicaoMaiorFilho(a, i, j):
# 	# CALCULA O INDICE DOS FILHOS
# 	filhoEsquerdo = ((2*i) + 1) if ((2*i) + 1) <= j else -1
# 	filhoDireito = ((2*i) + 2) if ((2*i) + 2) <= j else -1

# 	# VERIFICA O FILHO MAIOR QUANDO EXISTE DOIS FILHOS
# 	if (filhoEsquerdo != -1 and filhoDireito != -1):
# 		if (a[filhoEsquerdo] > a[filhoDireito]) and (a[filhoEsquerdo] > a[i] ):
# 			return filhoEsquerdo
# 		elif(a[filhoDireito] > a[filhoEsquerdo]) and (a[filhoDireito] > a[i] ):
# 			return filhoDireito
# 		else:
# 			return -1

# 	# VERIFICA O FILHO MAIOR QUANDO NÃO EXISTE UM DOS FILHOS
# 	else:
# 		if (filhoEsquerdo != -1 ) and (a[filhoEsquerdo] > a[i] ): 
# 			return filhoEsquerdo
# 		elif (filhoDireito != -1 ) and (a[filhoDireito] > a[i] ):
# 			return filhoDireito
# 		else:
# 			return -1


# # i POSICAO DA RAIZ
# # j ULTIMA POSICAO DO VETOR
# def heap(a, i, j):
# 	posicaoMaior = posicaoMaiorFilho(a, i, j)
# 	while (posicaoMaior != -1):
# 		aux = a[posicaoMaior]
# 		a[posicaoMaior] = a[i]
# 		a[i] = aux
# 		i = posicaoMaior
# 		posicaoMaior = posicaoMaiorFilho(a, posicaoMaior, j)
# 	return a

# def f_heapsort(a):

# 	posicaoInicial = 0
# 	posicaoFinal = len(a)-1
# 	while ((posicaoFinal -1 ) >= posicaoInicial):
# 		posicaoMeio = int(posicaoFinal/2)
# 		while( posicaoInicial <= posicaoMeio):
# 			a = heap(a, posicaoMeio, posicaoFinal)
# 			posicaoMeio -=  1
# 		aux = a[posicaoFinal]
# 		a[posicaoFinal] = a[0]
# 		a[0] = aux
# 		posicaoFinal -= 1
# 	return a









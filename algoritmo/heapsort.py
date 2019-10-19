# DECLARACAO DAS VARIAVEIS GLOBAIS
f_comparacao = None
v_coluna = None


# RETORNA O INDICE DO MAIOR FILHO QUE É MAIOR QUE A RAIZ
# RETORNA -1 QUANDO NÃO ENCONTRA ESSE FILHO 
def posicaoMaiorFilho(a, i, j):
	# CALCULA O INDICE DOS FILHOS
	filhoEsquerdo = ((2*i) + 1) if ((2*i) + 1) <= j else -1
	filhoDireito = ((2*i) + 2) if ((2*i) + 2) <= j else -1

	# VERIFICA O FILHO MAIOR QUANDO EXISTE DOIS FILHOS
	if (filhoEsquerdo != -1 and filhoDireito != -1):
		if f_comparacao( a[filhoEsquerdo][v_coluna], a[filhoDireito][v_coluna] ) == 1 and f_comparacao( a[filhoEsquerdo][v_coluna], a[i][v_coluna] ) == 1:
			return filhoEsquerdo
		elif f_comparacao( a[filhoDireito][v_coluna], a[filhoEsquerdo][v_coluna] ) == 1 and f_comparacao( a[filhoDireito][v_coluna], a[i][v_coluna] ) == 1:
			return filhoDireito
		else:
			return -1

	# VERIFICA O FILHO MAIOR QUANDO NÃO EXISTE UM DOS FILHOS
	else:
		if (filhoEsquerdo != -1 ) and f_comparacao( a[filhoEsquerdo][v_coluna], a[i][v_coluna]) == 1: 
			return filhoEsquerdo
		elif (filhoDireito != -1 ) and f_comparacao( a[filhoDireito][v_coluna], a[i][v_coluna] ) == 1:
			return filhoDireito
		else:
			return -1


# i POSICAO DA RAIZ
# j ULTIMA POSICAO DO VETOR
def heap(a, i, j):
	posicaoMaior = posicaoMaiorFilho(a, i, j)
	while (posicaoMaior != -1):
		aux = a[posicaoMaior]
		a[posicaoMaior] = a[i]
		a[i] = aux
		i = posicaoMaior
		posicaoMaior = posicaoMaiorFilho(a, posicaoMaior, j)
	return a

def f_heapsort(a, arg1, arg2):

	# INICIALIZACAO DO CONTEUDO DAS VARIAVEIS GLOBAIS
	global f_comparacao
	global v_coluna
	f_comparacao = arg1
	v_coluna = arg2

	posicaoInicial = 0
	posicaoFinal = len(a)-1
	while ((posicaoFinal -1 ) >= posicaoInicial):
		posicaoMeio = int(posicaoFinal/2)
		while( posicaoInicial <= posicaoMeio):
			a = heap(a, 0, posicaoFinal)
			posicaoMeio -=  1
		aux = a[posicaoFinal]
		a[posicaoFinal] = a[0]
		a[0] = aux
		posicaoFinal -= 1

	return a















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









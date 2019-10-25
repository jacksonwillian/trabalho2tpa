# DECLARACAO DAS VARIAVEIS GLOBAIS
f_comparacao = None
v_coluna = None

def maxheap(a, i, tam):
	
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

	meio = j//2
	while (0 <= meio):
		maxheap(a, meio, j)
		meio -= 1
		
	while (j >= 0):
		a[0], a[j] = a[j], a[0]
		j -= 1
		maxheap(a, 0, j)
	 
	return a

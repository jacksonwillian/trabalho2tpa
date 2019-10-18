
def f_selectsort(lista, arg1, arg2 ):

	f_comparacao = arg1
	v_coluna = arg2

	menor 	= None
	aux 	= None
	tam		= len(lista)

	for i in range (0,tam):
		menor = i
		for j in range(i+1,tam):
			if (f_comparacao(lista[j][v_coluna], lista[menor][v_coluna]) == -1): 
				menor = j
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux
	return lista

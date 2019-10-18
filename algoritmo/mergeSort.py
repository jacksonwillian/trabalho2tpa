# DECLARACAO DAS VARIAVEIS GLOBAIS
f_comparacao = None
v_coluna = None


def f_mergesort(lst, arg1 , arg2):

	# INICIALIZACAO DO CONTEUDO DAS VARIAVEIS GLOBAIS
	global f_comparacao
	global v_coluna
	f_comparacao = arg1
	v_coluna = arg2

	if(len(lst) > 1):
		
		meio = len(lst)//2

		lado_esq = lst[:meio]
		lado_dirt = lst[meio:]

		lado_esq = f_mergesort(lado_esq, arg1, arg2)
		lado_dirt = f_mergesort(lado_dirt, arg1, arg2)    

		return merge(lado_esq, lado_dirt)

	return lst


def merge(lado_esq,lado_dirt):

	index_dir = 0
	index_esq = 0
	tam_esq = len(lado_esq)
	tam_dir = len(lado_dirt)
	new_lst = []
	
	while index_esq < tam_esq and index_dir < tam_dir:
			
		if (f_comparacao(lado_esq[index_esq][v_coluna], lado_dirt[index_dir][v_coluna]) ==  1):
			
			new_lst.append(lado_esq[index_esq])
			index_esq+=1    
		
		else:

			new_lst.append(lado_dirt[index_dir])
			index_dir+=1
		
	new_lst += lado_dirt[index_dir:]
	new_lst += lado_esq[index_esq:]
	
	return new_lst



# FUNCAO DE CARREGAR O ARQUIVO NA MEMORIA COMO LISTA DE LISTA
# ESTRUTURA DA LISTA: LISTA NO INDICE 0 == [lista com os campos do cabeçalho do arquivo csv]
# 					  LISTA NO INDICE 1 == [lista de lista, cada elemento da lista é a linha do arquivo, 
#                                            e cada elemento da sublista são as colunas da linha do arquivos]
def f_read_csv(nome_Arquivo):
	arq_carregado = []
	try:
		arq  = open( nome_Arquivo , "r" )
	except IOError as e:
		print ("ERRO | I/O {} ".format(e))
	else:
		linha_cabecalho = arq.readline()
		arq_carregado.append(linha_cabecalho.strip().split(",") )
		lst_linhas = []
		linha = arq.readline()
		while linha != "":
			lst_linhas.append( linha.strip().split(",") )
			linha = arq.readline()
		arq.close()	
		arq_carregado.append(lst_linhas )
	return arq_carregado

# FUNCAO PARA SALVAR O ARQUIVO COMO LISTA NO ARQUIVO
def f_write_csv(arq_carregado, nome_arquivo):
	try:
		arq = open(nome_arquivo, "w")
	except IOError as e:
		print ("ERRO | I/O {} ".format(e))
	else:
		linha = ""
		for coluna in arq_carregado[0]:
			linha += coluna + ","
		arq.write(linha + "\n")
		for colunas in  arq_carregado[1]:
			linha = ""
			for coluna in colunas:
				linha += coluna + ","
			arq.write(linha + "\n")
		arq.close()
	return None
# IMPORTACAO DOS ALGORITMOS DE ORDENACAO
from algoritmo import insertsort
from algoritmo import heapsort
from algoritmo import quicksort 
from algoritmo import selectsort
from algoritmo import mergesort
from algoritmo import introsort
from algoritmo import timsort
# IMPORTACAO DOS ALGORITMIS DE COMPARACAO
from algoritmo import comparacao
# BIBLIOTECAS 
import time as time_
from datetime import datetime
import os.path
# DICIONARIO COM OS NOMES DAS FUNCOES EXISTENTES E O APONTAMENTO PARA AS MESMAS
id_f_ordenacao = {'insertsort':[insertsort.f_insertsort],'heapsort':[heapsort.f_heapsort],'quicksort':[quicksort.f_quicksort],'selectsort':[selectsort.f_selectsort], 'mergesort':[mergesort.f_mergesort], 'introsort':[introsort.f_introsort], 'timsort':[timsort.f_timsort]}
id_f_comparacao = {'compara_texto':[comparacao.f_compara_texto], 'compara_inteiro':[comparacao.f_compara_inteiro], 'compara_data':[comparacao.f_compara_data], 'compara_gen_C':[comparacao.f_comp_gen_C],'compara_gen_D':[comparacao.f_comp_gen_D]}



# FUNCAO DE CARREGAR O ARQUIVO NA MEMORIA COM LISTA
# OBS.: AS COLUNAS ESTÃO TODAS COMO STRINGS
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
		while linha != "":#000000
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

# FUNCAO DE ORDENAR GENERICA PARA CHAMAR UMA FUNCAO PRINCIPAL
def f_ordenar( arq_carregado, id_ordenacao, id_comparacao , posicao_coluna):

	f_ord_generico = id_f_ordenacao[id_ordenacao][0]
	f_cp_generico = id_f_comparacao[id_comparacao][0]
	listaOrdenada = f_ord_generico(arq_carregado[1], f_cp_generico, posicao_coluna)
	arq_carregado[1] = listaOrdenada

def main(args):
	if (len(args) == 4):
		# VERIFICA OS DOIS PRIMEIROS ARGUMENTOS 
		if (args[0] in id_f_ordenacao) and (args[1] in id_f_comparacao):

			# DEFINE POSICAO DA COLUNA DO CSV
			posicao = 2 # coluna Identiﬁcador de Usuario (uid).

			# CARREGA O ARQUIVO CSV
			# print("Carregando arquivo '{}'...".format(args[2]))
			arq_carregado = f_read_csv(args[2])
			tam_lst = len(arq_carregado[1])

			print("Ordenando os dados...  ['Ctrl + C' p/ terminar]")

			# PEGAR TEMPO INICIAL
			tempo_inicial = int (time_.time()*1000)

			try:
				
				f_ordenar( arq_carregado, args[0], args[1], posicao)
				
				mgs_execucao = "\nA execução terminou com SUCESSO!\n"

			except Exception as e:

				mgs_execucao = "\nERRO | A execução foi interrompido devido um o erro: {} \n".format(e)

			except KeyboardInterrupt as e:

				mgs_execucao = "\nA execução foi INTERROMPIDA via Teclado Ctrl + C!\n"

			finally:

				# PEGAR TEMPO FINAL
				tempo_final = int (time_.time()*1000)

				print(mgs_execucao)

				# SALVAR O ARQUIVO CSV
				print("Salvando arquivo '{}'...".format(args[3]))
				f_write_csv(arq_carregado, args[3])

				# print("Gerando relatorio...".format(args[3]))
				# RELATAR TEMPO DE EXECUCAO
				print("\n{} \t {} \t {}\n".format(args[0], tam_lst, (tempo_final - tempo_inicial) ))

				resultado = "{},{},{},{},{},{}".format(args[0], args[2], tam_lst, (tempo_final - tempo_inicial),datetime.now().strftime('%d/%m/%Y %H:%M') ,mgs_execucao.strip()) 
				print("\nGRAVOU RESULTADO: ", salvaResultado(resultado))


		else:
			print("ERRO | id_funcao_ordenacao e/ou id_funcao_comparacao inseridos nao estao corretos.")
			print("TENTE:\n id_funcao_ordenacao como um desses: {};\n id_funcao_comparacao como um desses: {};".format(str(list(id_f_ordenacao.keys())).strip('[]'), str(list(id_f_comparacao.keys())).strip('[]')))
	else:
		print("ERRO | Argumentos esperados: id_funcao_ordenacao id_funcao_comparacao arquivo_entrada arquivo_saida")
		print("TENTE:\n id_funcao_ordenacao como um desses: {};\n id_funcao_comparacao como um desses: {};".format(str(list(id_f_ordenacao.keys())).strip('[]'), str(list(id_f_comparacao.keys())).strip('[]')))
	return 0



def salvaResultado(linha):
	
	nome_arquivo = "resultado.csv"

	if not os.path.exists('resultado.csv'):
		linha = "id, nome arquivo, tamanho, tempo, hora e data, feedback\n" + linha

	try:
		arq = open(nome_arquivo, "a")
		
		arq.write(linha + "\n")
		arq.close()
		return True
	except IOError as e:
		print ("ERRO | I/O {} ".format(e))
	else:
		return False

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv[1:]))




#v -> vetor
#i -> indice inicio
#f -> indice fim
#q -> indice aux para o particionamento,
#q+1 define o indice em que o pivô está 

# DECLARACAO DAS VARIAVEIS GLOBAIS
f_comparacao = None
v_coluna = None

def particiona(v,i,f):
  pivo = v[f]
  q = i-1
  for j in range(i , f):
    if (f_comparacao( v[j][v_coluna], pivo[v_coluna]) <= 0):
      q += 1 
      v[q],v[j] = v[j],v[q]
  v[q+1],v[f] = v[f],v[q+1]
  return q+1

def quicksort(v,i,f):
  if (i < f):
    r = particiona(v, i, f )
    quicksort(v, i, r-1 )
    quicksort(v, r+1, f)

def f_quicksort(a, arg1, arg2):
	# INICIALIZACAO DO CONTEUDO DAS VARIAVEIS GLOBAIS
  global f_comparacao
  global v_coluna
  f_comparacao = arg1
  v_coluna = arg2

  t_vetor = len(a)-1
  quicksort(a, 0, t_vetor)
  return a

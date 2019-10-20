from algoritmo import insertsort
from algoritmo import heapsort
import math as math_

# DECLARACAO DAS VARIAVEIS GLOBAIS
f_comparacao = None
v_coluna = None


def introsort_(a,ini, fin, profundidade_max):

  t_vetor = fin - ini
  if t_vetor < 22:
    a_insertsort(a[ini:fin])
    return
  if profundidade_max == 0:
    a_heapsort(a[ini:fin])
    return
    
  pivo = mediana(a,ini,fin,ini+t_vetor//2)
  a[pivo],a[fin] = a[fin],a[pivo]

  if(fin > ini):
    i_part = particiona(a,ini,fin)
    introsort_(a, ini, i_part-1, profundidade_max -1)
    introsort_(a,i_part+1, fin, profundidade_max -1)

def particiona(v,i,f):
  pivo = v[f]
  q = i-1
  for j in range(i , f):
    if (f_comparacao( v[j][v_coluna], pivo[v_coluna]) <= 0):
      q += 1 
      v[q],v[j] = v[j],v[q]
  v[q+1],v[f] = v[f],v[q+1]
  return q+1


def f_introsort(a, arg1, arg2):
  # INICIALIZACAO DO CONTEUDO DAS VARIAVEIS GLOBAIS
  global f_comparacao
  global v_coluna
  f_comparacao = arg1
  v_coluna = arg2
  n = len(a) - 1

  profundidade_max = math_.floor(math_.log2(len(a)))
  introsort_(a, 0, n, profundidade_max)

  return a

def a_insertsort(a):

  for i in range(1, len(a)):
    chave = a[i]
    j = i-1
    while( j >= 0) and ( f_comparacao( a[j][v_coluna], chave[v_coluna]) == 1):
      a[j+1] = a[j]
      j = j -1
    a[j+1] = chave

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


def a_heapsort(a):
	j = len(a) - 1

	meio = j//2
	while (0 <= meio):
		maxheap(a, meio, j)
		meio -= 1
		
	while (j >= 0):
		a[0], a[j] = a[j], a[0]
		j -= 1
		maxheap(a, 0, j)

def mediana(vetor,a,b,c):
  x = vetor[a]
  y = vetor[b]
  z = vetor[c]

  if f_comparacao(x[v_coluna],y[v_coluna]) >= 0  and f_comparacao(x[v_coluna],z[v_coluna]) >= 0:
    if f_comparacao(y[v_coluna],z[v_coluna]) >= 0:
      return b
    else:
      return c
  
  if f_comparacao(y[v_coluna],x[v_coluna]) >= 0  and f_comparacao(y[v_coluna],z[v_coluna]) >= 0:
    if f_comparacao(x[v_coluna],z[v_coluna]) >= 0:
      return a
    else:
      return c
  
  if f_comparacao(z[v_coluna],x[v_coluna]) >= 0  and f_comparacao(z[v_coluna],y[v_coluna]) >= 0:
    if f_comparacao(x[v_coluna],y[v_coluna]) >= 0:
      return a
    else:
      return b
    



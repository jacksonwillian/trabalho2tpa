def f_insertsort(a, arg1, arg2):

  f_comparacao = arg1
  v_coluna = arg2

  for i in range(1, len(a)):
    chave = a[i]
    j = i-1
    while( j >= 0) and ( f_comparacao( a[j][v_coluna], chave[v_coluna]) == 1):
      a[j+1] = a[j]
      j = j -1
    a[j+1] = chave
  return a

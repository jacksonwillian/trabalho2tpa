def f_insertsort(a, arg1, arg2):
  global f_comparacao
  global v_coluna
  f_comparacao = arg1
  v_coluna = arg2

  for i in range(1,len(a)):
    chave = a[i]
    j = i-1

    while( j >= 0 and not (f_comparacao(chave, a[j], v_coluna))):
    
      a[j+1] = a[j]
    
      j = j -1
  
    a[j+1] = chave
 
  
  return a



# a = [52,45,25,31,28,17,65,35,42,86]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(insertSort(a)))
  
  
# a = [-1,-4, 0, 2]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(insertSort(a)))
  
  
# a = [5,4]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(insertSort(a))) 
  
# a = [1,2,1,2]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(insertSort(a))) 
  
# a = [1]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(insertSort(a)))
  
# a = []
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(insertSort(a)))

# a = ["Ana","Xuliana","Anna","Xuliana","Boca"]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(insertSort(a)))  



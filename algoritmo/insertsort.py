def insertSort(lista):

  for i in range(1,len(lista)):
    chave = lista[i]
    j = i-1

    while( j >= 0 and lista[j] > chave):
    
      lista[j+1] = lista[j]
    
      j = j -1
  
    lista[j+1] = chave
 
  
  return lista




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



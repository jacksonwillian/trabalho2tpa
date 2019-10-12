def selectSort(lista):

	menor 	= None
	aux 	= None
	tam		= len(lista)

	for i in range (0,tam):
		
		menor = i

		for j in range(i+1,tam):
			
			if(lista[j] < lista[menor]):
				menor = j
		
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux
	
	return lista

# a = [52,45,25,31,28,17,65,35,42,86]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(selectSort(a)))
  
  
# a = [-1,-4, 0, 2]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(selectSort(a)))
  
  
# a = [5,4]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(selectSort(a))) 
  
# a = [1,2,1,2]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(selectSort(a))) 
  
# a = [1]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(selectSort(a)))
  
# a = []
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(selectSort(a)))

# a = ["Ana","Xuliana","Anna","Xuliana","Boca"]
# print("\nENTRADA {}".format(a))
# print("\n SAIDA  {}\n".format(selectSort(a)))  

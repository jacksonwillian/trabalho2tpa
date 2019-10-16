def mergeSort(lst):

	if(len(lst) > 1):
		
		meio = len(lst)//2;

		lado_esq 	= lst[:meio]
		lado_dirt 	= lst[meio:]

		lado_esq 	= mergeSort(lado_esq)
		lado_dirt 	= mergeSort(lado_dirt)	

		return merge(lado_esq,lado_dirt)

	return lst


def merge(lado_esq,lado_dirt):

	index_dir 	= 0
	index_esq 	= 0
	tam_esq		= len(lado_esq)
	tam_dir		= len(lado_dirt)
	new_lst 	= []
	
	while index_esq < tam_esq and index_dir < tam_dir:
			
		if(lado_esq[index_esq] < lado_dirt[index_dir]):
			
			new_lst.append(lado_esq[index_esq])
			index_esq+=1	
		
		else:

			new_lst.append(lado_dirt[index_dir])
			index_dir+=1
		
	new_lst += lado_dirt[index_dir:]
	new_lst += lado_esq[index_esq:]
	
	return new_lst

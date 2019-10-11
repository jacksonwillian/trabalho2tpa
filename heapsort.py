
def posicaoMaiorFilho(a, i, j):
	filhoEsquerdo = ((2*i) + 1) if ((2*i) + 1) <= j else -1
	filhoDireito = ((2*i) + 2) if ((2*i) + 2) <= j else -1
	if (filhoEsquerdo != -1 and filhoDireito != -1):
		if (a[filhoEsquerdo] > a[filhoDireito]) and (a[filhoEsquerdo] > a[i] ):
			return filhoEsquerdo
		elif(a[filhoDireito] > a[filhoEsquerdo]) and (a[filhoDireito] > a[i] ):
			return filhoDireito
		else:
			return -1
	else:
		if (filhoEsquerdo != -1 ) and (a[filhoEsquerdo] > a[i] ): 
			return filhoEsquerdo
		elif (filhoDireito != -1 ) and (a[filhoDireito] > a[i] ):
			return filhoDireito
		else:
			return -1

def heap(a, i, j):
	posicaoMaior = posicaoMaiorFilho(a, i, j)
	while (posicaoMaior != -1):
		aux = a[posicaoMaior]
		a[posicaoMaior] = a[i]
		a[i] = aux
		i = posicaoMaior
		posicaoMaior = posicaoMaiorFilho(a, posicaoMaior, j)
	return a

def heapsort(a):
	posicaoInicial = 0
	posicaoFinal = len(a)-1
	while ((posicaoFinal -1 ) >= posicaoInicial):
		posicaoMeio = int(posicaoFinal/2)
		while( posicaoInicial <= posicaoMeio):
			a = heap(a, posicaoMeio, posicaoFinal)
			posicaoMeio -=  1
		aux = a[posicaoFinal]
		a[posicaoFinal] = a[0]
		a[0] = aux
		posicaoFinal -= 1
	return a
	
def main ():
	
	
	a = [52,45,25,31,28,17,65,35,42,86]
	print("\nENTRADA {}".format(a))
	print("\n SAIDA  {}\n".format(heapsort(a)))
	
	
	a = [-1,-4, 0, 2]
	print("\nENTRADA {}".format(a))
	print("\n SAIDA  {}\n".format(heapsort(a)))
	
	
	a = [5,4]
	print("\nENTRADA {}".format(a))
	print("\n SAIDA  {}\n".format(heapsort(a)))	
	
	a = [1,2,1,2]
	print("\nENTRADA {}".format(a))
	print("\n SAIDA  {}\n".format(heapsort(a)))	
	
	a = [1]
	print("\nENTRADA {}".format(a))
	print("\n SAIDA  {}\n".format(heapsort(a)))
	
	a = []
	print("\nENTRADA {}".format(a))
	print("\n SAIDA  {}\n".format(heapsort(a)))	
	
	return 0
	
main()



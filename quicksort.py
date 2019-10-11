#v -> vetor
#i -> indice inicio
#f -> indice fim
#q -> indice aux para o particionamento,
#q+1 define o indice em que o pivô está  

def particiona(v,i,f):
  pivo = v[f]
  q = i-1

  for j in range(i,f):
    if (v[j] <= pivo):
      q += 1 
      v[q],v[j] = v[j],v[q]
  v[q+1],v[f] = v[f],v[q+1]
  print(v)
  return q+1

def quicksort(v,i,f):
  if (i < f):
    r = particiona(v,i,f)
    quicksort(v,i,r-1)
    quicksort(v,r+1,f)


def main(args):
	a = [3,5,6,4,8,9,7,1,5,5,6,4,9,7,1,3,6,4,9]  
	quicksort(a,0,len(a)-1)
	print(a)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

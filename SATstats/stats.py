sats=["aids1SAT.tx","aids1UNSAT.tx","pcms1SAT.tx","pcms1UNSAT.tx","pdbs1SAT.tx","pdbs1UNSAT.tx","ppigo1SAT.tx","ppigo1UNSAT.tx"]


maxNodes=[]
minNodes=[]
totNodes=[]
avgNodes=[]
medNodes=[]

def median(lista):
    lista.sort()
    print lista
    odd = True
    length = len(lista)
    half = len(lista)/2
    if (half + half) == length:
        odd = False # it is even
    if odd:
        return lista[half+1]
    else:
        suma = lista[half-1] + lista[half]
        return suma/2.0

def nodesStats(filas):
    for i in range (0,len(filas)):
        fila = filas[i]
        print fila
        maxi=0
        mini=99999999
        suma=0
        counter=0
        lista=[]
        with open(fila) as fp:
            for line in fp.readlines():
                linelista=line.split(";")
                if len(linelista) > 1:
                    nodeslista = linelista[2].split(" ")
                    number = int(nodeslista[1])
                    suma = suma + number
                    counter = counter + 1
                    lista.append(number)
                    if number > maxi:
                        maxi = number
                    if number < mini:
                        mini = number          
        maxNodes.append(maxi)
        minNodes.append(mini)
        avgNodes.append((suma*1.0)/(counter*1.0))
        totNodes.append(suma)
        medNodes.append(median(lista))

nodesStats(sats)

print maxNodes
print minNodes
print avgNodes
print totNodes
print medNodes





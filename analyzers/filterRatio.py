import sys

aids0lista = ["../statsSIP0/aids/stats0.txt", "../statsSIP0/aids/stats1.txt", "../statsSIP0/aids/stats2.txt","../statsSIP0/aids/stats3.txt","../statsSIP0/aids/stats4.txt","../statsSIP0/aids/stats5.txt"]
aids1lista = ["../statsSIP1/aids/stats0.txt", "../statsSIP1/aids/stats1.txt", "../statsSIP1/aids/stats2.txt","../statsSIP1/aids/stats3.txt","../statsSIP1/aids/stats4.txt","../statsSIP1/aids/stats5.txt"]
pcms1lista = ["../statsSIP1/pcms/stats16_1BLH.cm.A.txt",  "../statsSIP1/pcms/stats32_1ATU.cm.A.txt", "../statsSIP1/pcms/stats32_1D1U.cm.A.txt", "../statsSIP1/pcms/stats16_1C5G.cm.A.txt", "../statsSIP1/pcms/stats32_1CNQ.cm.A.txt", "../statsSIP1/pcms/stats8_1A0G.cm.A.txt", "../statsSIP1/pcms/stats32_1ARO.cm.L.txt", "../statsSIP1/pcms/stats32_1CY1.cm.A.txt", "../statsSIP1/pcms/stats8_1A0G.cm.B.txt"]
pcms0lista = ["../statsSIP0/pcms/stats16_1BLH.cm.A.txt",  "../statsSIP0/pcms/stats32_1ATU.cm.A.txt", "../statsSIP0/pcms/stats32_1D1U.cm.A.txt", "../statsSIP0/pcms/stats16_1C5G.cm.A.txt", "../statsSIP0/pcms/stats32_1CNQ.cm.A.txt", "../statsSIP0/pcms/stats8_1A0G.cm.A.txt", "../statsSIP0/pcms/stats32_1ARO.cm.L.txt", "../statsSIP0/pcms/stats32_1CY1.cm.A.txt", "../statsSIP0/pcms/stats8_1A0G.cm.B.txt"]
pdbs0lista = ["../statsSIP0/pdbs/stats16_103l.0.txt", "../statsSIP0/pdbs/stats32_1AMU.txt", "../statsSIP0/pdbs/stats8_103l.0.txt", "../statsSIP0/pdbs/stats16_9ldb.1.txt", "../statsSIP0/pdbs/stats32_1ARO.txt", "../statsSIP0/pdbs/stats8_9ldb.1.txt"]

pdbs1lista = ["../statsSIP1/pdbs/stats16_103l.0.txt", "../statsSIP1/pdbs/stats32_1AMU.txt", "../statsSIP1/pdbs/stats8_103l.0.txt", "../statsSIP1/pdbs/stats16_9ldb.1.txt", "../statsSIP1/pdbs/stats32_1ARO.txt", "../statsSIP1/pdbs/stats8_9ldb.1.txt"]

ppigo1lista = ["../statsSIP1/ppigo/statst1_4.3.txt", "../statsSIP1/ppigo/statst2_8.4.txt", "../statsSIP1/ppigo/stats8_1.6.txt",  "../statsSIP1/ppigo/statst1_4.9.txt", "../statsSIP1/ppigo/statst1_4.9.txt", "../statsSIP1/ppigo/stats4.6.txt", "../statsSIP1/ppigo/statst1_4.3.txt", "../statsSIP1/ppigo/statst2_8.4.txt"]

ppigo0lista = ["../statsSIP0/ppigo/statst1_4.3.txt", "../statsSIP0/ppigo/statst2_8.4.txt", "../statsSIP0/ppigo/stats8_1.6.txt",  "../statsSIP0/ppigo/statst1_4.9.txt", "../statsSIP0/ppigo/statst1_4.9.txt", "../statsSIP0/ppigo/stats4.6.txt", "../statsSIP0/ppigo/statst1_4.3.txt", "../statsSIP0/ppigo/statst2_8.4.txt"]

answ=[]
fail1=[]
fail2=[]
fail3=[]
fail4=[]
fail5=[]

avgs=[]
meds=[]

mini=[]
maxi=[]

def normalize(lista, dbsize):
    for i in range (0, len(lista)):
        lista[i] = (lista[i]*100)/(dbsize*1.0)

def processFiles(lista, dbsize):
    for fila in lista:
        alles=[]
        with open(fila) as fp:
            for line in fp.readlines():
                number = line.strip('\n')
                alles.append(float(number))
        answ.append(alles[0])
        fail1.append(alles[1])
        fail2.append(alles[2])
        fail3.append(alles[3])
        fail4.append(alles[4])
        fail5.append(alles[5])
    normalize(fail1, dbsize)
    normalize(fail2, dbsize)
    normalize(fail3, dbsize)
    normalize(fail4, dbsize)
    normalize(fail5, dbsize)

def average(lista):
    suma = 0.0
    length = len(lista)
    for number in lista:
        suma = suma + float(number)
    avgs.append(suma/length)


def median(lista):
    lista.sort()
    odd = True
    length = len(lista)
    half = len(lista)/2
    if (half + half) == length:
        odd = False # it is even
    if odd:
        meds.append(lista[half+1])
    else:
        suma = lista[half-1] + lista[half]
        meds.append(suma/2.0)

def minmax(lista):
    lista.sort()
    mini.append(lista[0])
    maxi.append(lista[len(lista)-1])


#processFiles(aids1lista, 40000)
#processFiles(pcms1lista, 50)
#processFiles(pdbs1lista, 30)
#processFiles(ppigo1lista, 20)

#average(fail1)
#average(fail2)
#average(fail3)
#average(fail4)
#average(fail5)

#median(fail1)
#median(fail2)
#median(fail3)
#median(fail4)
#median(fail5)

#minmax(fail1)
#minmax(fail2)
#minmax(fail3)
#minmax(fail4)
#minmax(fail5)

def printLista(lista):
    i = 0
    for numb in lista:
        if (i+1) != len(lista):
           sys.stdout.write(str(numb) + ",")
        else:
            sys.stdout.write(str(numb) + "\n")
        i=i+1


# generate statistics for the number of solvable instances of eahc dataset
aidsansw=[8042,11957,78,461,77,3]
pcmsansw=[38,144,124,136,4,20,4,4,4]
pdbsansw=[500,580,460,136,360,300,580]
ppigoansw=[12,7,13,17,12]

normalize(aidsansw,40000)
normalize(pcmsansw,200)
normalize(pdbsansw,600)
normalize(ppigoansw,50)


median(aidsansw)
median(pcmsansw)
median(pdbsansw)
median(ppigoansw)

average(aidsansw)
average(pcmsansw)
average(pdbsansw)
average(ppigoansw)

minmax(aidsansw)
minmax(pcmsansw)
minmax(pdbsansw)
minmax(ppigoansw)

printLista(avgs)
printLista(meds)
printLista(mini)
printLista(maxi)

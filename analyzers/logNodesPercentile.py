import itertools
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from numpy.random import normal
import copy
from matplotlib.ticker import FormatStrFormatter

alldata=[]

def getData(fila):
    lista=[]
    with open(fila) as fp:
        for flista in fp.readlines():
            flista=flista[:-2].split(",")
            i = 0
            maxi = max(len(lista),len(flista))
            templista=[0]*len(flista)
            if len(lista) > 0:
                templista=lista[:]
                lista=[]
                if len(templista) < maxi:
                    lendiff = maxi-len(templista)
                    templista.extend([0]*lendiff)
                elif len(flista) < maxi:
                    lendiff = maxi - len(flista)
                    flista.extend([0]*lendiff)
            while i < maxi:
                #print templista[i]
                lista.append(int(templista[i]) + int(flista[i]))
                i=i+1
                #print maxi,i
    for i in range(0,len(lista)):
        lista[i] = lista[i]
    return lista

def makeIndices(limit):
    lista=[]
    for i in range(0,limit):
        lista.append(i)
    return lista



#alla = getData("../ppigo1nodes.txt")
alla=getData("../aidsSATnodes.txt")
print len(alla)
sumAlla = sum(alla)
percentile = sumAlla/100
#print(sumAlla % 100)
print percentile

percentiles = [0]*100
lowPercentiles = [0]*100
currentPercentile = percentile
percentileCounter = 0
lowPercentileCounter = 0
index = 0
first = True
while index < len(alla):
    deduction = min(alla[index], currentPercentile)
    if first and deduction != 0:# and not last:
        lowPercentiles[lowPercentileCounter] = index
        lowPercentileCounter += 1
        first = False
    currentPercentile -= deduction
    alla[index] -= deduction
    if currentPercentile == 0:
        percentiles[percentileCounter] = index
        currentPercentile = percentile
        percentileCounter += 1
        if percentileCounter != 99:
            first = True
        else:
            break
    if alla[index] == 0:
        index += 1

percentiles[99] = len(alla) - 1
#print(percentiles)
#print(lowPercentiles)

xvals = np.arange(0, 101, 10)
yvals = np.arange(0,percentiles[-1],10)

#log_percentiles=np.log(percentiles)
#print(log_percentiles)
plt.yscale('log')

for i, perc in enumerate(percentiles):
    plt.bar(i, perc, bottom=0, log=True, color='b')

plt.xlabel('percentile of population')
plt.ylabel('difficulty measured in search nodes')
plt.xticks(xvals)

plt.xlim(0, 100)
#plt.yscale('log')
plt.grid(True, which='major', color='b')
plt.grid(True, which='minor', color='r')
#ax = plt.gca()
#ax.set_yscale('log')
plt.tick_params(axis='y', which='minor')

#ax.yaxis.set_minor_formatter(FormatStrFormatter("%.1f"))


plt.show()

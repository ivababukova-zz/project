import itertools
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from numpy.random import normal
import copy


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



alla = getData("../aids1nodes.txt")
sumAlla = sum(alla)
percentile = sumAlla/100
print(sumAlla % 100)
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
    if alla[index] == 0:
        index += 1

percentiles[99] = len(alla) - 1
print(percentiles)
print(lowPercentiles)

xvals = np.arange(0, 101, 10)
yvals = np.arange(0,percentiles[-1],10)

#fig = plt.figure()
#ax = fig.add_subplot(2,1,1)


f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
ax.set_ylim(609, 750)  # outliers only
print(dir(ax))
f.subplots_adjust(top=0.9)
ax.set_position([0.1, 0.85, 0.8, 0.9])

#ax.margins(0.3, 0.3)
ax2.set_position([0.1, 0.1, 0.8, 0.72])


ax2.set_ylim(0, 140)  # most of the data

for i, perc in enumerate(percentiles):
    ax.bar(i, perc,  color = 'blue')
    ax2.bar(i, perc,  color = 'blue')

plt.xlabel('percentile of population')
plt.ylabel('difficulty measured in search nodes')
plt.xticks(xvals)
#for i, perc in enumerate(percentiles):
#    plt.bar(i, perc,  color = 'blue')

#plt.plot(numbers1x, numbers1y, marker = 'x', color = 'b')

plt.xlim(0, 100)
#ax.set_yscale('log')
ax.yaxis.grid(True)
ax.xaxis.grid(True)
ax2.yaxis.grid(True)
ax2.xaxis.grid(True)
#r1y=np.arange(1, maxi+1, 1)

#print zip(alla, r1y)

plt.show()


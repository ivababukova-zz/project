import sys

aids0statslista = ["nodesStatsSIP0/aids/stats0.txt", "nodesStatsSIP0/aids/stats1.txt", "nodesStatsSIP0/aids/stats2.txt","nodesStatsSIP0/aids/stats3.txt","nodesStatsSIP0/aids/stats4.txt","nodesStatsSIP0/aids/stats5.txt"]
aids1statslista = ["nodesStatsSIP1/aids/stats0.txt", "nodesStatsSIP1/aids/stats1.txt", "nodesStatsSIP1/aids/stats2.txt","nodesStatsSIP1/aids/stats3.txt","nodesStatsSIP1/aids/stats4.txt","nodesStatsSIP1/aids/stats5.txt"]

pcms1statslista = ["nodesStatsSIP1/pcms/stats16_1BLH.cm.A.txt", "nodesStatsSIP1/pcms/stats32_1ATU.cm.A.txt", "nodesStatsSIP1/pcms/stats32_1D1U.cm.A.txt", "nodesStatsSIP1/pcms/stats16_1C5G.cm.A.txt", "nodesStatsSIP1/pcms/stats32_1CNQ.cm.A.txt", "nodesStatsSIP1/pcms/stats8_1A0G.cm.A.txt", "nodesStatsSIP1/pcms/stats32_1ARO.cm.L.txt", "nodesStatsSIP1/pcms/stats32_1CY1.cm.A.txt", "nodesStatsSIP1/pcms/stats8_1A0G.cm.B.txt"]
pcms0statslista = ["nodesStatsSIP0/pcms/stats16_1BLH.cm.A.txt", "nodesStatsSIP0/pcms/stats32_1ATU.cm.A.txt", "nodesStatsSIP0/pcms/stats32_1D1U.cm.A.txt", "nodesStatsSIP0/pcms/stats16_1C5G.cm.A.txt", "nodesStatsSIP0/pcms/stats32_1CNQ.cm.A.txt", "nodesStatsSIP0/pcms/stats8_1A0G.cm.A.txt", "nodesStatsSIP0/pcms/stats32_1ARO.cm.L.txt", "nodesStatsSIP0/pcms/stats32_1CY1.cm.A.txt", "nodesStatsSIP0/pcms/stats8_1A0G.cm.B.txt"]

pdbs0statslista = ["nodesStatsSIP0/pdbs/stats16_103l.0.txt", "nodesStatsSIP0/pdbs/stats32_1AMU.txt", "nodesStatsSIP0/pdbs/stats8_103l.0.txt", "nodesStatsSIP0/pdbs/stats16_9ldb.1.txt", "nodesStatsSIP0/pdbs/stats32_1ARO.txt", "nodesStatsSIP0/pdbs/stats8_9ldb.1.txt"]
pdbs1statslista = ["nodesStatsSIP1/pdbs/stats16_103l.0.txt", "nodesStatsSIP1/pdbs/stats32_1AMU.txt", "nodesStatsSIP1/pdbs/stats8_103l.0.txt", "nodesStatsSIP1/pdbs/stats16_9ldb.1.txt", "nodesStatsSIP1/pdbs/stats32_1ARO.txt", "nodesStatsSIP1/pdbs/stats8_9ldb.1.txt"]

ppigo1statslista = ["nodesStatsSIP1/ppigo/statst1_4.3.txt", "nodesStatsSIP1/ppigo/statst2_8.4.txt", "nodesStatsSIP1/ppigo/stats8_1.6.txt", "nodesStatsSIP1/ppigo/statst1_4.9.txt", "nodesStatsSIP1/ppigo/statst1_4.9.txt", "nodesStatsSIP1/ppigo/stats4.6.txt", "nodesStatsSIP1/ppigo/statst1_4.3.txt", "nodesStatsSIP1/ppigo/statst2_8.4.txt"]
ppigo0statslista = ["nodesStatsSIP0/ppigo/statst1_4.3.txt", "nodesStatsSIP0/ppigo/statst2_8.4.txt", "nodesStatsSIP0/ppigo/stats8_1.6.txt",  "nodesStatsSIP0/ppigo/statst1_4.9.txt", "nodesStatsSIP0/ppigo/statst1_4.9.txt", "nodesStatsSIP0/ppigo/stats4.6.txt", "nodesStatsSIP0/ppigo/statst1_4.3.txt", "nodesStatsSIP0/ppigo/statst2_8.4.txt"]

alles=[]
allessuma=[]

# calculate the sum of the graphs that 
def getSuma(fila):
    suma=0
    with open(fila) as fp:
        for line in fp.readlines():
            number = line.strip('\n')
            suma = suma + int(number)
    return suma

# get a list of all nodes and their number of graphs from the file
def parseStats(fila):
    maxi=0
    smallalles=[]
    with open(fila) as fp:
        for line in fp.readlines():
                maxi=maxi+1
                number = line.strip('\n')
                smallalles.append(int(number))
                sys.stdout.write(number + ",")
    sys.stdout.write('\n')
    return smallalles

def generatePlotableStats(aids0statslista):
    for fila in aids0statslista:    
        #alles.append(parseStats(fila))
        allessuma.append(getSuma(fila))

generatePlotableStats(aids0statslista)

print allessuma






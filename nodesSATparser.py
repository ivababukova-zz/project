aidsSAT=["SATstats/aids1SAT.tx","SATstats/aids1UNSAT.tx","SATstats/aids1SATstats.tx","SATstats/aids1UNSATstats.tx"]
pcmsSAT=["SATstats/pcms1SAT.tx","SATstats/pcms1UNSAT.tx","SATstats/pcms1SATstats.tx","SATstats/pcms1UNSATstats.tx"]
pdbsSAT=["SATstats/pdbs1SAT.tx","SATstats/pdbs1UNSAT.tx","SATstats/pdbs1SATstats.tx","SATstats/pdbs1UNSATstats.tx"]
ppigoSAT=["SATstats/ppigo1SAT.tx","SATstats/ppigo1UNSAT.tx","SATstats/ppigo1SATstats.tx","SATstats/ppigo1UNSATstats.tx"]


nodeslista=[]

def maxNodes(fila):
    maxi=0
    with open(fila) as fp:
        for line in fp.readlines():
            linelista=line.split(";")
            if len(linelista) > 1:
                nodeslista = linelista[2].split(" ")
                number = int(nodeslista[1])
                if number > maxi:
                    maxi = number              
    return maxi

def parseSATstats(fila,isSAT):
    if isSAT == 1:
        infila=fila[0]
        outfila=fila[2]
    if isSAT == 0:
        infila=fila[1]
        outfila=fila[3]
    maxi=maxNodes(infila)
    #print maxi
    for i in range(1,maxi+1):
            if i == 1:
                #print "echo " + str(maxi) + " > " + outfila
                print "grep \" " + str(i) + " nodes;\" " + infila + " |wc -l > " + outfila
            else:
                print "grep \" " + str(i) + " nodes;\" " + infila + " |wc -l >> " + outfila

parseSATstats(aidsSAT,1)
parseSATstats(aidsSAT,0)

parseSATstats(pcmsSAT,1)
parseSATstats(pcmsSAT,0)

parseSATstats(pdbsSAT,1)
parseSATstats(pdbsSAT,0)

parseSATstats(ppigoSAT,1)
parseSATstats(ppigoSAT,0)






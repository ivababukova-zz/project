#Subgraph Isomorphism Solver

This is part of my 4th year project, supervised by Patrick Prosser(http://www.dcs.gla.ac.uk/~pat/), involving
investigations of subgraph isomorphism(SIP) processing algorithms.

Given two files with graphs: one with pattern graphs and one with target graphs, this code solves the subgraph
isomorphism problem for every pattern,target pair. It outputs some statistics about the time taken to find a
solution, number of recursive calls, etc. More about the implementation can be read in my dissertation which
can be found on https://github.com/ivababukova/subgraphProcessingDissertation.

The purpose of this code is not only to solve the SIP problem for a given instance, but also to look at the
reasons why a given instance was proved to be satisfiable or unsatisfiable. There are 5 different failures
measured. More detailed explanation about the failures and their motivation can be found in my dissertation in
Chapter 4. The filtering performance of the measured failures for 4 real datasets can be found in my dissertation
in Chapter 5.

##What does this repository contain?
This repository contains all the code needed to run the subgraph isomorphism solver along with the results of
my experiments with 4 datasets found in http://ferrolab.dmi.unict.it/GRAPES/grapes.html#formats . It also
contains scripts that generate bash sripts to run the code and small python programs to analyse and plot the
data using matplotlib(http://matplotlib.org/ ).

This repository contains two SIP solvers: SIP0 and SIP1. SIP0 is created by Patrick Prosser and SIP1 is an
extension of SIP1 with additional filtering method based on Neighbourhood Degree Sequence (NDS) of each graph.
The notion of NDS and the solvers are explained in my dissertation, Chapter 4.

The results of SIP between targets and patterns in the datasets can be found in resultsSIP1 folder after executed
with SIP1 solver and in resultsSIP0 folder after executed with SIP0 solver.

##Running the code
- To run the code, download the project/out/artifacts/Iva_Index3_jar jar in the repository, go to the directory
where the jar is saved and type the following command:

    java -cp Iva-Index3.jar Main <patterns filename> <targets filename>

This runs SIP1, as this is the default solver. To run SIP0, add <-SIP0> argument after the name of the targets
filename.

- To run the code along with information about which instance failed, add <-e> after the name of the targets 
filename.

##Running the statistics generators
- nodesStatsGenerator.py takes the results from the SIP solver and generates a bash script. When ran on a
terminal and given a directory SATstats that is placed in the same directory as nodesStatsGenerator.py, the
script creates a new .txt file containing the number of times each of the trivial failures proved that an instance
is unsatisfiable. The first line of the .txt file is for failure 1, second line for failure 2, etc.

- to run nodesStatsGenerator, open a terminal and go to the same directory where nodesStatsGenerator.py and the
results folders are stored. Type in the following commands:

    python nodesStatsGenerator.py > script.sh
    ./script.sh

- nodesSATparser.py takes the files created by nodesStatsGenerator.py in directory SATstats and (TODO)





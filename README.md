#Subgraph Isomorphism Solver

This is part of my 4th year project involving investigations of subgraph isomorphism processing algorithms.

Given two files with graphs: one with pattern graphs and one with target graphs, this code solves the subgraph
isomorphism problem for every pattern,target pair. It outputs some statistics about the time taken to find a
solution, number of recursive calls, etc. More about the implementation can be read in my dissertation which
can be found on https://github.com/ivababukova/subgraphProcessingDissertation

##What does this repository contain?
This repository contains all the code needed to run the subgraph isomorphism solver along with the results of
my experiments with 4 datasets found in http://ferrolab.dmi.unict.it/GRAPES/grapes.html#formats . It also
contains scripts that generate bash sripts to run the code and small python programs to analyse and plot the
data using matplotlib(http://matplotlib.org/ ).

##Running the code
-To run the code, download the project/out/artifacts/Iva_Index3_jar jar in the repository, go to the directory
where the jar is saved and type the following command:

    java -cp Iva-Index3.jar Main <patterns filename> <targets filename>


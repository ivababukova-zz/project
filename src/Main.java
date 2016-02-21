//
// java ExperimentTest ../sample/Q8 ../sample/dataset
//
// Therefore Q8 is the pattern/query and and dataset is the target (hit it!)
// Code below uses algorithm SIP0experimental
//

import java.util.*;
import java.io.*;

import graph.Graph;
import sip.*;

public class Main {

    public static void main(String[] args)  throws IOException {
        long totalCpuTime = System.currentTimeMillis();
        if (args[0].equals("-h")){
            System.out.println("-F FILE file of pairs of filenames of pattern and target graphs \n"+
                    "-a ALG   Name of algorithm, such as SIP0experimental, SIP1, ... \n"+
                    "-s INT  Set CPU time limit in seconds (default infinity) \n"+
                    "-f      Stop at first solution (default: search for all solutions) \n" +
                    "-i      Search for an induced subgraph (default: partial subgraph) \n" +
                    "-v      Print solutions (default: only number of solutions) \n" +
                    "-h     Print this help message");
            return;
        }
        boolean verbose = false, firstSolution = false, induced = false, trace = false, isExperimental = false;
        boolean isSIP0 = false;
        long timeLimit = -1;
        String filename = "", alg = "";
        for (int i=0;i<args.length;i++){
            if (args[i].equals("-v")) verbose = true;
            if (args[i].equals("-f")) firstSolution = true;
            if (args[i].equals("-i")) induced = true;
            if (args[i].equals("-s")) timeLimit = 1000 * (long)Integer.parseInt(args[i+1]);
            if (args[i].equals("-a")) alg = args[i+1];
            if (args[i].equals("-F")) filename = args[i+1];
            if (args[i].equals(("-e"))) isExperimental = true;
            if (args[i].equals(("-SIP0"))) isSIP0 = true;
        }

        ArrayList<Graph> patterns = new ArrayList<Graph>();
        Scanner patternScanner = new Scanner(new File(args[0]));
        //System.out.println("patterns:");
        while (patternScanner.hasNext()) {
            Graph g = new Graph(patternScanner);
            patterns.add(g);
            //g.displayDegreeSequence();
        }
        //System.out.println("targets:");
        patternScanner.close();
        ArrayList<Graph> targets = new ArrayList<Graph>();
        Scanner targetScanner = new Scanner(new File(args[1]));
        while (targetScanner.hasNext()) {
            Graph g = new Graph(targetScanner);
            targets.add(g);
            //g.displayDegreeSequence();
        }
        targetScanner.close();


        // TODO:
        // call indexing the graph from here

        // call SIP from here
        for (Graph P : patterns){
            int solutions = 0;
            int solved = 0;
            for (Graph T : targets){
                long cpuTime      = System.currentTimeMillis();
                if (isSIP0) {
                    SIP0 sip = new SIP0(P, T);
                    sip.setFirstSolution(true); //firstSolution;
                    sip.setInduced(induced);
                    sip.setVerbose(verbose);
                    sip.setTimeLimit(timeLimit);
                    sip.setIsExperimental(isExperimental);
                    sip.solve();
                    solutions = solutions + sip.getSolutions();
                    cpuTime   = System.currentTimeMillis() - cpuTime;
                    System.out.print("Pattern "+ P.getId() +" Target "+ T.getId() +" ");
                    if (!sip.isTimeout()) solved++;
                    if (sip.isTimeout()) System.out.print("CPU time exceeded: ");
                    else System.out.print("Run completed: ");
                    System.out.print(sip.getSolutions() + " solutions; " + sip.getFails() + " fail nodes; ");
                    System.out.println(sip.getNodes() +" nodes; "+ cpuTime +" milliseconds"); // +" "+ sip.simple);
                }
                else {
                    SIP1 sip = new SIP1(P, T);
                    sip.setFirstSolution(true); //firstSolution;
                    sip.setInduced(induced);
                    sip.setVerbose(verbose);
                    sip.setTimeLimit(timeLimit);
                    sip.setIsExperimental(isExperimental);
                    sip.solve();
                    solutions = solutions + sip.getSolutions();
                    cpuTime = System.currentTimeMillis() - cpuTime;
                    System.out.print("Pattern " + P.getId() + " Target " + T.getId() + " ");
                    if (!sip.isTimeout()) solved++;
                    if (sip.isTimeout()) System.out.print("CPU time exceeded: ");
                    else System.out.print("Run completed: ");
                    System.out.println(sip.getSolutions() + " solutions; " + sip.getFails() + " fail nodes; " +
                            sip.getNodes() + " nodes; " + cpuTime + " milliseconds"); // +" "+ sip.simple);
                }
            }
        }

        totalCpuTime = System.currentTimeMillis() - totalCpuTime;
        System.out.println("total cpu time: "+ totalCpuTime +" milliseconds");
    }
}
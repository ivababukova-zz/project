package sip;

import java.util.*;
import java.io.*;
import graph.*;

/**
 * This is SIP0 + check of the neighborhood degree sequence before search
 *
 * */

public class SIP1{

    private long nodes;              // number of decisions
    private long timeLimit;          // milliseconds
    private long cpuTime;            // milliseconds
    public long filterTime;
    public long verifyTime;
    private long initTime;           // the time when we started the verification stage
    private int[] solution;          // as it says
    private boolean matched;         // is there a matching?
    private boolean trace;           // trace, anyone for trace?
    private boolean timeout;         // true if timed out
    private boolean firstSolution;   // only wanting 1st solution?
    private boolean verbose;         // want solution displayed?
    private boolean induced;         // induced or (default) partial?
    private int solutions;           // number of solutions found
    private int fails;               // something like a failed node
    private Graph P;                 // the pattern graph
    private Graph T;                 // the target graph

    private boolean isExperimental;

    public SIP1 (String fnameP, String fnameT) throws IOException {
        P = new Graph(fnameP);
        T = new Graph(fnameT);
        nodes = cpuTime = solutions = fails = 0;
        matched = trace = timeout = firstSolution = verbose = induced = false;
        solution = new int[P.getOrder()];
    }

    public SIP1 (Graph P,Graph T) {
        this.P = P;
        this.T = T;
        nodes = cpuTime = solutions = fails = 0;
        matched = trace = timeout = firstSolution = verbose = induced = false;
        solution = new int[P.getOrder()];
    }

    /** fail-first heuristic, i.e. smallest domain first */
    public Variable select(Variable[] U){
        int smallest = 0;
        for (int i=1;i<U.length;i++){
            if (U[i].domain.cardinality() < U[smallest].domain.cardinality()){
                smallest = i;
            }
        }
        return U[smallest];
    }

    public void solve(){
        long initTime = System.currentTimeMillis();
        if (P.getOrder() > T.getOrder()) {
            if (isExperimental) {
                System.out.println("fail 1: P" + P.getId() + " T" + T.getId());
            }
            this.filterTime = System.currentTimeMillis() - initTime;
            return; // trivial fail
        }
        if (P.numbUniqueLabels() > T.numbUniqueLabels()) {
            if (isExperimental) {
                System.out.println("fail 2: P" + P.getId() + " T" + T.getId());
            }
            this.filterTime = System.currentTimeMillis() - initTime;
            this.verifyTime = 0;
            return; // trivial fail
        }
        // check neighborhood degree sequence:
        for (int i = 0; i < P.numbUniqueLabels(); i++) {
            Label pl = P.getLabel(i);
            Label tl = T.getLabelStr(pl.getLabel()); // O()
            if (tl == null) {
                if (isExperimental) {
                    System.out.println("fail 3: P" + P.getId() + " T" + T.getId());
                }
                this.filterTime = System.currentTimeMillis() - initTime;
                this.verifyTime = 0;
                return; // trivial fail
            }
            if (!isCompatible(pl.getDS(), tl.getDS())) {
                if (isExperimental) {
                    System.out.println("fail 4: P" + P.getId() + " T" + T.getId());
                }
                this.filterTime = System.currentTimeMillis() - initTime;
                this.verifyTime = 0;
                return; // trivial fail
            }
        }

        cpuTime  = System.currentTimeMillis();
        Variable[] U = new Variable[P.getOrder()];
        for (int i = 0; i < P.getOrder(); i++){
            BitSet domain = new BitSet(T.getOrder()); // the domain of U is of size the numb of vertices in T
            for (int j = 0; j < T.getOrder(); j++) {
                // if the conditions are true, jth entry of domain is set to true. Otherwise it is false
                domain.set(j, P.getvLabel(i).equals(T.getvLabel(j)) && P.getDegree(i) <= T.getDegree(j));
            }
            if (domain.cardinality() == 0){
                if (isExperimental) {
                    System.out.println("fail 5: P" + P.getId() + " T" + T.getId());
                }
                this.filterTime = System.currentTimeMillis() - initTime;
                this.verifyTime = 0;
                return; // trivial fail, no bits were set to true, no values in the domain
            }
            U[i] = new Variable(i,domain);
        }
        this.filterTime =  System.currentTimeMillis() - initTime;
        this.initTime = System.currentTimeMillis();
        try{expand(U);} catch(TimeOutException e){timeout = true;}
    }

    public boolean expand(Variable[] U){
        if (timeLimit > 0 && System.currentTimeMillis() - cpuTime >= timeLimit) throw new TimeOutException();
        int n = U.length;
        if (n == 0){
            solutions++;
            if (verbose) display();
            this.verifyTime = System.currentTimeMillis() - this.initTime;
            return firstSolution;
        }
        nodes++;
        Variable[] newU = new Variable[n-1];
        Variable u = select(U); // select the smallest domain
        boolean consistent = false;
        for (int i = u.domain.nextSetBit(0); i>=0 && !consistent; i = u.domain.nextSetBit(i+1)){
            consistent = true;
            solution[u.index] = i;
            for (int j = 0, k = 0; j < n && consistent; j++){
                Variable v = U[j];
                if (u.index != v.index){ // if the chosen u is not picked again and assigned to v
                    Variable newV = new Variable(v.index,(BitSet)v.domain.clone());
                    newV.domain.set(i,false); // cannot take value assigned to u
                    if (P.getNeighbours(u.index).get(v.index)) // adjacent(u,v) in P
                        newV.domain.and(T.getNeighbours(i)); // v can only take vertices in T adjacent to i
                    newU[k++] = newV;
                    consistent = newV.domain.cardinality() > 0;
                }
                if (!consistent) fails++;
            }
            consistent = consistent && expand(newU);
        }
        this.verifyTime = System.currentTimeMillis() - this.initTime;
        return consistent;
    }

    public void display(){
        System.out.print("Solution "+ solutions +":");
        for (int i=0;i<P.getOrder();i++) System.out.print(" "+ i +"="+ solution[i]);
        System.out.println();
    }

    public void shortDisplay(){
        for (int i=0;i<P.getOrder();i++) System.out.print(solution[i]);
        System.out.println();
    }

    /** does target sequence contain pattern sequence? */
    private boolean isCompatible(int[] patternSeq, int[] targetSeq) {
        if (targetSeq.length < patternSeq.length) return false;
        for (int i = 0; i < patternSeq.length; i++) {
            if (patternSeq[i] > targetSeq[i]) return false;
        }
        return true;
    }


    public void setNodes(long nodes) {
        this.nodes = nodes;
    }

    public void setTimeLimit(long timeLimit) {
        this.timeLimit = timeLimit;
    }

    public void setFirstSolution(boolean firstSolution) {
        this.firstSolution = firstSolution;
    }

    public void setVerbose(boolean verbose) {
        this.verbose = verbose;
    }

    public void setInduced(boolean induced) {
        this.induced = induced;
    }

    public void setSolutions(int solutions) {
        this.solutions = solutions;
    }

    public void setP(Graph p) {
        P = p;
    }

    public void setT(Graph t) {
        T = t;
    }

    public long getNodes() {

        return nodes;
    }

    public boolean isTimeout() {
        return timeout;
    }

    public int getSolutions() {
        return solutions;
    }

    public int getFails() {
        return fails;
    }

    public void setIsExperimental(boolean isExperimental) {

        this.isExperimental = isExperimental;
    }
}

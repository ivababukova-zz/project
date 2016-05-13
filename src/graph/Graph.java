package graph;

import java.util.*;
import java.io.*;

public class Graph {


    private int      order;     // numb of vertices
    private int      size;      // numb of edges
    private String   id;        // graph id
    private int[]    degree;    // degree of vertices, degree[u] = the degree of vertex u
    private BitSet[] neighbors; // neighbors[v] is neighbors of v
    private String[] vlabels;   // the labels of the vertices
    private Label[]  labels;    // all unique labels that occur in the graph


    public Graph (String fname) throws IOException {this(new Scanner(new File(fname)));}

    /* reads the input from @sc and constructs the graph */
    public Graph (Scanner sc) throws IOException {
        /* every label and the ids of vertices that have it
        *  avoids reiterating over the vlabels array multiple times when constructing NDS
        * */
        HashMap<String,ArrayList<Integer>> labelsMap = new HashMap<>();
        id          = sc.next();
        order       = sc.nextInt();
        degree      = new int[order];
        neighbors   = new BitSet[order]; // initialize to size of order in case the graph is a clique
        vlabels     = new String[order];

        // initialize bitsets
        for (int i=0; i<order; i++) {
            neighbors[i] = new BitSet(order);
        }
        // construct vertices:
        for (int i=0; i<order; i++) {
            String newL = sc.next(); // get string of label
            vlabels[i] = newL;
            if (labelsMap.get(newL) == null) { // haven't had a label with such string before
                ArrayList<Integer> vertexid  = new ArrayList<>();
                vertexid.add(i);
                labelsMap.put(newL,vertexid);
            }
            else{
                labelsMap.get(newL).add(i);
            }
        }
        // construct edges:
        size = sc.nextInt();
        for (int i=0;i< size;i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            // if changing code for direct graphs, modify to set the bit of only one of them
            neighbors[u].set(v,true); // set the v-th bit in the neighbor bitset of u to true
            neighbors[v].set(u, true); // set the u-th bit in the neighbor bitset of v to true
            degree[u] = degree[u] + 1;
            degree[v] = degree[v] + 1;
        }
        // construct neighbourhood degree sequence of the graph
        setNDS(labelsMap);
    }

    /**
     * Sets the degree sequence for each unique label that occurs in the graph
     * @param labels is generated during the graph construction
     * */
    private void setNDS(HashMap<String, ArrayList<Integer>> labels){
        int numbOfLabels = labels.size();
        String label;
        Iterator labelsIterator = labels.keySet().iterator();
        ArrayList<Integer> vertexids; // the ids of vertices that are labeled with the corresponding label
        this.labels = new Label[numbOfLabels];
        for (int i=0; i<numbOfLabels; i++){
            label           = labelsIterator.next().toString();
            vertexids       = labels.get(label);
            this.labels[i]  = new Label(label,vertexids.size());
            for (int j=0; j<vertexids.size(); j++) {
                this.labels[i].insertDegree(this.degree[vertexids.get(j)]);
            }
        }
        displayDegreeSequence();
    }

    public void display(){
        System.out.println("graph id:" + id);
        System.out.println("graph order:" + order);
        for (int i=0;i< order;i++) System.out.println(vlabels[i]);
        System.out.println(size);
        for (int i=0;i< order -1;i++)
            for (int j=i+1;j< order;j++)
                if (neighbors[i].get(j)) System.out.println(i +" "+ j);
    }

    /* prints the degree sequence of each label in the graph */
    public void displayDegreeSequence(){
        System.out.println(this.getId());
        for (int i = 0; i < this.labels.length; i++) {
            System.out.print(this.labels[i].getLabel() + " <");
            int[] degrees = labels[i].getDS();
            for (int j = 0; j < degrees.length; j++) {
                if (j != degrees.length - 1) {
                    System.out.print(degrees[j] + ", ");
                }
                else {
                    System.out.println(degrees[j] + ">");
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Graph G = new Graph(args[0]);
        G.display();
        G.displayDegreeSequence();
    }

    public int getOrder() {
        return order;
    }

    public BitSet getNeighbours(int i) {
        return neighbors[i];
    }

    public int getSize() {
        return size;
    }

    // get the label of vertex i
    public String getvLabel(int i) {
        return vlabels[i];
    }

    public int numbUniqueLabels(){
        return this.labels.length;
    }

    // get the ith label in labels
    public Label getLabel(int i) {
        return this.labels[i];
    }

    // get the label that has String label=l
    // O(numb of unique labels)
    public Label getLabelStr(String l) {
        for (int i = 0; i < labels.length; i++) {
            if (labels[i].getLabel().equals(l)) return labels[i];
        }
        return null;
    }

    public int getDegree(int i) {
        return degree[i];
    }

    public String getId(){
        return this.id;
    }
}
package graph;

import java.util.*;
import java.io.*;

public class Graph {

    private int order;              // numb of vertices
    private int size;               // numb of edges
    private String id;              // graph id
    private int[] degree;           // degree of vertices
    private BitSet[] neighbors;     // neighbors[v] is neighbors of v
    private String[] vlabels;      // labeled vertices

    private Label[] labels;      // all unique labels that occur in the graph

    public Graph (String fname) throws IOException {this(new Scanner(new File(fname)));}

    public Graph (Scanner sc) throws IOException {
        HashMap<String,ArrayList<Integer>> labels = new HashMap<>(); // every label and the ids of vertices that have it
        int maxLabelFrequency = 0; // the max size of the int[] that stores the label deg seq
        id     = sc.next();
        order = sc.nextInt();
        degree = new int[order];
        neighbors = new BitSet[order];
        vlabels = new String[order];

        // initialize bitsets
        for (int i=0; i<order; i++) {
            neighbors[i] = new BitSet(order);
        }

        // construct vertices:
        for (int i=0; i<order; i++) {
            String newL = sc.next();
            vlabels[i] = newL;
            if (labels.get(newL) == null) {
                ArrayList<Integer> vertexid  = new ArrayList<>();
                vertexid.add(i);
                labels.put(newL,vertexid);
            }
            else{
                labels.get(newL).add(i);
                int labelFrequency = labels.get(newL).size();
                if (maxLabelFrequency < labelFrequency) {
                    maxLabelFrequency = labelFrequency;
                }
            }
        }

        // construct edges:
        size = sc.nextInt();
        for (int i=0;i< size;i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            neighbors[u].set(v,true);
            neighbors[v].set(u, true);
            degree[u] = degree[u] + 1;
            degree[v] = degree[v] + 1;
        }
        setDegreeSequence(labels, maxLabelFrequency);
    }

    /**
     * Sets the degree sequence for each unique label that occurs in the graph
     * @param labels is generated during the graph construction
     * */
    private void setDegreeSequence(HashMap<String,ArrayList<Integer>> labels, int frequency){
        int labelsN = labels.size();
        String label;
        Iterator labelsIterator = labels.keySet().iterator();
        ArrayList<Integer> vertexids;
        this.labels = new Label[labelsN];
        for (int i = 0; i < labelsN; i++){
            label = labelsIterator.next().toString();
            vertexids = labels.get(label);
            Label l = new Label(label,vertexids.size());
            this.labels[i] = l;
            for (int j = 0; j < vertexids.size(); j++) {
                int vdegree = this.degree[vertexids.get(j)];
                l.insertDegree(vdegree);
            }
        }
    }

    public void display(){
        System.out.println(id);
        System.out.println(order);
        for (int i=0;i< order;i++) System.out.println(vlabels[i]);
        System.out.println(size);
        for (int i=0;i< order -1;i++)
            for (int j=i+1;j< order;j++)
                if (neighbors[i].get(j)) System.out.println(i +" "+ j);
    }

    public void displayDegreeSequence(){
        System.out.println(this.getId());
        for (int i = 0; i < this.labels.length; i++) {
            System.out.print(this.labels[i].getLabel() + " <");
            int[] degrees = labels[i].getDegrees();
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
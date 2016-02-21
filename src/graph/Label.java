package graph;

/**
 * Created by iva on 2/7/16.
 */
public class Label {

    private String label;
    private int[] degrees;
    private int size; // the current size of the degrees

    public Label(String l, int degreeSeqSize) {
        this.label = l;
        degrees = new int[degreeSeqSize];
        size = 0;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    /** TODO optimize by making binary search */
    public void insertDegree(int degree) {
        if (size == 0) {
            degrees[0] = degree;
            size ++;
        }
        else if (degrees[size-1] > degree) {
            degrees[size] = degree;
            size ++;
        }
        else {
            for (int i = 0; i < size; i++) {
                int currDeg = degrees[i];
                if (currDeg <= degree) {
                    insert(i, degree);
                    break;
                }
            }
        }
        return;
    }

    public int getSize() {
        return size;
    }

    /**
     * Inserts an element @elem at position @index in the degree array
     * */
    private void insert(int index, int elem) {
        int[] remaining = new int[size-index];
        for (int i = index, j = 0; i < size; i++, j++) {
            remaining[j] = degrees[i];
        }
        degrees[index] = elem;
        size ++;
        for (int i = index + 1, j = 0; j < remaining.length; i++, j++) {
            degrees[i] = remaining[j];
        }
    }

    public String getLabel() {
        return label;
    }

    public int[] getDegrees() {
        return degrees;
    }
}

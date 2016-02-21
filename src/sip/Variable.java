package sip;
import java.util.*;

public class Variable {

    int index;
    BitSet domain;
    BitSet confSet;

    public Variable (int index,BitSet domain){
        this.index  = index;
        this.domain = domain;
        confSet     = null;
    }

    public Variable (int index,BitSet domain,BitSet confSet){
        this.index   = index;
        this.domain  = domain;
        this.confSet = confSet;
    }

    public String toString(){return index +": "+ domain +" "+ confSet;}

}
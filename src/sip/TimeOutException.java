package sip;

public class TimeOutException extends RuntimeException {
    public TimeOutException(){};
    public TimeOutException(String msg){super(msg);}
}

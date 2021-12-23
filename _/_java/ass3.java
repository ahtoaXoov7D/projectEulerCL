import java.util.Scanner;

public class ass5 {

  public static void main(String[] args) {
    
    double salary=0.0,ttax=0.0;
    Scanner obj=new Scanner(Systrm.in);
    System.out.println("enter your Basic Salary");
    salary=obj.nextDouble();
    if( salary>0.00 && salary<=14999.99)
    ttax=0.00+salary*0.15;
    else if(salary>15000.00 && salary<=29999.99)
    ttax=2250+(salary-15000.00)*0.18;
    else if(salary>30000.00 && salary<=49999.99)
    ttax= 5400+(salary-30000.00)*0.22;
    else if(salary>50000.00 && salary<=79999.99)
    ttax=11000+(salary-50000.00)*0.27;
    else if(salary>80000.00 && salary<=150000.00)
    ttax=21600+(salary-80000)*0.33;
    else
    System.out.println(-1.0);
    
   System.out.print(" total tax on"+salary+"="+ttax);
    
  }

}

import java.util.Scanner;

public class ass4 {

  public static void main(String[] args) {
    int a,b,c,d,result=0;
    Scanner obj=new Scanner(System.in);
     a=obj.nextInt();
     b=obj.nextInt();
     c=obj.nextInt();
     d=obj.nextInt();
    obj.close();
     result=(a>b)?((a>c)?((a>d)?a:d):c):((b>c)?((b>d)?b:d):c);
     System.out.println("largest number of"+a+','+b+','+','+c+','+','+d+ "="+result);
  }

}

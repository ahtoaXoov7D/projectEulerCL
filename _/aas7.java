import java.util.Scanner;

public class ass7 {

  public static void main(String[] args) {
    int a=8,b=90,r=0;
    char ch;
    Scanner y=new Scanner(System.in);
    System.out.print("please enter a desired operator");
    ch=y.next().charAt(0);
    y.close();
    switch(ch)
    {
      case '+':
      r=a+b;
      break;
      
      case '-':
      r=a-b;
      break;
      
      case '*':
      r=a*b;
      break;
      
      case '/':
      r=a/b;
      break;
      
      default:
      System.out.println(" you entered a wrong option");
      }
      System.out.println("result="+r);
      
    }
  }



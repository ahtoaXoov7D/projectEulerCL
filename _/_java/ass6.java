import java.util.Scanner;

public class ass6 { 
public void ifel(int year)
{
  int year=1948;
  if(year%400==0||year%100==0||year%4==0)
  {
    System.out.println(year+"= leap year");
  }
  else
  {
    System.out.println(year+"=not a leap year");
  }
  
}
public void nestif(int year)
{ 
System.out.print(year+" ");
  if(year%100==0)
    System.out.print(" a leap year");
    else{
      if( year%4==0)
         System.out.print("a leap year");
         else
         {
           System.out.println(" not a leap year");
         }
     }
  
}
public void ifelif(int year)
{
  if(year%400==0)
  System.out.println(year+"a leap year" );
  else if(year%100==0)
  System.out.println(year+"a leap year");
  else if(year%4==0)
  System.out.println(year+"a leap year");
  else
  System.out.println("not a leap year");
}
  public static void main(String[] args) {
   Scanner y=new Scanner(System.in);
   int year= y.nextInt();
   ifel();
   nestif();
   ifelif();
   y.close();
  }

}

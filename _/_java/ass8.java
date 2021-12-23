public class ass8{

  public static void main(String[] args) 
  {for(int r=1;r<4;r++)
  {
    for(int s=4;s>=r;s--)
    {
       System.out.print(" ");
    }
    for(int c=1;c<=(2*r-1);c++)
    {
       if(c%2==1)
       {
         System.out.print("*");
       }
       else if(c%2==0)
       System.out.print(" ");
    }
    System.out.println();
    }
  }

}
    

public class problem6
{
   public static void main(String args[])
   {
       int sum1=0,sum2=0;
       for(int i = 1;i<=100;i++)
       {
          sum1=sum1+i;
          sum2=sum2+(i*i);
        }
       int diff=(sum1*sum1)-sum2;
       System.out.println("The difference is : "+diff);
    }
}

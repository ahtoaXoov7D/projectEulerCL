
public class problem1
{
   public static void main(String args[]) 
   {
        int num = 1000;
       int sum =0;
       for(int i = 0;i<num;i++)
       {
           if((i%5==0)||(i%3==0))
           sum+=i;
        }
       System.out.println(sum);
    }
}

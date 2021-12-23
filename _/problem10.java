public class problem10
{
   static boolean primechecker(long n)
    {
        boolean status = true;
        for (int i = 3; i<=Math.sqrt(n);i+=2)
        {
            if (n%i==0)
            {
                status=false;
                break;
            }
        }
        return status;
    }
    public static void main(String args[])
    {
        
        long sum = 0;
        for(long i = 3 ;i<=2000000;i+=2) // no even number can be prime except 2
        {
            if(primechecker(i))
            {
                sum = sum +i;
            }
        }
        System.out.println(sum+2); //because 2 is not included
   }
}

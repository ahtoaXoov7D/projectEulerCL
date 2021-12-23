public class problem3 
{ 
    static long primefactmax( long n)
    {
        long maxPrime = -1;
        while (n % 2 == 0)    //it rejects all the even number 
        {
            maxPrime = 2;
            n/=2; 
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) //n must be odd by the time it enters here
        {
            while (n % i == 0) {
                maxPrime = i;
                n /= i;
            }
        }
        if (n > 2)                //n must be prime by the time it enters here
            maxPrime = n;
        return maxPrime;
    }

    public static void main(String[] args)
    {
        long n = 600851475143l;   //the last value is l not 1 just to handle long numbers
        System.out.println(primefactmax(n));
    }
}


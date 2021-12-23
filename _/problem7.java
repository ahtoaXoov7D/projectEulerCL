public class problem7
{
    public static void main(String args[])
    {
        int n,count=0;
        int status = 1;
        int num = 3;
        n=10001;
        int arr[]=new int[n];
        System.out.println("The "+n+"st prime numbers is:");
        for ( int i = 2 ; i <=n ;)
        {
            for ( int j = 2 ; j <= Math.sqrt(num) ; j++ )
            {
                if ( num%j == 0 )
                {
                    status = 0;
                    break;
                }
            }
            if ( status != 0 )
            {
                arr[i-2]=num;
                i++;
            }
            status = 1;
            num++;
        }   
        System.out.println(arr[n-2]);
    }
}
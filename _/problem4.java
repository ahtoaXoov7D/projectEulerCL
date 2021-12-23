public class problem4
{
    static int productpalindrome(int n)
    {
        int up_lmt = 0;
        for (int i=1; i<=n; i++)
        {
            up_lmt *= 10;
            up_lmt += 9;
        }
        int lwr_lmt = 1 + up_lmt / 10;
        int mul_max = 0;

        for (int i = up_lmt; i >= lwr_lmt; i--)
        {
            for (int j = i; j >= lwr_lmt; j--)
            {
                int product = i * j;
                if (product < mul_max)
                    break;
                int number = product;
                int reverse = 0;
                while (number != 0)
                {
                    reverse = reverse * 10 + number % 10;
                    number /= 10;
                }
                if (product == reverse && product > mul_max)
                    mul_max = product;
            }
        }
        return mul_max;
    }

    public static void main (String[] args)
    {

        int n = 3;
        System.out.print(productpalindrome(n));
    }
}

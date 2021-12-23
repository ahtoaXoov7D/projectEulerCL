public class prolem9
{
    public static void main(String[] args) 
    {
        for (int a = 3; a <= 1000; a++) 
        {
            for (int b = a + 1; b < 1000; b++)
            {
                double csquare = Math.pow(a, 2) + Math.pow(b, 2);
                double c = Math.pow(csquare, 0.5);
                if (a + b + c == 1000)
                {
                    System.out.println((int)(a * b * c));
                    break;
                }
            }
        }
    }
}

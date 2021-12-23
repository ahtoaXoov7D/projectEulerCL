
  /**
   * By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
     find the sum of the even-valued terms.
   *
   * @author Tarantino O'Connor
   * @version 1 14.10.17
  */
class Solution002
{
    public static void main(String[] args)
    {
         new Solution002();
    }

    public Solution002()
    {
        int previous = 0;
        int current = 1;
        int nextNumber = 2;
        int sum = 0;
        do 
        {
            nextNumber = previous + current;
            if(nextNumber >= 4000000) // Checks whether the next Number is larger than 4 million, if so then break the looop and do not process it.
            {
             break;
            }
            previous = current; 
            current = nextNumber;
            if(nextNumber % 2 == 0) // checks whether the next number is even.
            {
             sum = sum + nextNumber;
            }
        }
        while(nextNumber < 4000000);
        System.out.println(sum); //Prints the output of the summation of all even numbers.
    }
}

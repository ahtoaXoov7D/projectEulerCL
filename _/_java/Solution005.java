import java.util.*;
/**
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 *
 * @author Tarantino O'Connor
 * @version 1 15.10.17
 */
class Solution005
{
    public static void main(String[] args)
    {
        new Solution005();
    }

    public Solution005()
    {
        boolean looking = true; // Initially set to true for the loop to start.
        int number = 1; // Starting number.
        int count = 0;  // Tests whether 20 divisions has occured.
        do
        {
            number++; // Initially adds 1 onto the number before the loop rather than after, as this would add '1' onto the answer.
            for(int i = 1; i <= 20; i++) //
            {
                if(number % i == 0) // When divided by the numbers 1-20, is the modulus '0' meaning there is no remainder.
                {
                    count++; //if divisible giving a whole number, add one onto the count.
                    if(count == 20) // If all 20 numbers can be divided into the number then stop looking.
                    {
                        looking = false; // Allows the do-while loop to stop running.
                    }
                }
                else
                {
                    count = 0; //If the modulus is not 0 then it is not divisible, so reset the count.
                    break; // Break the loop to start again with the next highest number.
                }
            }
        }
        while(looking); // continue looking for the smallest number divisble by 1-20 while true.
        System.out.println(number); //print the result.
    }

}

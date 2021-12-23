import java.util.*;
import java.math.BigInteger; 
/**
   * The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
   *
   * @author Tarantino O'Connor
   * @version 1 14.10.17
  */
class Solution003
{
    public static void main(String[] args)
    {
         new Solution003();
    }

    public Solution003()
    {
        BigInteger number = new BigInteger("600851475143"); //The value is much too large to be stored as an integer so the class BigInteger is used.
        BigInteger zero = new BigInteger("0");
        BigInteger one = new BigInteger("1");
        BigInteger two = new BigInteger("2");
        Set<BigInteger> primesSet = new HashSet<BigInteger>(); // This hashset will be used to store all the distinct prime numbers of the type BigInteger.
        for(BigInteger i = two; i.compareTo(number) == -1 || i.compareTo(number) == 0; i = i.add(one)) // Ensures that it runs from 2 up to itself.
        {
         if(number.mod(i).compareTo(zero) == 0) //If there is no remainder then it must be a prime number.
         {
            primesSet.add(i); //Adds the prime number to the Hashset.
            number = number.divide(i); //This halves the number allowing the next prime number to be found.
            i = i.subtract(one); //This allows i to return to the digit before to test from that value.
         }
        }
        System.out.println(Collections.max(primesSet)); // The Collections class has a useful method (max) of outputting the largest number in a collection.        
    }
}

import java.util.*;
/**
   * Find the largest palindrome made from the product of two 3-digit numbers.
   *
   * @author Tarantino O'Connor
   * @version 1 15.10.17
  */
class Solution004
{
    public static void main(String[] args)
    {
         new Solution004();
    }

    public Solution004()
    {
        int product = 0; // To store the product of both the three digit numbers.
        Set<Integer> palindromes = new HashSet<Integer>(); //To store the distinct palindromes that occur.
        for(int i = 100; i <=999; i++) // The two digit limit.
        {
         for(int j = 100; j <=999; j++)
         {
          product = i*j; // The product of the two three digit numbers.
          String strProduct = Integer.toString(product); //Converts the product to a string to allow for each of the digits to be accessed.
          char[] arrayLength5 = new char[5]; //Creates an array for the lowest amount of digits which is 5 (100*100 = 10000). 
          char[] arrayLength6 = new char[6]; //Creates an array for the highest amount of digits which is 6 (999*999 = 998001). 
          if(strProduct.length() == 5) // If a 5 digit number.
          {
            for(int k = 0; k < strProduct.length(); k++ )
            {
             arrayLength5[k] = strProduct.charAt(k); //Add each digit to the 5 digit array.
            }
            if((arrayLength5[0] == arrayLength5[4]) && (arrayLength5[1] == arrayLength5[3]))
             {
              palindromes.add(product); // For the respective positions for a 5 digit number, for it to qualify as a palindrome, if the values there are equal then add it to the hashset.
             }
          }
          else if(strProduct.length() == 6)// If a 6 digit number.
          {
           for(int l = 0; l < strProduct.length(); l++ )
            {
             arrayLength6[l] = strProduct.charAt(l); //Add each digit to the 6 digit array.
            }
           if((arrayLength6[0] == arrayLength6[5]) && (arrayLength6[1] == arrayLength6[4]) && (arrayLength6[2] == arrayLength6[3]))
             {
              palindromes.add(product); // For the respective positions for a 6 digit number, for it to qualify as a palindrome, if the values there are equal then add it to the hashset.
             }
          }
         }
        }
        System.out.println(Collections.max(palindromes)); //Print the contents of the HashSet.
    }
}
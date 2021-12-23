import java.util.*;
/**
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 *
 * @author Tarantino O'Connor
 * @version 1 15.10.17
 */
class Solution022
{
    public static void main(String[] args)
    {
        new Solution005();
    }

    public Solution022()
    {
    	Scanner s = new Scanner(System.in);
		int countNames = s.nextInt();
		s.nextLine();

		ArrayList<String> names = new ArrayList<String>();

		for (int i = 0; i<countNames; i++){
			names.add(s.nextLine());
		}
		names.sort(String::compareTo);

		int testcases = s.nextInt();
		s.nextLine();
		
		for (int i = 0; i<testcases; i++){
			String name = s.next();
			int namescore = 0;
			char[] ch = name.toCharArray();
			for (char c : ch){
				int temp = (int)c;
				int temp_integer = 64;
				if(temp<=90 & temp>=65)
					namescore += (temp-temp_integer);
			}
			namescore = namescore*(names.indexOf(name)+1);
			System.out.println(namescore);
		}
    }

}

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> listOfPrimes = new ArrayList<>();
        listOfPrimes.add(2);
        int currentNumber = 3;
        boolean isPrime;

        while(listOfPrimes.size() < 10001) {
            isPrime = true;
            for (int number : listOfPrimes) {
                if (currentNumber % number == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                listOfPrimes.add(currentNumber);
            }
            currentNumber++;
        }
        System.out.println("The 10001st prime number is: " + listOfPrimes.get(listOfPrimes.size() - 1));
    }
}

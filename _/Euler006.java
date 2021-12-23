public class Main {

    public static void main (String[] args) {
        int sumOfSquares = 0;
        int squareOfSum = 0;
        int diffenerce;

        for (int i = 1; i < 101; i++) {
            sumOfSquares += i*i;
            squareOfSum += i;
        }

        squareOfSum = squareOfSum * squareOfSum;
        diffenerce = squareOfSum - sumOfSquares;

        System.out.println("The square of the sum of the first 100 natural numbers is: " + squareOfSum);
        System.out.println("The sum of the square of the fitst 100 natural numbers is: " + sumOfSquares);
        System.out.println("Thew difference between the 2 are: " + diffenerce);
    }
}

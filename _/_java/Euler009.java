
public class Euler009 {
	public static void main(String[] args) {
		int a = 1;
		int b = 1;
		int c = 998;
		int max = 998;
		
		while (Math.pow(a,2) + Math.pow(b,2) != Math.pow(c,2)) {
			if (c == 1) {
				a++;
				max--;
				c = max;
				b = 1;
			}
			c--;
			b++;
		}
		System.out.println(a + "² + " + b + "² = " + (int)Math.pow(a, 2) + " + " + (int)Math.pow(b,2) + " = " + c + " = " + c +"²");
	}
}

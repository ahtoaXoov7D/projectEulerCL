package project.euler;

public class Pthag {

	public static int maxCount = 0;
	public static int pValue;

	public static void main(String[] args) {

		long timer = System.currentTimeMillis();

		for (int p = 12; p <= 1000; p += 2) {
			int tripleCount = 0;

			for (int a = 3; a < (p / 3); a++) {

				for (int b = a + 1; b < ((p - a) / 2); b++) {

					int c = (p - (a + b));
					if ((a * a + b * b) == (c * c))
						tripleCount++;

				} // b for

			} // a for
			if (tripleCount > maxCount) {
				pValue = p;
				maxCount = tripleCount;
			}

		} // p for

		System.out.println(maxCount + " " + pValue);

		System.out.print(System.currentTimeMillis() - timer);

	} // main

}// Pthag

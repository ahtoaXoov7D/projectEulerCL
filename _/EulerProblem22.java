import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class EulerQuestion22 {

	public static void main(String[] args) {
		String path = "P:\\Text.txt";
		long sum = 0;
		int count = 1;
		try {
			String content = new String(Files.readAllBytes(Paths.get(path)));
			String[] inputArray;
			
			List<String> inputList = new ArrayList<String>();
			inputArray = content.split(",");
			
			Collections.addAll(inputList, inputArray);
			Collections.sort(inputList);
			
			StringTokenizer st = new StringTokenizer(inputList.toString(), "[ \" , ]", false);

			while (st.hasMoreElements()) {
				String name = st.nextToken();
				int value = 0;
				for (int i = 0; i < name.length(); i++) {
					value = value + (name.charAt(i) - 'A' + 1);
				}
				sum = sum + value * count;
				count = count + 1;
			}
			System.out.println("Sum is : " + sum);

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}

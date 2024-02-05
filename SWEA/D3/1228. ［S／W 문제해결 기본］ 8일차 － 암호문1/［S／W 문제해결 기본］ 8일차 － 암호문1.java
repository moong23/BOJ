import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
class Solution
{
	 public static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int tc = 1; tc <= 10; tc++) {
            int N = Integer.parseInt(br.readLine());
            LinkedList<String> cipherList = new LinkedList<>();
            String[] originalCipher = br.readLine().split(" ");
            for (String num : originalCipher) {
                cipherList.add(num);
            }

            int commandCount = Integer.parseInt(br.readLine());
            String[] commands = br.readLine().split("I "); // splits the command by "I "

            for (String command : commands) {
                if (command.isEmpty()) continue; // Skip empty commands
                String[] parts = command.split(" "); // split the commands with whitespace
                int x = Integer.parseInt(parts[0]); // Starting position for the insert
                int y = Integer.parseInt(parts[1]); // Number of elements to insert
                for (int j = 0; j < y; j++) {
                    cipherList.add(x + j, parts[j + 2]); // add integer to linkedList
                }
            }

            sb.append("#").append(tc).append(" ");
            for (int i = 0; i < 10 && i < cipherList.size(); i++) {
                sb.append(cipherList.get(i)).append(" "); // prints out first 10 elements
            }
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}

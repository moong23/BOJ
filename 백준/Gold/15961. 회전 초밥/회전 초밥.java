
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // Set up BufferedReader and StringTokenizer for input reading
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // Reading the initial input values
        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        
        // Initialize the sushi array
        int[] sushi = new int[N];
        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }
        
        // Using HashMap to keep track of the count of each sushi type
        HashMap<Integer, Integer> current = new HashMap<>();
        
        int _max = -1;
        int _cnt = 0;
        
        // Initial count for the first-k sushi
        for (int i = 0; i < k; i++) {
            current.put(sushi[i], current.getOrDefault(sushi[i], 0) + 1);
            if (current.get(sushi[i]) == 1) {
                _cnt += 1;
            }
        }
        
        // Check if the coupon sushi is already in the initial selection
        if (!current.containsKey(c)) {
            _max = _cnt;
        } else {
            _max = _cnt - 1;
        }
        
        int start = 0;
        while (start < N) {
            if (current.get(sushi[start]) == 1) {
                _cnt -= 1;
            }
            current.put(sushi[start], current.get(sushi[start]) - 1);
            
            int nextIndex = (start + k) % N;
            current.put(sushi[nextIndex], current.getOrDefault(sushi[nextIndex], 0) + 1);
            if (current.get(sushi[nextIndex]) == 1) {
                _cnt += 1;
            }
            
            if (current.containsKey(c) && current.get(c) >= 1) {
                _cnt -= 1;
            }
            _max = Math.max(_max, _cnt);
            
            if (current.containsKey(c) && current.get(c) >= 1) {
                _cnt += 1;
            }
            start += 1;
        }
        
        // Print the maximum number of unique sushis + 1 for the coupon
        System.out.println(_max + 1);
    }
}


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int N, cnt;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(br.readLine());
		
		valid: {			
			while(N % 5 != 0) {
				N -= 3;
				if(N < 0) {
					cnt = -1;
					break valid;
				}
				cnt++;
			}
			cnt += N / 5;
		}
		
		bw.write(cnt + "");
		
		bw.flush();
		bw.close();
	}

}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder(6);
	public static int R, G, B;
	public static int N, r, g, b;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		N = Integer.parseInt(br.readLine());
		
		for(int i=0;i<N;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int _r, _g, _b;
			_r = Math.min(G,  B) + Integer.parseInt(st.nextToken());
			_g = Math.min(B,  R) + Integer.parseInt(st.nextToken());
			_b = Math.min(R,  G) + Integer.parseInt(st.nextToken());
			R = _r;
			G = _g;
			B = _b;
		}
		
		sb.append(Math.min(Math.min(R,  G), B));
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

}

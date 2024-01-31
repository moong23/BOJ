import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int N, M, start, end;
	public static int[] inArr, sumArr;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		inArr = new int[N];
		sumArr = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			inArr[i] = Integer.parseInt(st.nextToken());
			sumArr[i+1] = sumArr[i] + inArr[i];
		}
		
		
		for(int i=0;i<M;i++) {
			st = new StringTokenizer(br.readLine());
			start = Integer.parseInt(st.nextToken());
			end = Integer.parseInt(st.nextToken());
			
			sb.append(sumArr[end] - sumArr[start-1]).append("\n");
		}
		System.out.println(sb);
	}

}

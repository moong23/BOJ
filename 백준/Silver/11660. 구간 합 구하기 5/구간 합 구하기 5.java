import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int N, M, x1, x2, y1, y2;
	public static int[][] sumArr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		sumArr = new int[N+1][N+1];
		
		// row direction cumulative sum array
		for(int i=1;i<=N;i++) {
			st = new StringTokenizer(br.readLine());
			 for(int j=1;j<=N;j++) {
				 sumArr[i][j] = sumArr[i][j-1] + Integer.parseInt(st.nextToken());
			 }
		}
		
		// col direction cumulative sum array to create 2d cumulative array
		for(int i=2;i<=N;i++) {
			for(int j=1;j<=N;j++) {
				sumArr[i][j] += sumArr[i-1][j];
			}
		}
		// handling tc
		for(int tc=0;tc<M;tc++) {
			st = new StringTokenizer(br.readLine());
			x1 = Integer.parseInt(st.nextToken());
			y1 = Integer.parseInt(st.nextToken());
			x2 = Integer.parseInt(st.nextToken());
			y2 = Integer.parseInt(st.nextToken());
			
			sb.append(sumArr[x2][y2] - sumArr[x1-1][y2] - sumArr[x2][y1-1] + sumArr[x1-1][y1-1]).append("\n");
		}
		
//		for(int i=0;i<=N;i++) {
//			for(int j=0;j<=N;j++) {
//				System.out.print(sumArr[i][j] + " ");
//			}
//			System.out.println("");
//		}
		System.out.println(sb);
	}

}

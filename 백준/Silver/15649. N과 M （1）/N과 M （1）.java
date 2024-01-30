import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static int N;
	public static int M;
	public static int[] numArr;
	public static boolean[] visited;
	public static StringBuilder sb = new StringBuilder(40320);
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		numArr = new int[M];
		visited = new boolean[N];

		dfs(0);
		System.out.println(sb);
	}
	
	public static void dfs(int depth) {
		if (depth == M) {
			for(int num : numArr) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (!visited[i]) {
				visited[i] = true;
				numArr[depth] = i + 1;
				dfs(depth + 1);
				visited[i] = false;
			}
		}
	}

}
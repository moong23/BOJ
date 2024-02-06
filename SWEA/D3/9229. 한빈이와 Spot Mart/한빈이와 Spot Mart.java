import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
class Solution
{
	public static StringBuilder sb = new StringBuilder();
	public static int T, N, M, start, end, _sum, snack[];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			snack = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				snack[i] = Integer.parseInt(st.nextToken());
			}
			Arrays.sort(snack);
			start = 0;
			end = snack.length - 1;
			_sum = snack[start] + snack[end];
			if (_sum > M)
				_sum = -1;
			while (start < end) {
				if (snack[start] + snack[end] == M) {
					_sum = M;
					break;
				}
				if (snack[start] + snack[end] > M) { // when sum of weight is bigger than target
					end--;
				} else {
					_sum = Math.max(_sum, snack[start] + snack[end]);
					start++;
				}
			}
			sb.append("#").append(tc).append(" ").append(_sum).append("\n");
		}
		bw.write(sb.toString());

		bw.flush();
		bw.close();
	}

}
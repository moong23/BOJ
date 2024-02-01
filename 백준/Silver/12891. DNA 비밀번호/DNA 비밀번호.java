
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int S, P, _cnt, start, end;
	public static char[] dna;
	public static int[] condition, current;
	public static final String DNA = "ACGT";

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		S = Integer.parseInt(st.nextToken());
		P = Integer.parseInt(st.nextToken());
		dna = br.readLine().toCharArray();
		condition = new int[4];
		current = new int[4];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			condition[i] = Integer.parseInt(st.nextToken());
		}

		// initialize current array with the first window
		for (int idx = 0; idx < P; idx++) {
			current[DNA.indexOf(dna[idx])]++;
		}

		for (start = 0, end = start + P; end <= S; start++, end++) {
			// check if string is valid
			isValid: {
				for (int i = 0; i < 4; i++) {
					if (current[i] < condition[i])
						break isValid;
				}
				_cnt++;
			}
			if (end == S)
				break;
			current[DNA.indexOf(dna[start])]--;
			current[DNA.indexOf(dna[end])]++;
		}

		sb.append(_cnt);
		System.out.println(sb);
	}

}

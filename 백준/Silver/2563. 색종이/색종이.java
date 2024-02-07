import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int N, size[][], _x, _y, _cnt;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		size = new int[100][100];

		N = Integer.parseInt(br.readLine());

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			_x = Integer.parseInt(st.nextToken());
			_y = Integer.parseInt(st.nextToken());

			for (int y = _y; y < _y + 10; y++) {
				for (int idx = 0; idx < 10; idx++) {
					size[_x+idx][y] = 1;
				}
			}
		}
		
//		System.out.println(Arrays.deepToString(size));
		
		for(int i=0;i<100;i++) {
			for(int j=0;j<100;j++) {
				_cnt += size[i][j];
			}
		}
		System.out.println(_cnt);
		bw.flush();
		bw.close();
	}

}

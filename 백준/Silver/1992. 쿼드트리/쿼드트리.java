
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 * Using Recursive Function
 * check if given checking array is consisted with all the same number
 * if true, print the number and finish recursion
 * if false, stop checking and divide array to 1/4 size and start +1 recursion
 */
public class Main {
	/**
	 * sb : StringBuilder
	 * N : size of the initial array
	 * arr : saves numbers in 2d array
	 */
	public static StringBuilder sb = new StringBuilder();
	public static int N, arr[][];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			String[] _tmp = br.readLine().split("");
			for(int j=0;j<N;j++) {
				arr[i][j] = Integer.parseInt(_tmp[j]);
			}
		}

		// start bfs with the biggest array (left top [0,0], size N)
		check(0, 0, N);

		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

	/**
	 * 
	 * @param x : left top x coordinate
	 * @param y : left top y coordinate
	 * @param size : size of the array to check
	 */
	public static void check(int x, int y, int size) {
		// iteration to check if the array is consisted with the same number
		isSame: {
			int _tmp = arr[x][y];
			for(int i=0;i<size;i++) {
				for(int j=0;j<size;j++) {
					if (arr[x+i][y+j] != _tmp)
						break isSame;
				}
			}
			// if consisted with one number, append the number and end recursion
			sb.append(_tmp);
			return;
		}
		// when all the element aren't same, divide into 1/4 size array
		int _idx = size/2;
		sb.append("(");
		check(x, y, _idx); // left top cell
		check(x, y+_idx, _idx); // right top cell
		check(x+_idx, y, _idx); // left btm cell
		check(x+_idx, y+_idx, _idx); // right btm cell
		sb.append(")");
	}
}

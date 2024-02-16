import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int R, C, _max;
	public static int[][] dirCoord = {{-1,0}, {0, 1}, {1, 0}, {0, -1}};
	public static boolean visited[] = new boolean[26];
	public static char[][] board;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new char[R][C];
		
		for(int i=0;i<R;i++) {
			board[i] = br.readLine().toCharArray();
		}
		
		dfs(0,0,0);
		if(_max == 0)_max+=1;
		bw.write(_max+"");
		bw.flush();
		bw.close();
	}
	
	public static void dfs(int x, int y, int cnt) {
		if(visited[board[x][y]-'A'] == true) {
			_max = Math.max(_max,  cnt);
			return;
		} else {
			visited[board[x][y]-'A'] = true;
			for(int i=0;i<4;i++) {
				if(x+dirCoord[i][0] >= 0 && x + dirCoord[i][0] <R
						&& y + dirCoord[i][1] >= 0 && y + dirCoord[i][1] < C) {
					dfs(x+dirCoord[i][0], y+dirCoord[i][1], cnt+1);
				}
			}
			
			
			visited[board[x][y]-'A'] = false;
		}
	}

}

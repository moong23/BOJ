import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution
{
		public static StringBuilder sb = new StringBuilder();
	public static int T, H, W, N;
	public static char map[][], command[];
	public static final String direction = "URDL", orientations = "^>v<";
	public static final int[][] dirCoord = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
	public static int dir, tankRow, tankCol;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");
			String[] _tmp = br.readLine().split(" ");
			H = Integer.parseInt(_tmp[0]);
			W = Integer.parseInt(_tmp[1]);
			map = new char[H][W];

			for (int i = 0; i < H; i++) {
				map[i] = br.readLine().toCharArray();
			}

			N = Integer.parseInt(br.readLine());
			command = new char[N];
			command = br.readLine().toCharArray();

			tankRow = -1;
			tankCol = -1;

			// block to find initial tank position, direction
			findTank: {
				for (int i = 0; i < H; i++) {
					for (int j = 0; j < W; j++) {
						char current = map[i][j];
						if (orientations.contains(String.valueOf(current))) {
							tankRow = i;
							tankCol = j;
							// Set the initial direction based on the tank's orientation
							dir = orientations.indexOf(current);
							break findTank;
						}
					}
				}
			}

//			System.out.println(Arrays.deepToString(map));

			for (char cmd : command) {
				switch (cmd) {
				case 'S':
					int idx = 1;
					while (true) {
						if (tankRow + dirCoord[dir][0] * idx < 0 || tankRow + dirCoord[dir][0] * idx >= H
								|| tankCol + dirCoord[dir][1] * idx < 0 || tankCol + dirCoord[dir][1] * idx >= W) {
							break;
						}
						if (map[tankRow + dirCoord[dir][0] * idx][tankCol + dirCoord[dir][1] * idx] == '*') {
							map[tankRow + dirCoord[dir][0] * idx][tankCol + dirCoord[dir][1] * idx] = '.';
							break;
						} else if (map[tankRow + dirCoord[dir][0] * idx][tankCol + dirCoord[dir][1] * idx] == '#') {
							break;
						}
						idx++;
					}
					break;
				default:
					dir = direction.indexOf(cmd);
					int _targetdir[] = dirCoord[dir];
					if(tankRow + _targetdir[0] != -1 && tankRow + _targetdir[0] != H 
							&& tankCol + _targetdir[1] != -1 && tankCol + _targetdir[1] != W) {
						if(map[tankRow + _targetdir[0]][tankCol + _targetdir[1]] == '.'){
							map[tankRow][tankCol] = '.';
							tankRow += _targetdir[0];
							tankCol += _targetdir[1];
						}
					}
					map[tankRow][tankCol] = orientations.charAt(dir);
					
					break;
				}	
			}
			for(int i=0;i<H;i++) {
				for(int j=0;j<W;j++) {
					sb.append(map[i][j]);
				}
				sb.append("\n");
			}
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}

}

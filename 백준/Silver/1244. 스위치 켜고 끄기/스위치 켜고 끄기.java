import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int switchNum = Integer.parseInt(br.readLine());
		int[] switchArr = new int[switchNum];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0;i<switchNum;i++) {
			switchArr[i] = Integer.parseInt(st.nextToken());
		}
		
		
		int stNum = Integer.parseInt(br.readLine());
		int target;
		
		for(int i=stNum;i>0;i--) {
			st = new StringTokenizer(br.readLine());
			if(Integer.parseInt(st.nextToken()) == 1) { // 남학생의 경우
				target = Integer.parseInt(st.nextToken());
				for(int idx = target-1;idx<switchNum;idx+=target) {
					switchArr[idx] = 1 - switchArr[idx];
				}
			} else { // 여학생의 경우
				target = Integer.parseInt(st.nextToken()) - 1;
				int _idx = 1;
				switchArr[target] = 1 - switchArr[target];
				while (true) {
					if (target - _idx < 0 || target + _idx >= switchNum) break;
					if(switchArr[target - _idx] == switchArr[target + _idx]) {
						switchArr[target + _idx] = switchArr[target - _idx] = 1 - switchArr[target - _idx];
						_idx += 1;
					} else {
						break;
					}
				}
			}
		}
		for(int i=0;i<switchNum;i++) {
			if (i!=0 && i%20 == 0) sb.append("\n");
			sb.append(switchArr[i]).append(" ");
		}
		System.out.println(sb);
	}
}
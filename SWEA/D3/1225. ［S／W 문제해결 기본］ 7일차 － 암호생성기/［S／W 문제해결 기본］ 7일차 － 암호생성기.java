import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Solution
{
    public static StringBuilder sb = new StringBuilder();
	public static ArrayDeque<Integer> arrQ;
	public static int iterIdx;
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int tc = 1;tc<=10;tc++) {
			iterIdx = 1;
			arrQ = new ArrayDeque<Integer>();
			br.readLine();
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i=0;i<8;i++) {
				arrQ.add(Integer.parseInt(st.nextToken()));
			}
		
			while(true) {
				int target = arrQ.pollFirst();
				if(target - iterIdx <= 0) {
					arrQ.addLast(0);
					break;
				}
				arrQ.addLast(target - iterIdx);
				
				
				
				iterIdx++;
				if(iterIdx >5)iterIdx-=5;
			}
			
			sb.append("#").append(tc).append(" ");
			for(int i=0;i<8;i++) {
				sb.append(arrQ.pollFirst()).append(" ");
			}
			sb.append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
	}
}
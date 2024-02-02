/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    public static StringBuilder sb = new StringBuilder();
	public static int tcNum, _cnt;
	public static char[] inStr;
	public static boolean success;
	public static ArrayDeque<Character> parStack;
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int tc=1;tc<=10;tc++) {
			_cnt = 0;
			tcNum = Integer.parseInt(br.readLine());
			parStack = new ArrayDeque<Character>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			inStr = st.nextToken().toCharArray();
			
			checkPar: {
				for(int i=0;i<tcNum;i++) {
					if(_cnt - 1 > tcNum/2) {
						sb.append("#").append(tc).append(" ").append(0).append("\n");
						break checkPar;
					}
					switch(inStr[i]) {
					case ')':
						if(parStack.pollLast() != '(') {
							sb.append("#").append(tc).append(" ").append(0).append("\n");
							break checkPar;
						}
						_cnt--;
						break;
					case ']':
						if(parStack.pollLast() != '[') {
							sb.append("#").append(tc).append(" ").append(0).append("\n");
							break checkPar;
						}
						_cnt--;
						break;
					case '}':
						if(parStack.pollLast() != '{') {
							sb.append("#").append(tc).append(" ").append(0).append("\n");
							break checkPar;
						}
						_cnt--;
						break;
					case '>':
						if(parStack.pollLast() != '<') {
							sb.append("#").append(tc).append(" ").append(0).append("\n");
							break checkPar;
						}
						_cnt--;
						break;
					default:
						parStack.addLast(inStr[i]);	
						_cnt++;
						break;
					}
				}
				
				sb.append("#").append(tc).append(" ").append(1).append("\n");
			}
			
			
			
		}
		bw.write(sb.toString());
		
		bw.flush();
		bw.close();
	}
}
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
import java.io.IOException;
import java.io.InputStreamReader;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    public static StringBuilder sb = new StringBuilder();
	public static String line;
	public static int increaseNum = 2;
	public static int idxNum = 1;
	public static int T, num, target, _sum;
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());

		for (int tc = 0; tc < T; tc++) {
			_sum = 0;
			num = Integer.parseInt(br.readLine());
			for (int i = 0; i < num; i++) {
				line = br.readLine();
				for (int j = 0; j < num; j++) {
					if (i <= num / 2) // 위쪽 영역
					{
						if (i + j <= num / 2 - 1) // 왼쪽 위 공백
							continue;
						else if (j - i >= num / 2 + 1) // 오른쪽 위 공백
							continue;
						else
							_sum += Integer.parseInt(Character.toString(line.charAt(j)));

					} else if (i > num / 2)// 아래쪽 영역
					{
						if (i - j >= num / 2 + 1)// 왼쪽 밑 공백
							continue;
						else if (i + j >= num / 2 * 3 + 1)// 오른쪽 및 공백
							continue;
						else
							_sum += Integer.parseInt(Character.toString(line.charAt(j)));

					}
				}
			}
			sb.append("#").append(tc + 1).append(" ").append(_sum).append("\n");
		}
		System.out.println(sb);

	}
}
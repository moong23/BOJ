import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * N for _ in range(N)]

target = list(map(int, input().split()))

for i in range(N):
    for start in range(N - i):
        end = start + i

        if start == end:
            dp[start][end] = 1
        elif target[start] == target[end]:
            if start == end - 1:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1


M = int(input())
for _ in range(M):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])

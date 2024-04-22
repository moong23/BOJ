import sys
input = sys.stdin.readline

N = int(input())

jump = []
for _ in range(N):
    jump.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)]for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == j == N-1:
            print(dp[i][j])
            exit(0)
        tmp = jump[i][j]
        if i + tmp < N:
            dp[i + tmp][j] += dp[i][j]
        if j + tmp < N:
            dp[i][j+tmp] += dp[i][j]

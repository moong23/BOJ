import sys
input = sys.stdin.readline

N = int(input())
T, P = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    fin_date = i + T[i] - 1
    if fin_date <= N:
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + P[i])
print(max(dp))

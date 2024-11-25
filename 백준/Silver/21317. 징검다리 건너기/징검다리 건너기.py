import sys

input = sys.stdin.read
data = input().splitlines()

INF = 1_000_000
n = int(data[0])
bridge = [(0, 0)] * (n + 4)
dp = [[INF, INF] for _ in range(n + 4)]

for i in range(1, n):
    a, b = map(int, data[i].split())
    bridge[i] = (a, b)

k = int(data[n])

dp[1][0] = 0
for i in range(1, n + 1):
    if i + 1 <= n:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + bridge[i][0])
    if i + 2 <= n:
        dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + bridge[i][1])
    if i + 3 <= n:
        dp[i + 3][1] = min(dp[i + 3][1], dp[i + 2][1] + bridge[i + 2][0])
        dp[i + 3][1] = min(dp[i + 3][1], dp[i + 1][1] + bridge[i + 1][1])
        dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + k)


print(min(dp[n][0], dp[n][1]))

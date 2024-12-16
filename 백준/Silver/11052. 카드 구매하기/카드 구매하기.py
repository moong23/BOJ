n = int(input())
arr = [0]
dp = [0] * (n + 1)

for x in map(int, input().split()):
    arr.append(x)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + arr[j])

print(dp[n])

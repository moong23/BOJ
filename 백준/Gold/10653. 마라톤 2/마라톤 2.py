import sys
input = sys.stdin.readline

def fn(x1, x2):
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

n, m = map(int, input().split())
board = [[0] * 2 for _ in range(n + 1)]

for i in range(1, n + 1):
    x, y = map(int, input().split())
    board[i][0] = x
    board[i][1] = y

dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[1][0] = 0  

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + fn(board[i], board[i - 1])

    for j in range(1, m + 1):
        idx = j
        for k in range(i - 1, 0, -1):
            if dp[k][idx] != float('inf'):
                dp[i][j] = min(dp[i][j], dp[k][idx] + fn(board[i], board[k]))
            idx -= 1
            if idx < 0:
                break

result = min(dp[n][i] for i in range(m + 1))
print(result)

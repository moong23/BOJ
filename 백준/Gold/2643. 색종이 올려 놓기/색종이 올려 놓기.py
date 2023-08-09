n = int(input())
papers = []

for _ in range(n):
    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    papers.append((A, B))

papers.sort(reverse=True)

dp = [1] * n

for i in range(n):
    for j in range(i):
        if papers[i][0] <= papers[j][0] and papers[i][1] <= papers[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

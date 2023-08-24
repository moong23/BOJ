import sys
sys.setrecursionlimit(10**5)
N, M, K = map(int, sys.stdin.readline().split())
graph = [[0]*M for _ in range(N)]
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
visit = [[0]*M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
res = 0


def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = 1
                cnt += 1
                dfs(nx, ny)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visit[i][j]:
            cnt = 0
            dfs(i, j)
            res = max(res, cnt)
print(res)

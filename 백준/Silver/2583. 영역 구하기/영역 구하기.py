# https://www.acmicpc.net/problem/2583
import sys
sys.setrecursionlimit(10**6)


def bfs(sx, sy):
    global area
    if sx < 0 or sx >= M or sy < 0 or sy >= N:
        return 0
    if visited[sx][sy] == 1:
        return 0
    area += 1
    visited[sx][sy] = 1
    for mx, my in ([-1, 0], [1, 0], [0, -1], [0, 1]):
        bfs(sx+mx, sy+my)

    return area


M, N, K = map(int, input().split())
visited = [[0] * N for _ in range(M)]
area = 0
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            visited[y][x] = 1
res = []
for i in range(M):
    for j in range(N):
        cnt = bfs(i, j)
        if cnt:
            res.append(cnt)
            area = 0

res.sort()
print(len(res))
for r in res:
    print(r, end=' ')

import sys
from collections import deque
input = sys.stdin.readline

xydir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M, T = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
q = deque()
visited = [[0]*M for _ in range(N)]


def bfs():
    gram = 10001
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if [x, y] == [N-1, M-1]:
            return min(visited[x][y]-1, gram)
        if _map[x][y] == 2:
            gram = visited[x][y]-1 + N-1-x + M-1-y

        for i, j in xydir:
            nx, ny = x+i, y+j
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if _map[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return gram


res = bfs()
print('Fail' if res > T else res)

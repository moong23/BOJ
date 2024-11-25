import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ice = []
for _ in range(N):
    ice.append(list(map(int, input().split())))

temp = [[0 for _ in range(M)] for _ in range(N)]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def melt(x, y):
    for dx, dy in dir:
        nx, ny = dx + x, dy + y
        if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] == 0:
            temp[x][y] += 1

def bfs(start_x, start_y, visited):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ice[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_iceberg():
    visited = [[False] * M for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0 and not visited[i][j]:
                count += 1
                bfs(i, j, visited)
    return count

def simulate():
    year = 0

    while True:

        for i in range(N):
            for j in range(M):
                if ice[i][j] > 0:
                    melt(i, j)


        for i in range(N):
            for j in range(M):
                ice[i][j] -= temp[i][j]
                if ice[i][j] < 0:
                    ice[i][j] = 0
                temp[i][j] = 0

        year += 1

        iceberg_count = count_iceberg()
        if iceberg_count == 0:
            return 0
        if iceberg_count > 1:
            return year

print(simulate())

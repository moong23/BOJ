from sys import stdin
from collections import deque

input = stdin.readline

R, C = map(int, input().split())
graph = []

posJ = []
posF = []

for i in range(R):
    row = list(input().strip())
    for j in range(C):
        if row[j] == "J":
            posJ.append((i, j))
        elif row[j] == "F":
            posF.append((i, j))
    graph.append(row)

q = deque()
q.append((posJ[0][0], posJ[0][1], "J"))
graph[posJ[0][0]][posJ[0][1]] = 0

for r, c in posF:
    q.append((r, c, "F"))
    graph[r][c] = "#"

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, case = q.popleft()

        if case == "J" and (x == 0 or y == 0 or x == R - 1 or y == C - 1):
            if graph[x][y] == "#":
                continue
            return graph[x][y] + 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != "#" and case == "F":
                    graph[nx][ny] = "#"
                    q.append((nx, ny, "F"))
                elif graph[nx][ny] == "." and case == "J" and graph[x][y] != "#":
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny, "J"))

    return "IMPOSSIBLE"

print(bfs())

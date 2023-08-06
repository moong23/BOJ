import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
graph[r - 1][0] = 1

result = 0


def dfs(x, y):
    global result
    if x == 0 and y == c - 1:
        if graph[x][y] == k:
            result += 1
            return
        else:
            return
    for i in move:
        nx = x + i[0]
        ny = y + i[1]
        if nx >= 0 and ny >= 0 and nx < r and ny < c:
            if graph[nx][ny] == '.':
                graph[nx][ny] = graph[x][y] + 1
                dfs(nx, ny)
                graph[nx][ny] = '.'


dfs(r - 1, 0)
print(result)

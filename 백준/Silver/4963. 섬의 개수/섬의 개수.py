import sys

sys.setrecursionlimit(10000)

def dfs(x, y):
    land[x][y] = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i
            ny = y + j
            if 0 <= nx < B and 0 <= ny < A and land[nx][ny] == 1:
                dfs(nx, ny)


while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        exit(0)

    land = []
    count = 0
    for _ in range(B):
        land.append(list(map(int, input().split())))

    for i in range(B):
        for j in range(A):
            if land[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
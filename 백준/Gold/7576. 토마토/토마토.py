import sys
from collections import deque
input = sys.stdin.readline

xydir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

M, N = map(int, input().split())
inArr = [list(map(int, input().split())) for _ in range(N)]

tomato = deque()
for i in range(N):
    for j in range(M):
        if inArr[i][j] == 1:
            tomato.append([i, j])


def bfs():
    while tomato:
        x, y = tomato.popleft()
        for i, j in xydir:
            if 0 <= x+i < N and 0 <= y+j < M and inArr[x+i][y+j] == 0:
                inArr[x+i][y+j] = inArr[x][y] + 1
                tomato.append([x+i, y+j])


bfs()
res = 0

for line in inArr:
    if line.count(0) > 0:
        print(-1)
        exit(0)

print(max(map(max, inArr))-1)

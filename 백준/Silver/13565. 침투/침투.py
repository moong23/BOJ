import sys
sys.setrecursionlimit(10**9)

dir = [[-1, 0],[0,1],[1,0],[0,-1]]

def dfs(x,y):
    board[x][y] = 2
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
            dfs(nx, ny)

M, N = map(int, input().split())

board = []
for _ in range(M):
    board.append(list(map(int, list(input()))))

for i in range(N):
    if board[0][i] == 0:
        dfs(0, i)

if 2 in board[-1]:
    print('YES')
else:
    print('NO')
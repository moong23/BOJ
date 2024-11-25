from collections import deque

dir = [[-1,0],[0,1],[1,0],[0,-1]]
ndir = [[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

K = int(input())
W, H = map(int, input().split())

board = []
for _ in range(H):
    board.append(list(map(int, input().split())))

def bfs():
    queue = deque([(0, 0, 0, K)])
    visited = [[set() for _ in range(W)] for _ in range(H)]
    visited[0][0].add(K)

    while queue:
        x, y, cnt, kcnt = queue.popleft()

        if x == H-1 and y == W-1:
            return cnt

        targetdir = dir if kcnt == 0 else dir + ndir
        # print(x, y, cnt, kcnt, targetdir)
        for dx, dy in targetdir:
            nx, ny = x + dx, y + dy

            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
                nkcnt = kcnt - 1 if [dx, dy] in ndir else kcnt
                if nkcnt not in visited[nx][ny]:
                    visited[nx][ny].add(nkcnt)
                    queue.append((nx, ny, cnt + 1, nkcnt))

    return -1

print(bfs())

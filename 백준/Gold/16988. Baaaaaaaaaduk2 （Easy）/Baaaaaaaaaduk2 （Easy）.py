from collections import deque

D = [[-1, 0], [0, 1], [1, 0], [0, -1]]
total = 0
N, M = 0, 0
map_ = []

def dfs(r, dep):
    global total
    if dep == 2:
        count()
        return
    for i in range(r, N):
        for j in range(M):
            if map_[i][j] == 0:
                map_[i][j] = 1
                dfs(i, dep + 1)
                map_[i][j] = 0

def count():
    global total
    visit = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_[i][j] == 2 and not visit[i][j]:
                cnt += bfs(visit, i, j)
    total = max(total, cnt)

def bfs(visit, r, c):
    q = deque([(r, c)])
    visit[r][c] = True
    find_zero = False
    cnt = 1

    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in D:
            nr, nc = cur_r + dr, cur_c + dc
            if not check(nr, nc) and not visit[nr][nc] and map_[nr][nc] != 1:
                if map_[nr][nc] == 0:
                    find_zero = True
                    continue
                visit[nr][nc] = True
                q.append((nr, nc))
                cnt += 1
    if find_zero:
        return 0
    return cnt

def check(a, b):
    return a < 0 or a >= N or b < 0 or b >= M


N, M = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(N)]

dfs(0, 0)

print(total)

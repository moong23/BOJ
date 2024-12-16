import heapq

N = 0
map_ = []
shark = 2
remain = 2
cY, cX = 0, 0

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(cy, cx):
    q = []
    heapq.heappush(q, (0, cy, cx))
    visited = [[False] * N for _ in range(N)]
    visited[cy][cx] = True

    while q:
        dist, y, x = heapq.heappop(q)

        if map_[y][x] > 0 and map_[y][x] < shark:
            map_[y][x] = 0
            global cY, cX
            cY, cX = y, x
            return dist

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and map_[ny][nx] <= shark:
                visited[ny][nx] = True
                heapq.heappush(q, (dist + 1, ny, nx))

    return -1

N = int(input())
map_ = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if map_[i][j] == 9:
            cY, cX = i, j
            map_[i][j] = 0

ans = 0
while True:
    ret = bfs(cY, cX)
    if ret == -1:
        break
    ans += ret
    remain -= 1
    if remain == 0:
        shark += 1
        remain = shark

print(ans)

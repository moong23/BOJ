import heapq
import math

INF = math.inf
dirX = [0, 0, -1, 1]
dirY = [-1, 1, 0, 0]

N = 0
map_ = []
visit = []
size = []

def bfs(x, y, roopy):
    visit[x][y] = True
    pq = []
    heapq.heappush(pq, (roopy, x, y))
    size[x][y] = roopy

    while pq:
        current_size, cx, cy = heapq.heappop(pq)

        for i in range(4):
            nowX = cx + dirX[i]
            nowY = cy + dirY[i]

            if range_check(nowX, nowY) and not visit[nowX][nowY] and size[nowX][nowY] > (map_[nowX][nowY] + current_size):
                size[nowX][nowY] = map_[nowX][nowY] + current_size
                visit[nowX][nowY] = True
                heapq.heappush(pq, (size[nowX][nowY], nowX, nowY))

def range_check(x, y):
    return 0 <= x < N and 0 <= y < N

count = 1
while True:
    N = int(input())
    if N == 0:
        break

    map_ = []
    visit = [[False] * N for _ in range(N)]
    size = [[INF] * N for _ in range(N)]

    for i in range(N):
        map_.append(list(map(int, input().split())))

    bfs(0, 0, map_[0][0])
    print(f"Problem {count}: {size[N-1][N-1]}")
    count += 1

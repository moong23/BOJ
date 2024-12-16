dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
map_ = [[False] * 101 for _ in range(101)]
ans = 0

def dragon_curve(x, y, d, g):
    tmp = [d]

    for i in range(1, g + 1):
        for j in range(len(tmp) - 1, -1, -1):
            tmp.append((tmp[j] + 1) % 4)

    map_[y][x] = True
    for dir in tmp:
        x += dx[dir]
        y += dy[dir]
        map_[y][x] = True

N = int(input())

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve(x, y, d, g)

for i in range(100):
    for j in range(100):
        if map_[i][j] and map_[i][j + 1] and map_[i + 1][j] and map_[i + 1][j + 1]:
            ans += 1

print(ans)

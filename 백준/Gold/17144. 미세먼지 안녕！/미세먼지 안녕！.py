import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
air = [[None for _ in range(C)] for _ in range(R)]
purifier = 0
target = []
xydir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        air[i][j] = tmp[j]
        if tmp[j] == -1:
            purifier = i

# print(air, purifier)


def spread():
    while target:
        x, y, val = target.pop()
        cnt = 0
        for dx, dy in xydir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if air[nx][ny] == -1:
                continue
            air[nx][ny] += val//5
            cnt += val//5
        air[x][y] -= cnt


def innerCirclulate(pur, dir):
    x, y = pur, 1
    tmp = 0
    idx = 1
    while True:
        nx = x + xydir[idx][0]
        ny = y + xydir[idx][1]
        if nx == R or ny == C or nx == -1 or ny == -1:
            idx = (idx-1) % 4 if dir == 0 else (idx+1) % 4
            continue
        if air[x][y] == -1:
            break
        air[x][y], tmp = tmp, air[x][y]
        x, y = nx, ny


def circulate():
    innerCirclulate(purifier-1, 0)
    innerCirclulate(purifier, 1)


for i, line in enumerate(air):
    for j, value in enumerate(line):
        if value > 0:
            target.append((i, j, value))

for t in range(T):
    spread()
    circulate()
    for i, line in enumerate(air):
        for j, value in enumerate(line):
            if value > 0:
                target.append((i, j, value))

print(sum(target[i][2] for i in range(len(target))))

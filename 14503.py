# https://www.acmicpc.net/problem/14503


def curr_clean(a, b):
    global cnt
    if root[a][b] == 0:
        cnt += 1
        root[a][b] = 2


def check_around(a, b):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        if a+dx[i] < 0 or a+dx[i] >= N or b + dy[i] < 0 or b + dy[i] >= M:
            pass
        else:
            # print(a+dx[i], b+dy[i])
            if root[a+dx[i]][b+dy[i]] == 0:
                return True

    else:
        return False


def check_front(a, b, d):
    if d == 0:  # North
        if a - 1 < 0 or root[a-1][b] != 0:
            return a, b, d
        else:
            return a-1, b, d
    elif d == 1:  # East
        if b + 1 >= M or root[a][b+1] != 0:
            return a, b, d
        else:
            return a, b+1, d
    elif d == 2:  # South
        if a + 1 >= N or root[a+1][b] != 0:
            return a, b, d
        else:
            return a+1, b, d
    elif d == 3:  # West
        if b - 1 < 0 or root[a][b-1] != 0:
            return a, b, d
        else:
            return a, b-1, d


def can_back(a, b, d):
    if d == 2:
        if root[a-1][b] == 1:
            return False
    elif d == 3:
        if root[a][b+1] == 1:
            return False
    elif d == 0:
        if root[a+1][b] == 1:
            return False
    else:
        if root[a][b-1] == 1:
            return False
    return True


def go_back(a, b, d):
    if d == 2:
        return a-1, b, d
    elif d == 3:
        return a, b+1, d
    elif d == 0:
        return a+1, b, d
    else:
        return a, b-1, d


N, M = map(int, input().split())
r, c, d = map(int, input().split())
cnt = 0
root = []

for _ in range(N):
    root.append(list(map(int, input().split())))


while (1):
    curr_clean(r, c)
    if check_around(r, c):  # 빈 칸 있는 경우
        d = (d+3) % 4
        r, c, d = check_front(r, c, d)
        # print(r, c, d)
    else:
        if can_back(r, c, d):
            r, c, d = go_back(r, c, d)
        else:
            print(cnt)
            break

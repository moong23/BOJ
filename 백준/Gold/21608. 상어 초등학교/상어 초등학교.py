import sys
input = sys.stdin.readline

N = int(input())
chair = [[0 for _ in range(N)] for _ in range(N)]
xydir = [[0, -1], [1, 0], [0, 1], [-1, 0]]
chairMemo = {}


def Step_1(user, favorite):
    _max = -1
    _maxL = []
    for i in range(N):
        for j in range(N):
            if chair[i][j] != 0:
                continue
            favCnt = 0
            for dx, dy in xydir:
                if 0 <= i+dx < N and 0 <= j+dy < N:
                    if chair[i+dx][j+dy] in favorite:
                        favCnt += 1
                else:
                    pass
            if _max < favCnt:
                _max = favCnt
                _maxL = [[i, j]]
            elif _max == favCnt:
                _maxL.append([i, j])
    if (len(_maxL) == 1):
        chair[_maxL[0][0]][_maxL[0][1]] = user
        chairMemo[user] = [_maxL[0][0], _maxL[0][1]]
    else:
        Step_2(user, _maxL)


def Step_2(user, cand):
    _max = -1
    _maxL = []
    for i, j in cand:
        emptyCnt = 0
        for dx, dy in xydir:
            if 0 <= i+dx < N and 0 <= j+dy < N:
                if chair[i+dx][j+dy] == 0:
                    emptyCnt += 1
            else:
                continue
        if _max < emptyCnt:
            _max = emptyCnt
            _maxL = [[i, j]]
        elif _max == emptyCnt:
            _maxL.append([i, j])
    if (len(_maxL) == 1):
        chair[_maxL[0][0]][_maxL[0][1]] = user
        chairMemo[user] = [_maxL[0][0], _maxL[0][1]]
    else:
        Step_3(user, _maxL)


def Step_3(user, cand):
    cand.sort()
    chair[cand[0][0]][cand[0][1]] = user
    chairMemo[user] = [cand[0][0], cand[0][1]]


user = {}
for _ in range(N*N):
    inLine = list(map(int, input().split()))
    Step_1(inLine[0], inLine[1:])
    user[inLine[0]] = inLine[1:]

# print(chair)
# print(user)
# print(chairMemo)
res = 0
for u in user:
    cnt = 0
    for dx, dy in xydir:
        i, j = chairMemo[u]
        if 0 <= i+dx < N and 0 <= j+dy < N:
            if chair[i+dx][j+dy] in user[u]:
                cnt += 1
    if cnt == 0:
        continue
    else:
        res += pow(10, cnt-1)
print(res)

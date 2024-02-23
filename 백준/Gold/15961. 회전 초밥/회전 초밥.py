import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().split())

sushi = []
for _ in range(N):
    sushi.append(int(sys.stdin.readline()))
current = defaultdict(int)


# print(current)
_max = -1
_cnt = 0
for i in range(k):
    if current[sushi[i]] == 0:
        current[sushi[i]] = 1
        _cnt += 1
    else:
        current[sushi[i]] += 1

start = 0
# for x, y in current.items():
#     if y != 0:
#         print(str(x) + ':', y, end=', ')
# print()
# print(_cnt)
if current[c] == 0:
    _max = _cnt
else:
    _max = _cnt - 1

while (start < N):
    # print('---')
    # print(sushi[start], sushi[(start+k) % N], c)

    if current[sushi[start]] == 1:
        current[sushi[start]] -= 1
        _cnt -= 1
    else:
        current[sushi[start]] -= 1
    if current[sushi[(start+k) % N]] == 0:
        current[sushi[(start+k) % N]] = 1
        _cnt += 1
    else:
        current[sushi[(start+k) % N]] += 1
    if current[c] >= 1:
        _cnt -= 1
    _max = max(_max, _cnt)
    # for x, y in current.items():
    #     if y != 0:
    #         print(str(x) + ':', y, end=', ')
    # print()
    # print(_cnt)
    if current[c] >= 1:
        _cnt += 1
    start += 1

print(_max+1)

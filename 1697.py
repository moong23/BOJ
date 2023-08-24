# https://www.acmicpc.net/problem/1697

from collections import deque

init, target = map(int, input().split())

test = deque()
test.append(init)
dist = [0] * 1000001

while test:
    x = test.popleft()
    if x == target:
        print(dist[x])
        break
    for tg in (x-1, x+1, 2*x):
        if 0 <= tg <= 1000000 and not dist[tg]:
            dist[tg] = dist[x] + 1
            test.append(tg)

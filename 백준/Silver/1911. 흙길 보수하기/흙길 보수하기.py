import sys
import math
input = sys.stdin.readline

N, L = map(int, input().split())

water = []
for _ in range(N):
    water.append(list(map(int, input().split())))
water.sort(key=lambda x: x[0])

pCount = 0
maxidx = 0

for s, e in water:
    if s <= maxidx:
        s = maxidx+1

        if e <= s:
            continue

    cnt = math.ceil((e-s)/L)
    pCount += cnt
    maxidx = max(maxidx, s + cnt*L-1)

print(pCount)
import sys

input = sys.stdin.readline

MAX_NUM = 1000000
Prime = [1 for _ in range(MAX_NUM+1)]
Prime[0], Prime[1] = 0, 0

N = int(input())

numList = set(map(int, input().split()))

for i in range(2, 1001):
    k = 2
    while i*k <= MAX_NUM:
        Prime[i*k] = 0
        k += 1

res = 1
for x in numList:
    res *= x if Prime[x] == 1 else 1
else:
    print(res if res > 1 else -1)

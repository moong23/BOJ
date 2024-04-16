import sys

input = sys.stdin.readline

N, M = map(int, input().split())

checkArr = {}

for _ in range(N):
    checkArr[input()] = 1

cnt = 0
for _ in range(M):
    if input() in checkArr:
        cnt += 1
else:
    print(cnt)

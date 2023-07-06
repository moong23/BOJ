# https://www.acmicpc.net/problem/2217

N = int(input())
ropeList = []
for _ in range(N):
    ropeList.append(int(input()))
# 내림차순 정렬
ropeList.sort(reverse=True)

weight = 0
for idx, rope in enumerate(ropeList):
    if (weight < (idx+1) * rope):
        weight = (idx+1) * rope

print(weight)
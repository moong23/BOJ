import sys
input = sys.stdin.readline

N, C = map(int, input().split())

coord = []
for _ in range(N):
    coord.append(int(input()))
coord.sort()


start, end = 1, coord[-1] - coord[0]
res = 0
while start <= end:
    mid = (start + end)//2
    cur = coord[0]
    cnt = 1
    for i in range(1, N):
        if coord[i] >= cur + mid:
            cnt += 1
            cur = coord[i]
    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)

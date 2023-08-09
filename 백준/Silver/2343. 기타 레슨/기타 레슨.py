import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lesson = list(map(int, input().split()))

left = max(lesson)
right = sum(lesson)
ans = 10**9
while left <= right:
    mid = (left+right)//2
    cnt = 0
    sum = 0
    for i in range(len(lesson)):
        if sum+lesson[i] > mid:
            cnt += 1
            sum = 0
        sum += lesson[i]
    if sum:
        cnt += 1

    if cnt > m:
        left = mid+1
    else:
        ans = min(ans, mid)
        right = mid-1
print(ans)

n, m = map(int, input().split())

arr =[int(input())for _ in range(n)]

left, right = min(arr), sum(arr)
ans = 0
while left <= right:
    mid = (left + right) // 2
    money = mid
    cnt = 1

    for i in arr:
        if money < i:
            money = mid
            cnt += 1
        money -= i
    
    if cnt > m or mid < max(arr):
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
print(ans)
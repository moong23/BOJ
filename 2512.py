N = int(input())
cities = list(map(int, input().split()))
money = int(input())
start, end = 0, max(cities)

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in cities:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= money:
        start = mid + 1
    else:
        end = mid - 1
print(end)

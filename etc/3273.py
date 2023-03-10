num = int(input())
arr = list(map(int, input().split()))
val = int(input())

cnt = 0

arr.sort()

start, end = 0, len(arr)-1

while start != end:
    tmp = arr[start] + arr[end]
    if tmp == val:
        start += 1
        cnt += 1
    elif tmp > val:
        end -= 1
    else:
        start += 1
print(cnt)

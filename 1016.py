start, end = map(int, input().split())

arr = [1] * (end+1)
arr[0], arr[1] = 0, 0
print(arr)

for i in range(int(pow(end, 1/2))+1):
    if arr[i] == 1:
        for j in range(i+i, end+1, i):
            arr[j] = 0
print(arr)

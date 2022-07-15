num = list(input())
arr = []
for i in num:
    arr.append(int(i))
arr.sort(reverse=True)
for i in range(len(arr)):
    print(arr[i], end='')

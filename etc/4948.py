n = 2 * 123456
arr = [1]*(n+1)
m = int(n ** 0.5)

for i in range(2, m+1):
    if arr[i] == 1:
        for j in range(i+i, n+1, i):
            arr[j] = 0
arr[0] = 0
arr[1] = 0

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if arr[i] == 1:
            cnt += 1
    print(cnt)

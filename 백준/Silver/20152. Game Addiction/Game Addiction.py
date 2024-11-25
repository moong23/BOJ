N, K = map(int, input().split())

target = abs(N - K) + 1

arr = [[0 for _ in range(target)] for i in range(target)]

for i in range(target):
    arr[0][i] = 1


for i in range(1, target):
    for j in range(i, target):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

print(arr[-1][-1])
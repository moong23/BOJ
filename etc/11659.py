import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for x in map(int, sys.stdin.readline().split()):
    if len(arr) == 0:
        arr.append(x)
    else:
        arr.append(arr[-1]+x)
arr.insert(0, 0)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(arr[b] - arr[a-1])
# print(arr)

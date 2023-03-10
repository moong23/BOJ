num = int(input())

arr = list()
for _ in range(num):
    a, b = input().split()
    a = int(a)
    arr.append([a, b])
arr.sort(key=lambda x: x[0])
for a, b in arr:
    print(a, b)

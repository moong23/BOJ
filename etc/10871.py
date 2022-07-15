a, b = map(int, input().split())

arr = input().split()
ans = []
for i in arr:
    if int(i) < b:
        ans.append(int(i))


for x in ans:
    print(x, end=' ')

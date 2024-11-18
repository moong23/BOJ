N = int(input())
inArr = list(map(int, input().split()))

a = 0
for i in sorted(inArr):
    if a+1 < i:
        break
    a += i

print(a+1)
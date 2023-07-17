# https://www.acmicpc.net/problem/11399

Num = int(input())

listP = list(map(int, input().split(' ')))

listP.sort(reverse=True)

sum = 0
for i, x in enumerate(listP):
    sum += (i+1) * x

print(sum)
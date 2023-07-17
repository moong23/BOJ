# https://www.acmicpc.net/problem/13305

Num = int(input())
dist = list(map(int, input().split(' ')))
oil = list(map(int, input().split()))

sum = 0
min_oil = 1000000001
for i in range(Num - 1):
    min_oil = min(oil[i], min_oil)
    sum += min_oil * dist[i]
print(sum)
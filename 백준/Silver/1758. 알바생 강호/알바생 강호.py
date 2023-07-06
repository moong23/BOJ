# https://www.acmicpc.net/problem/1758

Num = int(input())

tip = []
for _ in range(Num):
    tip.append(int(input()))

tip.sort(reverse=True)

sum = 0
for idx, x in enumerate(tip):
    sum += max(x - idx, 0)
print(sum)

# https://www.acmicpc.net/problem/11508

Num = int(input())

product = []

for _ in range(Num):
    product.append(int(input()))

product.sort(reverse=True)

sum = 0
for i, price in enumerate(product):
    if i % 3 == 2:
        continue
    sum += price
print(sum)
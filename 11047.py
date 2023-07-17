# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:
    if coin > K:
        pass
    while K >= coin:
        cnt += K // coin
        K = K % coin

print(cnt)
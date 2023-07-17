# https://www.acmicpc.net/problem/20365

N = int(input())

colors = list(input())

cnt = 1
for i in range(1,N):
    if colors[i] != colors[i-1]:
        cnt += 1
print(int(cnt/2 + 1))
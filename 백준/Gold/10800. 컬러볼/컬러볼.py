import sys

input = sys.stdin.readline

n = int(input())
_MAX = 200000
balls = []

for i in range(n):
    color, size = map(int, input().split())
    balls.append((size, color, i))

balls.sort()
color_count = [0] * (_MAX + 1)
total, j = 0, 0
ans = [0] * (n + 1)

for i in range(n):
    while balls[j][0] < balls[i][0]:
        color_count[balls[j][1]] += balls[j][0]
        total += balls[j][0]
        j += 1
    ans[balls[i][2]] = total - color_count[balls[i][1]]

for i in range(n):
    print(ans[i])

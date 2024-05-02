import sys
input = sys.stdin.readline

N, K = map(int, input().split())

left, right = 0, N // 2

while left <= right:
    tmp = (left + right) // 2
    _sum = (tmp + 1) * (N - tmp + 1)
    if K == _sum:
        print("YES")
        exit(0)
    if K > _sum:
        left = tmp + 1
    else:
        right = tmp - 1

print("NO")

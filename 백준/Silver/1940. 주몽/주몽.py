import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
number = list(map(int, input().split()))

number.sort()
start, end = 0, N-1
count = 0

while start < end:
    target = number[start] + number[end]
    if target < M:
        start += 1
    elif target > M:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)

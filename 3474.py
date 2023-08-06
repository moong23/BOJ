# https://www.acmicpc.net/problem/3474
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input())
    cnt = 0
    i = 5
    while i <= num:
        cnt += num // i
        i *= 5
    print(cnt)

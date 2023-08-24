# https://www.acmicpc.net/problem/1253
import sys
input = sys.stdin.readline


N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()


def isGood(idx, number):
    start, end = 0, N-1
    while start < end:
        if start == idx:
            start += 1
        elif end == idx:
            end -= 1
        elif number == numbers[start] + numbers[end]:
            return 1
        elif number < numbers[start] + numbers[end]:
            end -= 1
        else:
            start += 1
    return 0


cnt = 0
for idx, number in enumerate(numbers):
    if isGood(idx, number):
        cnt += 1
print(cnt)

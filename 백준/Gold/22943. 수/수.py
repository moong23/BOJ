import sys
from itertools import permutations
input = sys.stdin.readline

k, m = map(int, input().split())
primeNum = [True] * (10**k)

MAX_NUM = int((10**k)**0.5)
for i in range(2, MAX_NUM + 1):
    if primeNum[i]:
        for j in range(i+i, 10**k, i):
            primeNum[j] = False


cnt = 0
for num in permutations(range(10), k):
    if num[0] == 0:
        continue
    num = int(''.join(list(map(str, num))))
    temp = num
    while temp % m == 0:
        temp = temp//m
    for i in range(2, int(temp**0.5)+1):
        if temp % i == 0:
            if primeNum[i] and primeNum[temp//i]:
                for j in range(2, num//2):
                    if primeNum[j] and primeNum[num-j]:
                        cnt += 1
                        break
                break
            break


print(cnt)

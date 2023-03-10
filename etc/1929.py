

from math import sqrt


def isPrime(num):
    for i in range(2, sqrt(num)+1):
        if num % i == 0:
            return 0
    else:
        return 1


a, b = map(int, input().split())

for i in range(a, b+1):
    if isPrime(i) == 1:
        print(i)

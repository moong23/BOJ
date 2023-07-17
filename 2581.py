from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


a = int(input())
b = int(input())

arr = list()
for i in range(a, b+1):
    if is_prime(i):
        arr.append(i)
if len(arr) >= 1:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)

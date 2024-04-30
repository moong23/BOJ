import sys
input = sys.stdin.readline


N = int(input())


def check(A):
    _len = len(A)
    if _len == 1:
        return True

    for i in range(_len//2):
        if A[i] == A[_len - 1 - i]:
            return False
    else:
        return check(A[0:_len//2]) and check(A[_len//2 + 1:])


for _ in range(N):
    inStr = list(map(int, input().rstrip()))

    print("YES" if check(inStr) else "NO")

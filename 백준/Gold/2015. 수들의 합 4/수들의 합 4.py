import sys
input = sys.stdin.readline

N, K = map(int, input().split())
inArr = list(map(int, input().split()))

S = {0: 1}

_sum = 0
answer = 0

for i in inArr:
    _sum += i

    if _sum - K in S.keys():
        answer += S[_sum - K]

    S[_sum] = S.get(_sum, 0) + 1

print(answer)

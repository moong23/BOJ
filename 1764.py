import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A, B = set(), set()

for _ in range(N):
    A.add(input().rstrip())

for _ in range(M):
    B.add(input().rstrip())

res = sorted(list(A & B))
print(len(res))
for x in res:
    print(x)

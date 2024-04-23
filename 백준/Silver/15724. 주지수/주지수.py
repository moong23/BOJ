import sys
input = sys.stdin.readline

N, M = map(int, input().split())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

sumP = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        sumP[i+1][j+1] = sumP[i+1][j] + people[i][j]

# print(*sumP)

for i in range(N):
    for j in range(M):
        sumP[i+1][j+1] += sumP[i][j+1]

# print(*sumP)

num = int(input())
for _ in range(num):
    A, B, C, D = map(int, input().split())
    print(sumP[C][D] - sumP[C][B-1] - sumP[A-1][D] + sumP[A-1][B-1])

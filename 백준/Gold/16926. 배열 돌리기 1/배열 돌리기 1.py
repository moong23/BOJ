from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

matrix = []
A = [[0]*M for _ in range(N)]
tmp = deque()

for i in range(N):
    matrix.append(list(input().split()))

loops = min(N, M) // 2
for i in range(loops):
    tmp.clear()
    tmp.extend(matrix[i][i:M-i])
    tmp.extend([row[M-i-1] for row in matrix[i+1:N-i-1]])
    tmp.extend(matrix[N-i-1][i:M-i][::-1])
    tmp.extend([row[i] for row in matrix[i+1:N-i-1]][::-1])

    tmp.rotate(-R)

    for j in range(i, M-i):
        A[i][j] = tmp.popleft()
    for j in range(i+1, N-i-1):
        A[j][M-i-1] = tmp.popleft()
    for j in range(M-i-1, i-1, -1):
        A[N-i-1][j] = tmp.popleft()
    for j in range(N-i-2, i, -1):
        A[j][i] = tmp.popleft()

for line in A:
    print(" ".join(line))

from collections import deque
import sys
input = sys.stdin.readline


def dfs(s):
    queue = deque()
    queue.append(s)
    cnt = 0
    while queue:
        start = queue.popleft()
        for i in range(len(graph[start])):
            if graph[start][i] != 0 and visited[start][i] == 0:
                queue.append(graph[start][i])
                visited[start][i] = 1
                cnt += 1
                break
            if visited[start][i] == 1:
                return -1
    return cnt


N, M, P = map(int, input().split())

graph = [[] for _ in range(M + 1)]
visited = [[] for _ in range(M + 1)]

for i in range(N):
    A, B = map(int, input().split())
    graph[B].append(A)
    visited[B].append(0)

print(dfs(P))

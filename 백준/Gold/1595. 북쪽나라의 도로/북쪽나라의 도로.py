graph = [[] for _ in range(10001)]


def dfs(node):
    visited[node] = True
    for i, j in graph[node]:
        if not visited[i]:
            distance[i] += distance[node] + j
            dfs(i)


while True:
    try:
        A, B, N = map(int, input().split())
        graph[A].append((B, N))
        graph[B].append((A, N))
    except:
        break

visited = [False] * 10001
visited[1] = True
distance = [0] * 10001

dfs(1)

furthest = distance.index(max(distance))

visited = [False] * 10001
visited[furthest] = True
distance = [0] * 10001

dfs(furthest)
print(max(distance))

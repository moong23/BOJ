import sys
input = sys.stdin.readline

MAX_INT = float('inf')

def bf(n, m, edges):
    dist = [MAX_INT] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        for edge in edges:
            a, b, w = edge
            if dist[a] != MAX_INT and dist[b] > dist[a] + w:
                dist[b] = dist[a] + w

    for edge in edges:
        a, b, w = edge
        if dist[a] != MAX_INT and dist[b] > dist[a] + w:
            return -1

    return dist

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

res = bf(n, m, edges)
if res == -1:
    print(-1)
else:
    for d in res[2:]:
        print(d if d != MAX_INT else -1)

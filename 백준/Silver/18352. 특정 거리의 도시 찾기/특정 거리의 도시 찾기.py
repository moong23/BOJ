import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

Node = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    Node[start].append(end)

dist = [sys.maxsize for _ in range(N+1)]


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        d, target = heapq.heappop(q)
        if dist[target] < d:
            continue
        for i in Node[target]:
            cost = 1 + d
            if cost < dist[i]:
                dist[i] = cost
                heapq.heappush(q, (cost, i))


dijkstra(X)

flag = False
for i in range(1, N+1):
    if dist[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)

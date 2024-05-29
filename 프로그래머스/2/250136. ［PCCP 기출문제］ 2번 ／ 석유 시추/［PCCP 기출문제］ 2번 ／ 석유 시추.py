from collections import deque

xydir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(land, i, j, visited, areaID):
    N, M = len(land), len(land[0])
    queue = deque([(i, j)])
    visited[i][j] = areaID
    areas = set()
    size = 0

    while queue:
        cx, cy = queue.popleft()
        size += 1
        areas.add(cy)
        for dx, dy in xydir:
            nx, ny = cx + dx, cy + dy
            if (0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1 and visited[nx][ny] == -1):
                visited[nx][ny] = areaID
                queue.append((nx, ny))

    return size, areas


def solution(land):
    N, M = len(land), len(land[0])

    visited = [[-1] * M for _ in range(N)]

    area = {}

    areaID = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and visited[i][j] == -1:
                area[areaID] = (bfs(land, i, j, visited, areaID))
                areaID += 1

    oils = [0] * M
    for areaID, (size, areas) in area.items():
        for a in areas:
            oils[a] += size

    return max(oils)
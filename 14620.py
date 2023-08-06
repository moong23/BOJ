N = int(input())
flower_inList = [list(map(int, input().split())) for _ in range(N)]

ans = 10000


def check(flower_list):
    cost = 0
    flower_occupied = []

    for order in flower_list:
        x, y = order // N, order % N

        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000

        for w in range(5):
            flower_occupied.append(
                (x+[0, 0, 1, 0, -1][w], y+[0, 1, 0, -1, 0][w]))
            cost += flower_inList[x+[0, 0, 1, 0, -1][w]][y+[0, 1, 0, -1, 0][w]]

    if len(set(flower_occupied)) != 15:
        return 10000

    return cost


for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            ans = min(ans, check([i, j, k]))

print(ans)

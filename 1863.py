N = int(input())

building = []
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    while len(building) > 0 and building[-1] > y:
        cnt += 1
        building.pop()
    if len(building) > 0 and building[-1] == y:
        continue
    building.append(y)

for b in building[::-1]:
    if b > 0:
        cnt += 1


print(cnt)

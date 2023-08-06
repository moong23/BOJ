from itertools import combinations

N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]
members = list(range(N))
min_value = 9999999

for possible in combinations(members, N//2):
    start, link = 0, 0
    compact = list(set(members) - set(possible))

    for x in combinations(possible, 2):
        start += power[x[0]][x[1]]
        start += power[x[1]][x[0]]

    for x in combinations(compact, 2):
        link += power[x[0]][x[1]]
        link += power[x[1]][x[0]]

    min_value = min(min_value, abs(start-link))

print(min_value)

import sys

from itertools import combinations
n, m = map(int, sys.stdin.readline().split())  # 5,3

ice = [[False]*n for _ in range(n)]
print(ice)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True
print(ice)
ans = 0

print(list(combinations(range(n), 3)))
for comb in combinations(range(n), 3):
    if ice[comb[0]][comb[1]] or ice[comb[1]][comb[2]] or ice[comb[0]][comb[2]]:
        continue
    ans += 1

print(ans)


# import sys
# from itertools import combinations


# n, m = map(int, input().split())
# noscream = []  # [(1, 2), (3, 4), (1, 3)]
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     noscream.append((a, b))


# icecream = []  # [1,2,3,4,5]
# for i in range(1, n+1):
#     icecream.append(i)


# c = list(combinations(icecream, 3))  # [(1,2,3), (1,2,4),...]

# remove_ice = []

# for x, y in noscream:
#     for indiv_ice in c:
#         if x in indiv_ice and y in indiv_ice:
#             remove_ice.append(indiv_ice)

# for x in remove_ice:
#     try:
#         c.remove(x)
#     except:
#         continue
# print(len(c))

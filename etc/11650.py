# import sys
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     so.append(list(map(int, sys.stdin.readline().split())))

# so.sort(key=lambda x: (x[0], x[1]))
# for i in so:
#     print(i[0], i[1])

import sys
n = int(sys.stdin.readline())

so = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    so.append([a, b])
so.sort()

# print(so)
for i in range(n):
    print(so[i][0], so[i][1])

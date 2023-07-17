def bs (rank, point):
    start, end = 0, len(rank)-1
    res = 0
    while start <= end:
        mid = (start + end)//2
        if int(rank[mid][1]) >= point:
            end = mid - 1
            res = mid
        else:
            start = mid ++ 1
    return res

import sys
n, m = map(int, sys.stdin.readline().split())
rank = [sys.stdin.readline().split() for _ in range(n)]


for i in range(m):
    point = int(sys.stdin.readline())
    print(rank[bs(rank,point)][0])
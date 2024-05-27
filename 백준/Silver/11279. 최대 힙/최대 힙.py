import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []
heapq.heapify(arr)

for _ in range(N):
    cmd = int(input())
    # print(cmd, arr)
    if cmd == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (-cmd, cmd))

# https://www.acmicpc.net/problem/11000

import sys
import heapq

time_list = []
input = sys.stdin.readline
N = int(input())
in_list = []

for i in range(N):
    start, end = map(int, input().split())
    in_list.append([start, end])
in_list.sort(key=lambda x: x[0])

heapq.heappush(time_list, in_list[0][1])  #첫번째 강의가 끝나는 시간을 넣음

for i in range(1, N):
    if time_list[0] > in_list[i][0]: # add one more
        heapq.heappush(time_list, in_list[i][1])
    else: #update fin time
        heapq.heappop(time_list)
        heapq.heappush(time_list, in_list[i][1])
print(len(time_list))
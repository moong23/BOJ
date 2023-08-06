import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    result = 0
    while len(arr) >= 2:
        num1 = heapq.heappop(arr)
        num2 = heapq.heappop(arr)
        result += (num1 + num2)
        heapq.heappush(arr, (num1 + num2))
    print(result)

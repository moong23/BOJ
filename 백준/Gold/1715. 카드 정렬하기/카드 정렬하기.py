import sys
import heapq

input = sys.stdin.readline

N = int(input())

cards = []
for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards)


sum = 0
while 1:
    try:
        a, b = heapq.heappop(cards), heapq.heappop(cards)
        sum += a + b
        heapq.heappush(cards, a+b)
    except:
        print(sum)
        break

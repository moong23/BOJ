import sys
from collections import deque

input = sys.stdin.readline

totalMin = int(input())

currentQueue = deque()
totalScore = 0
cnt = 0
for _ in range(totalMin):
    tf = 0
    try:
        tf, score, time = map(int, input().split())
        currentQueue.append([time, score])
        cnt += 1
    except:
        pass
    if cnt > 0:
        currentQueue[cnt-1][0] -= 1
        if currentQueue[cnt-1][0] == 0:
            totalScore += currentQueue.pop()[1]
            cnt -= 1
else:
    print(totalScore)

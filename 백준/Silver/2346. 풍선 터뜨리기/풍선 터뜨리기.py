from collections import deque

N = int(input())
arr = deque(enumerate(map(int, input().split())))
answer = []

while arr:
    idx, item = arr.popleft()
    answer.append(idx+1)

    if item > 0:
        arr.rotate(-item + 1)
    else:
        arr.rotate(-item)

print(' '.join(map(str, answer)))

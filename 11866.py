from collections import deque

K, N = map(int, input().split())

queue = deque([i+1 for i in range(K)])
res = []
cnt = 0


while len(queue) != 0:
    cnt += 1
    if cnt == N:
        res.append(queue.popleft())
        cnt = 0
    else:
        queue.append(queue.popleft())
print('<', end='')
print(', '.join(map(str, res)), end='')
print('>')

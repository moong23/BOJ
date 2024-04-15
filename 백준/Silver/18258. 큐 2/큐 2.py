import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


dq = deque()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        dq.append(int(cmd[1]))
        continue
    if cmd[0] == 'pop':
        if (len(dq) > 0):
            print(dq.popleft())
        else:
            print(-1)
        continue
    if cmd[0] == 'size':
        print(len(dq))
        continue
    if cmd[0] == 'empty':
        print(0 if len(dq) > 0 else 1)
        continue
    if cmd[0] == 'front':
        len_d = len(dq)
        if (len_d > 0):
            print(dq[0])
        else:
            print(-1)
        continue
    if cmd[0] == 'back':
        len_d = len(dq)
        if (len_d > 0):
            print(dq[len_d-1])
        else:
            print(-1)

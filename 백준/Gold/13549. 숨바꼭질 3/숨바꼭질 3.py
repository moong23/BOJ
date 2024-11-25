from collections import deque

S, E = map(int, input().split())

if S == E:
    print(0)
    exit(0)

que = deque()
visited = set()
time = 0
if S == 0:
    S, time = 1, 1
    visited.update([0,1])
    
que.append((S, time))
visited.add(S)

while que:
    current, time = que.popleft()

    if current == E:
        break

    for nx in (2*current, current-1, current+1):
        if 0 <= nx <= 100000:
            if nx not in visited:
                visited.add(nx)
                if nx == 2 * current:
                    que.appendleft((nx, time))
                else:
                    que.append((nx, time+1))

print(time)
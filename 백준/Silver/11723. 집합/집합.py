import sys
input = sys.stdin.readline

M = int(input())

S = 0
for _ in range(M):
    cmd = list(input().split())
    if cmd[0] == 'add':
        S = S | (1 << int(cmd[1]))
    elif cmd[0] == 'remove':
        S = S & ~(1 << int(cmd[1]))
    elif cmd[0] == 'check':
        print(1) if (S & (1 << int(cmd[1]))) == (
            1 << int(cmd[1])) else print(0)
    elif cmd[0] == 'toggle':
        S = S ^ (1 << int(cmd[1]))
    elif cmd[0] == 'all':
        S = (1 << 21) - 1
    elif cmd[0] == 'empty':
        S = 0
    # print(S)

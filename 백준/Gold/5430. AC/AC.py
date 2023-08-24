import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    command = input().strip()
    N = int(input())
    numbers = deque(
        map(int, input().strip()[1:-1].split(','))) if N > 0 else deque(input().strip()[1:-1])
    # print(numbers)
    direction = 1  # 1 -> / 0 <-
    error_flag = False
    for cmd in command:
        if cmd == 'R':
            direction = 1 - direction
        elif cmd == 'D':
            if N > 0:
                N -= 1
                if direction == 1:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                print('error')
                error_flag = True
                break
    if not error_flag:
        if direction == 0:
            numbers.reverse()
        print('['+','.join(map(str, numbers))+']')

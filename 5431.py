from collections import deque

T = int(input())

while(T):
    T -= 1
    p = input()
    n = int(input())
    arr = deque()
    if n > 0:
        arr = deque(map(int, input()[1:-1].split(',')))
    # print(arr);
    direction = 0
    # 0 ->
    # 1 <-
    for x in p:
        if x == 'R':
            direction = 1 - direction
        elif x == 'D':
            try:
                if direction == 0:
                    arr.popleft()
                else:
                    arr.pop()
            except:
                print('error')
                break
    else:
        if direction == 1:
            print('['+','.join(list((arr)))+']')
        else:
            print('['+','.join(list(arr))+']')

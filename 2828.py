# https://www.acmicpc.net/problem/2828

N, M = map(int, input().split(' '))

num = int(input())
cur_pos = [1, M]
total = 0
for _ in range(num):
    apple = int(input()) 
    # 바구니보다 오른쪽에 떨어지면
    if apple > cur_pos[1]:
        tmp = apple - cur_pos[1]
        cur_pos[0] += tmp
        cur_pos[1] += tmp
        total += tmp
    # 바구니보다 왼쪽에 떨어지면
    elif apple < cur_pos[0]:
        tmp = cur_pos[0] - apple
        cur_pos[0] -= tmp
        cur_pos[1] -= tmp
        total += tmp
else:
    print(total)
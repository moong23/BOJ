# https://www.acmicpc.net/problem/2138

N = int(input())

init = list(map(int, input()))
target = list(map(int, input()))

# 첫번째 전구 바꾸는 경우와 안바꾸는 경우
def process(init):
    tmp = init[:]
    cnt = 0
    for i in range(0, N-1):
        if tmp[i] == target[i]:
            continue
        
        cnt += 1
        for idx in range(i, i+3):
            if idx < N:
                tmp[idx] = 1 - tmp[idx]
    if tmp == target:
        return cnt
    else:
        return pow(10,100)

res = process(init)
init[0], init[1] = 1- init[0], 1-init[1]
res = min(res, process(init)+1)

if res == pow(10,100):
    print(-1)
else:
    print(res)

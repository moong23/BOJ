# https://www.acmicpc.net/problem/19941

N, K = map(int, input().split(' '))

# 모든 사람이 가장 왼쪽부터 가능한 첫번째 햄버거를 집는다
burger = list(input())

cnt = 0

for i in range(N):
    if burger[i] == 'P':
        for j in range(-K,K+1):
            if i+j < 0:
                continue
            if i+j > N-1:
                break
            else:
                if burger[i+j] == 'H':
                    burger[i], burger[i+j] = '1', '0'
                    cnt += 1
                    break
    # print(burger,cnt)
print(cnt)
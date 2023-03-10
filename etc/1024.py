N = int(input())
L = int(input())

ans = []
for i in range(L, 101):
    if i % 2 == 0:  # i가 짝수
        if N % i == 0:  # N이 2의 배수이면 가망없음
            continue
        else:
            start = N // i
else:
    print(-1)

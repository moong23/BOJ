import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    L = list(map(int, input().split()))

    if M != N:
        for j in range(M - 1):
            L.append(L[j])

    start, end = 0, M - 1
    count = sum(L[:M])
    check = 0

    if count < K:
        check += 1

    while end < len(L) - 1:
        count -= L[start]
        start += 1
        end += 1
        count += L[end]
        
        if count < K:
            check += 1
    
    print(check)

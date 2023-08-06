N = int(input())
height = list(map(int, input().split()))
ans = [0] * N
for idx in range(1, N+1):
    t = height[idx-1]
    cnt = 0
    for i in range(N):
        if cnt == t and ans[i] == 0:
            ans[i] = idx
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)

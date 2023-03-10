N = int(input())
M = int(input())
ans = abs(100 - N)
broken = map(input().split())

for i in range(1000000):
    for x in str(i):
        if x in broken:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - N))

print(ans)
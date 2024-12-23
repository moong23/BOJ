h, w = map(int, input().split())
block = list(map(int, input().split()))

res = 0
for i in range(1, w - 1):
    l = 0
    r = 0

    for j in range(i):
        l = max(block[j], l)

    for j in range(i + 1, w):
        r = max(block[j], r)

    if block[i] < l and block[i] < r:
        res += min(l, r) - block[i]

print(res)

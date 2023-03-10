num = int(input())

cow = dict()
cnt = 0
for _ in range(num):
    x, y = map(int, input().split())
    if x in cow:
        if cow[x] != y:
            cow[x] = y
            cnt += 1
    else:
        cow[x] = y
    print(cow, cnt)
print(cnt)

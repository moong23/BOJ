N = int(input())
village = [[]for _ in range(N)]

po = 0
for i in range(N):
    X, A = map(int, input().split())
    village[i] = [X, A]
    po += A
tmp = 0
village.sort(key=lambda x: (x[0]))
for i in range(N):
    tmp += village[i][1]
    if tmp >= po/2:
        print(village[i][0])
        break

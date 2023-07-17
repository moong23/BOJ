num = int(input())
list_s = []

for _ in range(num):
    weight, height = map(int, input().split())
    list_s.append((weight, height))

for i in list_s:
    rank = 1
    for j in list_s:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

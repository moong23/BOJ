from itertools import combinations

testcse = int(input())
for _ in range(testcse):
    k = int(input())
    arr = []
    cnt = 0
    for _ in range(k):
        arr.append(input())

    for x in list(combinations(arr, 2)):
        tmp = x[0] + x[1]
        if tmp == tmp[::-1]:
            print(tmp)
            break
        tmp1 = x[1] + x[0]
        if tmp1 == tmp1[::-1]:
            print(tmp1)
            break
    else:
        print(0)

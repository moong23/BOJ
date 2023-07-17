num = int(input())

arr = list(map(int, input().split()))
# brr = sorted(set(arr))
brr = sorted(list(set(arr)))
dic = {brr[i]: i for i in range(len(brr))}
# print(dic)

for i in arr:
    print(dic[i], end=' ')

# for i in arr:
#     print(brr.index(i))

# print(arr)
# print(brr)

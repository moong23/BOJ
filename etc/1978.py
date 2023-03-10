# n = 1000
# a = [1]*(n+1)
# m = int(n ** 0.5)

# for i in range(2, m+1):
#     if a[i] == 1:
#         for j in range(i+i, n+1, i):
#             a[j] = 0
# print([i for i in range(2, n+1) if a[i] == 1])


# arr = []
# for i in range(2, 1001):
#     arr.append(i)

# for i in range(2, 1001):
#     for j in range(2, 1000):
#         if i*j > 1000:
#             break
#         if i*j in arr:
#             arr.remove(i*j)


n = 1000
arr = [1]*(n+1)
m = int(n ** 0.5)

for i in range(2, m+1):
    if arr[i] == 1:
        for j in range(i+i, n+1, i):
            arr[j] = 0
arr[0] = 0
arr[1] = 0
# print([i for i in range(2, n+1) if arr[i] == 1])
# print(arr)
a = int(input())
b = int(input())

arr1 = []
for h in range(a, b+1):
    if arr[h] == 1:
        arr1.append(h)

if len(arr1) == 0:
    print(-1)
else:
    print(sum(arr1))
    # print(arr1[0])

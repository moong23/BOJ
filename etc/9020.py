n = 10000
arr = [1]*(n+1)
m = int(n ** 0.5)

for i in range(2, m+1):
    if arr[i] == 1:
        for j in range(i+i, n+1, i):
            arr[j] = 0
arr[0] = 0
arr[1] = 0

num = int(input())

for _ in range(num):
    a = int(input())
    for i in range(int(a/2), 1, -1):
        # for i in range(2, int(a/2)+1):
        if arr[i] == 1:
            if arr[a-i] == 1:
                if i < a-i:
                    print(i, a-i)
                else:
                    print(a-i, i)
                break


# n = 10000
# arr = [1]*(n+1)
# m = int(n ** 0.5)

# for i in range(2, m+1):
#     if arr[i] == 1:
#         for j in range(i+i, n+1, i):
#             arr[j] = 0
# arr[0] = 0
# arr[1] = 0

# pt = []

# t = int(input())
# for _ in range(t):
#     pt1 = []
#     arr1 = []
#     a = int(input())
#     for h in range(a+1):
#         if arr[h] == 1:
#             arr1.append(h)

#     for u in range(len(arr1)):
#         for i in range(len(arr1)):
#             if arr1[u]+arr1[i] == a:
#                 pt1.append(arr1[u])
#                 pt1.append(arr1[i])
# # 두개이상있는경우
#     mini = []
#     if len(pt1) > 2:
#         for j in range(0, len(pt1), 2):
#             mini.append(pt1[j]-pt1[j+1])
#         pt.append(pt1[mini.index(min(mini))*2])
#         pt.append(pt1[mini.index(min(mini))*2+1])

# print(pt)

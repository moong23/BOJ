# t = int(input())

# for _ in range(t):
#     f = int(input())  # 1
#     num = int(input())  # 3
#     flo = []
#     for floor in range(f+1):  # 0~1
#         for he in range(1, num+1):  # 1~3
#             flo.append(he)  # flo[1,2,3] 0층
#         for ho in range(num+1, num+num+1):  # 3~6
#             flo.append(sum(flo))
#     print(flo[1])


t = int(input())

for _ in range(t):
    f = int(input())
    num = int(input())
    zero_f = []  # 0층
    for i in range(num):
        zero_f.append(i+1)
    for x in range(f):
        for i in range(1, num):
            zero_f[i] += zero_f[i-1]
    print(zero_f[-1])

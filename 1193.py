num = int(input())


a = num - 1
tmp = 1  # 몇번째 대각선에 속하는지
while a >= 0:
    a -= tmp
    tmp += 1
a += tmp
tmp -= 1

# print(a, tmp)

dir = tmp % 2  # 1: 아래 -> 위 / 0 : 위 -> 아래

if dir == 0:
    print(f'{a}/{tmp-a+1}')
else:
    print(f'{tmp-a+1}/{a}')

# [9] => a : 3 / tmp : 4
# dir 0 : [7]1/4 [8]2/3 [9]3/2 [10]4/1

# dir 1 : [11]5/1 [12]4/2 [13]3/3 [14]2/4 [15]1/5


# linecnt = 1
# num = 1
# direction = 0
# wholenum = 0
# i = int(input())  # 10
# while num < i:
#     for a in range(linecnt):  # [0]
#         num += a  # 1
#         if num >= i:
#             linecnt = a
#             break
# if linecnt % 2 == 0:
#     direction += 1
# else:
#     direction = 0

# for a in range(linecnt-1):
#     wholenum += a

# if direction == 1:
#     print(i-wholenum-1, '/', linecnt-(i-wholenum))
# else:
#     print(linecnt-(i-wholenum), '/', i-wholenum-1)

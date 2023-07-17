num = int(input())
while num:
    res = ''
    h, w, n = map(int, input().split())
    val = 1
    while 1:
        n -= h
        if n <= 0:
            break
        val += 1
    # print(val, n + h)
    res += str(n+h)
    if val < 10:
        res += '0' + str(val)
    else:
        res += str(val)
    print(res)
    num -= 1


# test_num = int(input())

# for x in range(test_num):
#     middle_num = 0
#     end_num = 1
#     ans = False
#     h, w, n = map(int, input().split())  # 6 12 10
#     while ans == False:
#         for i in range(h):  # 12
#             n = n-1  # 10
#             if n == 0:
#                 print(f'{i+1}{middle_num}{end_num}')
#                 # print(h)
#                 ans = True
#                 break
#         if n > 0:
#             end_num += 1
#         if end_num == 10:
#             end_num = 0
#             middle_num += 1

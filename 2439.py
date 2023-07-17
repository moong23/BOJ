a = int(input())
for b in range(1, 1+a):
    c = a-b
    print(' '*c + '*'*b)


# num = int(input())

# for x in range(num):
#     for _ in range(num-1, x, -1):
#         print(' ', end='')
#     for _ in range(x+1):
#         print('*', end='')
#     print('')

# for x in range(1, num+1):  # x = [1,2,3,4,5]
#     print(' '*(num-x), end='')
#     print('*'*x, end='')

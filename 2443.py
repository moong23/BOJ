# a = int(input())

# for i in range(a, 0, -1):
#     print(' '*(a-(i))+'*'*(2*i-1))
#     # print(i)

a = int(input())
for b in range(a, 0, -1):
    print(' ' * (a-b) + '*' * (2*b - 1))

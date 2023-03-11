num = int(input())

for _ in range(num):
    a, b = input().split()
    a = int(a)
    for x in b:
        print(a*x, end='')
    print('')

# test = int(input())
# for t in range(test):
#     inp = input()
#     num = int(inp[0])
#     le = []

#     for l in range(2, len(inp)):
#         for b in range(num):
#             le.append(inp[l])

#     print(le)

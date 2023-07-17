croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

test = input()

for x in croatia_alphabet:
    if x in test:
        test = test.replace(x, '*')
print(len(test))


# croa = list(input())
# wrdcnt = 0

# for i in range(2, int(len(croa))):
#     if croa[i-2] == 'c':
#         if croa[i-1] == '=' or croa[i-1] == '-':
#             wrdcnt += 1
#             croa[i-1] = 'x'
#     elif croa[i-2] == 'd':
#         if croa[i-1] == 'z' and croa[i] == '=':
#             wrdcnt += 1
#             croa[i-1] = 'x'
#             croa[i] = 'x'
#         if croa[i] == '-':
#             wrdcnt += 1
#             croa[i-1] = 'x'

#     elif croa[i-2] == 'l' and croa[i-1] == 'j':
#         wrdcnt += 1
#         croa[i-2] = 'x'
#         croa[i-1] = 'x'
#     elif croa[i-2] == 'z' and croa[i-1] == '=':
#         wrdcnt += 1
#         croa[i-1] = 'x'
#     elif croa[1-i] == 'x':
#         continue
#     else:
#         wrdcnt += 1
# print(wrdcnt)

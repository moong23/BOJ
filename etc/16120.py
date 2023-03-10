arr = input()
test = []
for x in arr:
    test.append(x)
    # print(test)
    # print(''.join(test[-4:]))
    if ''.join(test[-4:]) == 'PPAP':
        for _ in range(3):
            test.pop()
    # print(test)
if ''.join(test) == 'P':
    print('PPAP')
else:
    print('NP')

num = [input() for _ in range(5)]

numCode = {
    '0': ['*****', '*   *', '*****'],
    '1': ['     ', '     ', '*****'],
    '2': ['* ***', '* * *', '*** *'],
    '3': ['* * *', '* * *', '*****'],
    '4': ['***  ', '  *  ', '*****'],
    '5': ['*** *', '* * *', '* ***'],
    '6': ['*****', '* * *', '* ***'],
    '7': ['*    ', '*    ', '*****'],
    '8': ['*****', '* * *', '*****'],
    '9': ['*** *', '* * *', '*****'],
}

arr = []
for j in range(len(num[0])):
    tmp = ''
    if j % 4 == 3:
        continue
    for i in range(5):
        tmp += num[i][j]
    arr.append(tmp)

res = ''
for i in range(0, len(arr), 3):
    isValid = False
    for num, code in numCode.items():
        if code == arr[i:i+3]:
            isValid = True
            res += num
    if not isValid:
        print("BOOM!!")
        exit(0)
print("BEER!!" if int(res) % 6 == 0 else "BOOM!!")

arr = ''
while 1:
    try:
        tmp = input()
        arr += tmp
    except:
        break

print(sum(list(map(int, arr.split(',')))))

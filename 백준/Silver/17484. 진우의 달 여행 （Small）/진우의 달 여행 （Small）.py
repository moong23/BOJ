N, M = map(int,input().split())

def prep_data(num, N):
    rev_base = ''
    while num > 0:
        num, mod = divmod(num, N)
        rev_base += str(mod)
    return rev_base[::-1] 

def checkValid(_str, num):
    prev = int(_str[1]) - int(_str[0])
    if prev > 1:
        return 0
    elif prev < -1:
        return 0
    for i in range(2, num):
        now = int(_str[i]) - int(_str[i-1])
        if prev == now:
            return 0
        elif now >= 2:
            return 0
        elif now <= -2:
            return 0
        else:
            prev = now
    else:
        return 1

use_list = []
for i in range(pow(M, N)):
    tmp = prep_data(i, M).zfill(N)
    # print(tmp)
    if checkValid(tmp, N):
        use_list.append(tmp)
# print(use_list)

oil = []
for i in range(N):
    oil.append(list(map(int, input().split())))

_min = 99999999
for testcse in use_list:
    _sum = 0
    for idx in range(N):
        # print(oil[idx], testcse[idx])
        # print(oil[idx][int(testcse[idx])])
        _sum += oil[idx][int(testcse[idx])]
    _min = min(_min, _sum)
    # print(_min, _sum, testcse)
    # print('----------------')

print(_min)

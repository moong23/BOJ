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

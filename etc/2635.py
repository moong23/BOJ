
num = int(input())

result = []
len_res = 0
for i in range(num+1):
    res = [num, i]
    j = 0

    while True:
        recent_num = res[j] - res[j+1]
        j += 1
        if recent_num < 0:
            break
        res.append(recent_num)
        if len_res < len(res):
            len_res = len(res)
            result = res[:]

print(len_res)
for x in result:
    print(x, end=' ')

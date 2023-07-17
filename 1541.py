# https://www.acmicpc.net/problem/1541

in_str = input()
plusList = in_str.split('-')
res = []
for x in plusList:
    sum = 0
    for y in x.split('+'):
        sum += int(y)
    res.append(sum)
if (len(res) == 2):
    print(res[0] - res[1])
elif (len(res) == 1):
    print(res[0])
else:
    ret = 0
    for i in range(len(res)):
        if i == 0:
            ret += res[0]
        else:
            ret -= res[i]
    print(ret)
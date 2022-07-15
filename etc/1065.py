def hansu(num):
    ret = 0
    val = 0
    if len(str(num)) <= 2:
        return 1
    tmp = list(str(num))
    val = int(tmp[0]) - int(tmp[1])
    for c in range(1, len(tmp)-1):
        if val != (int(tmp[c]) - int(tmp[c+1])):
            break
    else:
        ret = 1
    return ret


num = int(input())
cnt = 0
for i in range(1, num+1):
    cnt += hansu(i)
print(cnt)

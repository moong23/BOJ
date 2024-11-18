N = int(input())

scheduleList = [0 for _ in range(367)]

_max = -1
_min = 365
for _ in range(N):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        scheduleList[i] += 1
    _max = max(_max, end)
    _min = min(_min, start)

# print(scheduleList[_min:_max+1])

curStack = 0
curLength = 0
res = 0
for i in range(_min,_max+2):
    if scheduleList[i] == 0:
        res += curStack * curLength
        curStack, curLength = 0, 0
    else:
        curLength += 1
        curStack = max(curStack, scheduleList[i])

print(res)
import sys
input = sys.stdin.readline

N = int(input())
liq = list(map(int, input().split()))

liq.sort()

start, end = 0, N-1

_min = sys.maxsize
_minL = [liq[start], liq[end]]
while start < end:
    _sum = liq[start] + liq[end]
    if _sum == 0:
        print(liq[start], liq[end])
        exit(0)
    else:
        if abs(_sum) < _min:
            _min = abs(_sum)
            _minL = [liq[start], liq[end]]
        _min = min(_min, abs(_sum))
        if _sum < 0:
            start += 1
        else:
            end -= 1
print(_minL[0], _minL[1])

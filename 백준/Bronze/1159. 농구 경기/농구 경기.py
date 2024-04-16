import sys
import string
input = sys.stdin.readline

N = int(input())

first = {}

for a in string.ascii_lowercase:
    first[a] = 0
res = set()
for _ in range(N):
    tmp = input()[0]
    first[tmp] += 1
    if first[tmp] >= 5:
        res.add(tmp)
else:
    if len(res) == 0:
        print('PREDAJA')
    else:
        print(''.join(sorted(res)))

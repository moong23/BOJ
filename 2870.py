import sys
import re
input = sys.stdin.readline


N = int(input())
in_str = []
for _ in range(N):
    in_str.append(input().rstrip())

use_list = []
for elem in in_str:
    for x in re.split(r'[a-z]', elem):
        if x.isdigit():
            use_list.append(int(x))

use_list.sort()
for y in use_list:
    print(y)

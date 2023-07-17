# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

import sys
while True:
    str = sys.stdin.readline().rstrip()
    if str == '0 0':
        break
    else:
        a, b = map(int, str.split())
        print(a+b)

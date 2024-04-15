import sys

input = sys.stdin.readline

N = int(input())

cmd = input().rstrip()

numArr = []
for _ in range(N):
    numArr.append(int(input()))


calArr = []
for x in cmd:
    # print(x, calArr)
    if x == '+':
        A, B = calArr.pop(), calArr.pop()
        calArr.append(A+B)
        continue
    elif x == '-':
        B, A = calArr.pop(), calArr.pop()
        calArr.append(A-B)
        continue
    elif x == '*':
        A, B = calArr.pop(), calArr.pop()
        calArr.append(A*B)
        continue
    elif x == '/':
        B, A = calArr.pop(), calArr.pop()
        calArr.append(A/B)
        continue
    else:
        calArr.append(numArr[ord(x)-ord('A')])
else:
    print('{:.2f}'.format(calArr[0]))

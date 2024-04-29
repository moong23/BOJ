import sys
input = sys.stdin.readline

inStr = input()

pStack = []
res = 0
tmp = 1
for i in range(len(inStr)):
    target = inStr[i]
    if target == '(':
        tmp *= 2
        pStack.append('(')
    elif target == '[':
        tmp *= 3
        pStack.append('[')
    elif target == ')':
        if not pStack or pStack[-1] != '(':
            print(0)
            exit(0)

        if inStr[i-1] == '(':
            res += tmp
        tmp /= 2
        pStack.pop()
    elif target == ']':
        if not pStack or pStack[-1] != '[':
            print(0)
            exit(0)
        if inStr[i-1] == '[':
            res += tmp
        tmp /= 3
        pStack.pop()
else:
    if len(pStack):
        print(0)
        exit(0)
    print(int(res))

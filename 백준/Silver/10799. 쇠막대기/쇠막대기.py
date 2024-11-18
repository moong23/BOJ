import sys
input = sys.stdin.readline

x = input()

pipeCnt = 0
pipeStack = 0

i = 0
# for i in range(len(x)):
while i < len(x)-1 :
    # print(i, x[i:], pipeCnt, pipeStack)
    if x[i] == '(':
        if x[i+1] == ')':
            pipeCnt += pipeStack
            i += 2
        else:
            pipeStack += 1
            i += 1
    else:
        pipeStack -= 1
        pipeCnt += 1
        i += 1


print(pipeCnt)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input())
tmp = K
stack = []

for i in range(N):
    while tmp > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        tmp -= 1
    stack.append(num[i])

print(''.join(stack[:N-K]))

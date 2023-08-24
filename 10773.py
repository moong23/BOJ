N = int(input())

stack = []
for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)
print(sum(stack))

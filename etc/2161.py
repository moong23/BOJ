from collections import deque
num = int(input())
arr = deque()

for i in range(1, num+1):
    arr.append(i)

while True:
    if len(arr) == 1:
        break
    print(arr.popleft())
    arr.append(arr.popleft())

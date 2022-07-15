from math import sqrt
num = int(input())
idx = 2

while True:
    if num == 1:
        break
    if num % idx == 0:
        print(idx)
        if idx == num:
            break
        num /= idx
    else:
        idx += 1

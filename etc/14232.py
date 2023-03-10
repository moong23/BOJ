num = int(input())
arr = ''
cnt = 0
i = 2
while num != 1:
    if i >= 1000000:
        arr += str(int(num))
        cnt += 1
        break
    if num % i == 0:
        num /= i
        arr += str(i) + ' '
        cnt += 1
    else:
        i += 1
print(cnt)
print(arr)

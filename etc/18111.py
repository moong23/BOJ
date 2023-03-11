n, m, inven = map(int, input().split())

arr = []
min_val = 257
max_val = -1
min_time = 99999
for _ in range(n):
    tmp = list(map(int, input().split()))
    for x in tmp:
        if x < min_val:
            min_val = x
        elif x > max_val:
            max_val = x
        arr.append(x)
print(arr)
# print(min_val, max_val)

for i in range(min_val, max_val + 1):
    time_total = 0
    inven_tmp = inven
    for x in arr:
        if i < x:
            inven_tmp += x - i
            time_total += 2 * (x - i)
        elif i > x:
            inven_tmp -= (i - x)
            if inven_tmp < 0:

                time_total = 99999
                break
            time_total += i - x
    if min_time > time_total:
        min_time = time_total
        min_block = i

print(min_time, min_block)

num = int(input())
if num == 1:
    print(0)
    exit()
elif num == 2:
    print(1)
    exit()

arr = [1 for _ in range(num+1)]
# print(arr)
arr[0], arr[1] = 0, 0
for i in range(2, int(pow(num, 1/2))+1):
    if arr[i] == 1:
        for j in range(i+i, num+1, i):
            arr[j] = 0

# print(arr)

brr = []
for x in range(len(arr)):
    if arr[x] == 1:
        brr.append(x)
# print(brr)
start, end = 0, 1
tmp_sum = brr[0] + brr[1]
cnt = 0

while start < len(brr):
    # print(brr[start], brr[end], tmp_sum, num)
    if tmp_sum < num:
        end += 1
        if end >= len(brr) or start >= len(brr):
            break
        tmp_sum += brr[end]
    elif tmp_sum == num:
        # print('-------------------')
        cnt += 1
        end += 1
        if end >= len(brr) or start >= len(brr):
            break
        tmp_sum = tmp_sum + brr[end] - brr[start]
        start += 1
    else:
        tmp_sum -= brr[start]
        start += 1
        if end >= len(brr) or start >= len(brr):
            break

print(cnt)

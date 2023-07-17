num = int(input())
arr = []
for _ in range(num):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x: (x[1], x[0]))
# print(arr)
end = arr[0][1]
cnt = 1
for x in arr[1:]:
    # print(x)

    if x[0] >= end:
        cnt += 1
        end = x[1]

print(cnt)

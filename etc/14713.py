a = int(input())
arr = []
for _ in range(a):
    arr.append(list(map(str, input().split())))
# print(arr)
brr = list(map(str, input().split()))

for x in brr:
    for i in range(a):
        # print(x, arr[i])
        if arr[i][0] == x:
            arr[i].pop(0)
            if(len(arr[i]) == 0):
                arr[i].append('')
            break
    else:
        print('Impossible')
        break
else:
    print('Possible')

# print(arr)

a, b = map(int, input().split())
arr_1 = list(map(int, input().split()))

arr = []

for x in range(len(arr_1)):
    for y in range(x+1, len(arr_1)):
        for z in range(y+1, len(arr_1)):
            ans = arr_1[x]+arr_1[y]+arr_1[z]
            if ans <= b:
                arr.append(ans)

print(max(arr))

sum1 = 0
sum2 = 0
for i in range(9591):
    arr = input().split(',')
    print(arr)
    sum1 += float(arr[0])
    sum2 += float(arr[2])

print('sum1',sum1)
print('sum2',sum2)
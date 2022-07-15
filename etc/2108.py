num = int(input())

arr = list()
for i in range(num):
    arr.append(int(input()))

print(round(sum(arr)/len(arr)))
arr.sort()
print(arr[len(arr)//2+1])

arr = []
for _ in range(5):
    arr.append(int(input()))
arr.sort()
print(int(sum(arr)/len(arr)))
print(arr[2])

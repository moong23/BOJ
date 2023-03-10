num = 1000000000

arr = [1]*(num+1)

arr[0], arr[1] = 0, 0

for i in range(int(pow(num, 1/2))):
    if arr[i] == 1:
        for j in range(i+i, num+1, i):
            arr[j] = 0

maxcnt = 0
n = int(input())

def rowcheck():
    global maxcnt
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
                maxcnt = max(maxcnt, cnt)
            else:
                cnt = 1

def colcheck():
    global maxcnt

    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                cnt += 1
                maxcnt = max(maxcnt, cnt)
            else:
                cnt = 1

def check():
    rowcheck()
    colcheck()



arr = []

for _ in range(n):
    tmp = list(map(str,input()))
    arr.append(tmp)

for i in range(n):
    for j in range(n-1):
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        check()
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        check()
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]


print(maxcnt)
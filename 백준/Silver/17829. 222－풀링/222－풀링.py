import sys
input = sys.stdin.readline

N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]

def check_second(i, j):
    a, b = Arr[i][j:j+2]
    c, d = Arr[i+1][j:j+2]
    return sorted([a, b, c, d], reverse=True)[1]

while True:
    size = len(Arr)
    if size == 1:
        print(Arr[0][0])
        break
    brr = [[None for _ in range(size // 2)] for _ in range(size // 2)]
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            brr[i // 2][j // 2] = check_second(i, j)
    Arr = brr
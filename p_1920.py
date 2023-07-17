# week 1 binary search
# http: // acmicpc.net/problem/1920
# python ver

def binary_search(start, end, Arr, target):
    while start <= end:
        mid = (start + end) // 2
        if Arr[mid] > target:
            end = mid - 1
        elif Arr[mid] < target:
            start = mid+1
        else:
            return print(1)
    return print(0)


N = int(input())  # int형 변수로 N 입력받기
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    binary_search(0, N-1, A, i)

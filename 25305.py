a, b = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=1)
print(arr[b-1])

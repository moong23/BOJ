a, b = map(int, input().split())
arr = list(map(int, input().split()))
max_arr = len(arr)-1
arr = arr*2
# print(arr, max_arr)
start, end = 0, b
tmp_max = -1
tmp_sum = sum(arr[start:end])
while start <= max_arr:
    tmp_sum -= arr[start]
    tmp_sum += arr[end]
    tmp_max = max(tmp_max, tmp_sum)
    start += 1
    end += 1
print(tmp_max)

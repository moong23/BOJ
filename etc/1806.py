N, S = map(int, input().split())

arr = list(map(int, input().split())) + [0 for _ in range(10001)]
arr.insert(0, 0)

start, end = 0, 1
tmp_sum = arr[0] + arr[1]
short = len(arr) + 1

while end <= N:
    if tmp_sum < S:
        end += 1
        tmp_sum += arr[end]
    else:
        short = min(short, end-start+1)
        tmp_sum -= arr[start]
        start += 1

if short == len(arr)+1:
    print(0)
else:
    print(short)

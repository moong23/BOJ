N = int(input())
start, end = 0, 1
cnt = 0
num_sum = 1
while start < N//2 + 1:  # [0,3]
    if num_sum < N:
        end += 1
        num_sum += end
    elif num_sum == N:
        cnt += 1
        end += 1
        num_sum -= start
        num_sum += end
        start += 1
    else:
        num_sum -= start
        start += 1

print(cnt+1)

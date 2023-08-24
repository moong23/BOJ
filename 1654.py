K, N = map(int, input().split())
rope = []
for _ in range(K):
    rope.append(int(input()))

start = 1
end = max(rope)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in rope:
        cnt += i // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)

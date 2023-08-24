N, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
arr = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        arr[i] = min(arr[i], arr[i-1]+1)
    for start, end, shortcut in graph:
        if i == start and end <= D and arr[i] + shortcut < arr[end]:
            arr[end] = arr[i] + shortcut

print(arr[D])

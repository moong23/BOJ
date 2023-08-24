n = int(input())

array = [i for i in range(n + 1)]
array[1] = 0
history = [i for i in range(n + 1)]
history[1] = 0

for i in range(2, n + 1):
    array[i] = array[i - 1] + 1
    history[i] = i - 1

    if i % 3 == 0 and array[i] > array[i // 3] + 1:
        array[i] = array[i // 3] + 1
        history[i] = i // 3
    if i % 2 == 0 and array[i] > array[i // 2] + 1:
        array[i] = array[i // 2] + 1
        history[i] = i // 2

print(array[n])
print(n, end=" ")

res = n
while history[res] != 0:
    print(history[res], end=" ")
    res = history[res]

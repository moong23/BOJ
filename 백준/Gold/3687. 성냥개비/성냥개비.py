T = int(input())
queries = []

for _ in range(T):
    queries.append(int(input()))

dpMin = [float('inf')] * 101
dpMax = ["0"] * 101

dpMin[2] = 1
dpMin[3] = 7
dpMin[4] = 4
dpMin[5] = 2
dpMin[6] = 6
dpMin[7] = 8
dpMin[8] = 10

minDigits = ["1", "7", "4", "2", "0", "8"]

for i in range(9, 101):
    for j in range(2, 8):
        dpMin[i] = min(dpMin[i], int(str(dpMin[i - j]) + minDigits[j - 2]))

maxDigits = ["7", "7", "1", "7", "4", "2", "6", "8"]
dpMax[2] = "1"

for i in range(3, 101):
    if i % 2 == 0:
        dpMax[i] = "1" * (i // 2)
    else:
        dpMax[i] = maxDigits[i % 2] + "1" * (i // 2 - 1)

result = []
for m in queries:
    result.append(f"{dpMin[m]} {dpMax[m]}")

print("\n".join(result))

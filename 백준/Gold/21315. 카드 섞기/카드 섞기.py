import math

def suffle(case, index):
    if index == 0:
        return case
    newList = case[len(case)-index:]
    return suffle(newList, index//2) + case[:len(case)-index]
    
N = int(input())

tcArr = list(map(int, input().split()))

maxK = int(math.log2(N))
result = []

for k1 in range(1, maxK+1):
    for k2 in range(1, maxK+1):
        card_list = [i for i in range(1, N+1)]
        if suffle(suffle(card_list, 2**k1), 2**k2) == tcArr:
            result.append((k1, k2))

print(*result[0])
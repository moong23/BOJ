import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)


def hit(eggs, i, j):
    eggs[i][0] -= eggs[j][1]
    eggs[j][0] -= eggs[i][1]


def unhit(eggs, i, j):
    eggs[i][0] += eggs[j][1]
    eggs[j][0] += eggs[i][1]


def count_broken(eggs):
    return sum(1 for s, _ in eggs if s <= 0)


def backtrack(eggs, index, max_broken):
    if index == len(eggs):
        max_broken[0] = max(max_broken[0], count_broken(eggs))
        return

    if eggs[index][0] <= 0:
        backtrack(eggs, index + 1, max_broken)
    else:
        all_broken = True
        for i in range(len(eggs)):
            if i != index and eggs[i][0] > 0:
                hit(eggs, index, i)
                backtrack(eggs, index + 1, max_broken)
                unhit(eggs, index, i)
                all_broken = False
        if all_broken:
            backtrack(eggs, index + 1, max_broken)


input_data = input().split()
N = int(input_data[0])
eggs = []
for i in range(N):
    S, W = map(int, input_data[2*i + 1: 2*i + 3])
    eggs.append([S, W])

max_broken = [0]
backtrack(eggs, 0, max_broken)
print(max_broken[0])

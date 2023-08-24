def dfs(start, target):
    if start == target:
        return 1

    if len(target) <= len(start):
        return 0

    ans = 0
    if target[-1] == 'A':
        ans = dfs(start, target[:-1])
    if ans == 1:
        return 1

    if target[0] == 'B':
        ans = dfs(start, target[::-1][:-1])

    return ans


S = list(input())
T = list(input())

print(dfs(S, T))

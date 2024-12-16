def dfs(target, cNum, cVal, cSign, cSum, exp):
    if target == cNum:
        cSum = cSum + (cVal * cSign)
        if cSum == 0:
            result.append(exp + "\n")
        return
    dfs(target, cNum + 1, cVal * 10 + (cNum + 1), cSign, cSum, exp + " " + str(cNum + 1))
    dfs(target, cNum + 1, cNum + 1, 1, cSum + (cVal * cSign), exp + "+" + str(cNum + 1))
    dfs(target, cNum + 1, cNum + 1, -1, cSum + (cVal * cSign), exp + "-" + str(cNum + 1))


result = []
test_cases = int(input())

for _ in range(test_cases):
    target = int(input())
    dfs(target, 1, 1, 1, 0, "1")
    result.append("\n")

print("".join(result))

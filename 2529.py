max_num = 10


def check(a, b, char):
    if char == '<':
        if a > b:
            return 0
    if char == '>':
        if a < b:
            return 0
    return 1


def dfs(cnt, num):
    if cnt == k+1:
        answer.append(num)
        return

    for i in range(max_num):
        if visited[i]:
            continue

        if cnt == 0 or check(num[cnt-1], str(i), inequList[cnt-1]):
            visited[i] = 1
            dfs(cnt+1, num+str(i))
            visited[i] = 0


k = int(input())
inequList = list(input().split())

visited = [0]*max_num
answer = []
dfs(0, '')

answer.sort()
print(answer[-1])
print(answer[0])

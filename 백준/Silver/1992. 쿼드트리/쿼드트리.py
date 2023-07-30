N = int(input())
tree = [list(map(int, input())) for _ in range(N)]


def dfs(x, y, n):
    tmp = tree[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != tree[i][j]:
                tmp = -1
                break

    if tmp == -1:
        print("(", end='')
        n //= 2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x+n, y, n)
        dfs(x+n, y+n, n)
        print(")", end='')
    elif tmp == 1:
        print(1, end='')
    else:
        print(0, end='')


dfs(0, 0, N)

N = 19

board = [list(map(int, input().split())) for _ in range(N)]

dir = [[1, 0], [1, 1], [0, 1], [-1, 1]]

winner = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            target = board[i][j]
            for x, y in dir:
                cnt = 1
                nx = x + i
                ny = y + j
                while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == target:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= i - x < N and 0 <= j - y < N and board[i-x][j-y] == target:
                            break
                        if 0 <= nx + x < N and 0 <= ny + y < N and board[nx+x][ny+y] == target:
                            break
                        print(target)
                        print(i+1, j+1)
                        exit(0)
                    nx += x
                    ny += y
else:
    print(0)

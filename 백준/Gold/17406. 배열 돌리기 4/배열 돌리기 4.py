from itertools import permutations
import copy


def calc_min(arr):
    _min = 1000000
    for i in range(N):
        _min = min(_min, sum(arr[i]))
    return _min


def spin_arr(arr, calc):
    R, C, S = calc
    R, C = R-1, C-1
    for n in range(S, 0, -1):
        tmp = arr[R-n][C+n]
        arr[R-n][C-n+1:C+n+1] = arr[R-n][C-n:C+n]
        for row in range(R-n, R+n):
            arr[row][C-n] = arr[row+1][C-n]
        arr[R+n][C-n:C+n] = arr[R+n][C-n+1:C+n+1]
        for row in range(R+n, R-n, -1):
            arr[row][C+n] = arr[row-1][C+n]
        arr[R-n+1][C+n] = tmp

    return arr


def test_arr(arr, order):
    tmpArr = copy.deepcopy(arr)

    # print('og:', calc[order[0]], calc[order[1]])
    # for x in tmpArr:
    #     print(x)
    # print('---------------')
    for idx in order:
        tmpArr = spin_arr(tmpArr, calc[idx])
        # for x in tmpArr:
        #     print(x)
        # print('-----------------')
    return calc_min(tmpArr)


N, M, K = map(int, input().split())


arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
calc = []
for _ in range(K):
    calc.append(list(map(int, input().split())))

_min = 1000000
for idx in list(permutations(range(K), K)):
    _min = min(_min, test_arr(arr, idx))
print(_min)

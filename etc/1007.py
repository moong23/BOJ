import math
from itertools import combinations, permutations
testcse = int(input())
for _ in range(testcse):
    num = int(input())
    arr = []
    for _ in range(num):
        arr.append(list(map(int, input().split())))
    print(arr)
    leng = len(arr)
    if leng == 2:
        print(math.sqrt(pow(arr[0][0]-arr[1][0], 2) +
              pow(arr[0][1]-arr[1][1], 2)))
        continue
    min_dist = 99999999
    for x in list(permutations([i for i in range(leng)], 4)):
        # print(x)
        print(arr[x[0]], arr[x[1]], arr[x[2]], arr[x[3]])
        tmp1 = [arr[x[0]][0]-arr[x[1]][0], arr[x[0]][1]-arr[x[1]][1]]
        tmp2 = [arr[x[2]][0]-arr[x[3]][0], arr[x[2]][1]-arr[x[3]][1]]
        print(tmp1, tmp2)
        print(math.dist([0, 0], [tmp1[0]+tmp2[0], tmp1[1]+tmp2[1]]))
        min_dist = min(min_dist, math.dist(
            [0, 0], [tmp1[0]+tmp2[0], tmp1[1]+tmp2[1]]))
        # print(math.dist([arr[x[0]][0]-arr[x[1]][0],
        #                  arr[x[0]][1]-arr[x[1]][1]],
        #                 [arr[x[2]][0]-arr[x[3]][0],
        #                  arr[x[2]][1]-arr[x[3]][1]]))
        # min_dist = min(min_dist, math.dist([arr[x[0]][0]-arr[x[1]][0],
        #                                     arr[x[0]][1]-arr[x[1]][1]],
        #                                    [arr[x[2]][0]-arr[x[3]][0],
        #                                    arr[x[2]][1]-arr[x[3]][1]]))
    print(min_dist)

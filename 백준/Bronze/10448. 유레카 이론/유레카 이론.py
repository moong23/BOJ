tri = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990]
total = len(tri)
def check(num):
    for i in range(total):
        for j in range(i, total):
            for k in range(j, total):
                if tri[i] + tri[j] + tri[k] == num:
                    print(1)
                    return;
    else:
        print(0)


N = int(input())
for _ in range(N):
    check(int(input()))
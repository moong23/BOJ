# def d(n):
#     n = n + sum(map(int, str(n)))
#     return n


# noSelfNum = set()

# for i in range(1, 10001):
#     noSelfNum.add(d(i))

# for j in range(1, 10001):
#     if j not in noSelfNum:
#         print(j)


def selfNum(num):
    num += sum(map(int, str(num)))
    return num


arr = [i for i in range(1, 10001)]
for i in range(1, 10001):
    if selfNum(i) <= 10000:
        try:
            arr.remove(selfNum(i))
        except:
            pass


print(*arr)

def first(testStr, K):
    _l = float('inf')
    tmp = {}

    for i, x in enumerate(testStr):
        if x not in tmp:
            tmp[x] = []
        tmp[x].append(i)

        if len(tmp[x]) >= K:
            length = tmp[x][-1] - tmp[x][-K] + 1
            _l = min(_l, length)

    return _l if _l != float('inf') else -1

def second(testStr, K):
    _l = -1
    tmp = {}

    for i, x in enumerate(testStr):
        if x not in tmp:
            tmp[x] = []
        tmp[x].append(i)

        if len(tmp[x]) >= K:
            length = tmp[x][-1] - tmp[x][-K] + 1
            _l = max(_l, length)

    return _l if _l != -1 else -1

T = int(input())

for _ in range(T):
    test_case = input()
    K = int(input())
    f = first(test_case, K)
    s = second(test_case, K)
    print(f, s) if (f != -1 and s != -1) else print(-1)

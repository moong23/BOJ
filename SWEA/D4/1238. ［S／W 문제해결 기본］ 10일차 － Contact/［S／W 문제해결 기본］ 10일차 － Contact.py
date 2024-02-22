testcase = 10

for i in range(testcase):
    contact = {}
    visited = []
    current = []
    bigList = []
    _length, start = map(int, input().split())
    _str = list(map(int, input().split()))
    idx = 0
    while (idx < _length):
        if _str[idx] in contact.keys():
            contact[_str[idx]].append(_str[idx+1])
        else:
            contact[_str[idx]] = [_str[idx+1]]
        idx += 2
    # print(contact)
    current.append(start)
    visited.append(start)
    big = -1
    while (current):
        # print('current :', current)
        big = -1
        deletion = []
        addition = []
        for cu in current:
            deletion.append(cu)
            if cu in contact:
                target = contact[cu]
                for x in target:
                    if x not in current and x not in visited:
                        big = max(big, x)
                        visited.append(x)
                        addition.append(x)
        # if (len(addition) == 0):
        #     print('++++++++')
        for x in deletion:
            current.remove(x)
        for x in addition:
            current.append(x)
        # print('current :', current)
        # print('visited :', visited)
        bigList.append(big)

    print(f'#{i+1} {bigList[-2]}')

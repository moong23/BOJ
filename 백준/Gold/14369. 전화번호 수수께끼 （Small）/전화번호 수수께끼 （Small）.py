numbers = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
# unique = {
#     0: ['Z'],
#     1: [],
#     2: ['W'],
#     3: [],
#     4: ['U'],
#     5: [],
#     6: ['X'],
#     7: [],
#     8: ['G'],
#     9: [],
# }
unique = {
    'G': 8,
    'Z': 0,
    'W': 2,
    'U': 4,
    'X': 6
}
# no_unique = [1,3,5,7,9]

no_unique = {
    'O': 1,
    'T': 3,
    'F': 5,
    'S': 7,
}

# ONE    O
# THREE  T H R
# FIVE   F
# SEVEN  S
# NINE   


N = int(input())

for i in range(N):
    res = []
    in_str = list(input())
    # print(*in_str)
    tmp = in_str.copy()
    for x in tmp:
        if x in unique.keys():
            # print(unique[x], x)
            res.append(unique[x])
            for word in numbers[unique[x]]:
                in_str.remove(word)
            # print(res, numbers[unique[x]], in_str)
        tmp = in_str.copy()

    for y in tmp:
        if y in no_unique.keys():
            # print(no_unique[y], y)
            res.append(no_unique[y])
            for word in numbers[no_unique[y]]:
                in_str.remove(word)
            # print(res, numbers[no_unique[y]], in_str)
        tmp = in_str.copy()
    while len(in_str) > 0:
        res.append(9)
        for word in numbers[9]:
            in_str.remove(word)
        
    res.sort()
    ret = ''
    for num in res:
        ret += str(num)
    print(f"Case #{i+1}: {ret}")

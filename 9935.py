arr = input()
bomb = input()
len_bomb = len(bomb)
test = []
for x in arr:
    test.append(x)
    if ''.join(test[-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            test.pop()
if len(test) == 0:
    print('FRULA')
else:
    print(''.join(test))

a, b = map(int, input().split(' '))

p_list = list(map(int, input().split(' ')))
p_list = p_list * 2

chk_list = list()
for i in range(a):
    chk_list.append(0)
for i in range(a):
    for j in range(0, b):
        chk_list[i] += p_list[i+j]
print(chk_list)

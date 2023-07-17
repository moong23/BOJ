from string import ascii_lowercase
alphabet = (ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
v = []
a = input()  # baekjoon


for i in alphabet:
    if i in a:
        v.append(a.index(i))
    else:
        v.append(-1)
print(*v)

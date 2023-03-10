a = []
for i in range(10):
    a.append(int(input()) % 42)
    # a = [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
   # a => set(a) a = [39, 40, 41, 0, 1, 2]
print(len(set(a)))

a = []
for i in range(10):
    a.append(int(input()) % 42)
print(a)
b = []
for i in a:  # a = [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
    if i not in b:
        b.append(i)  # b = [39, 40, 41, 0, 1, 2]
print(len(b))

# for i in range(int(input())):
#     b = input()  # 5 50 50 70 80 100
#     a = []
#     for i in b.split()[1:]:  # [50, 50, 70, 80, 100]
#         a.append(int(i))
# #     print(a)


for i in range(int(input())):
    b = input()
    a = []
    for i in b.split()[1:]:
        a.append(int(i))
    c = sum(a)/int(b.split()[0])
    f = []
    for s in range(len(a)):
        if int(a[s]) > c:
            f.append(int(a[s]))
    g = round(len(f)/len(a)*100, 3)
    print(f'{g:.3f}%')

a = []
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)

# a = []
# max = -1
# for i in range(9):
#     a.append(int(input()))
#     if max < a[i]:
#         max = a[i]
# print(max)
# print(a.index(max)+1)

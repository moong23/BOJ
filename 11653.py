# num = int(input())
# idx = 2

# while True:
#     if num == 1:
#         break
#     if num % idx == 0:
#         print(idx)
#         if idx == num:
#             break
#         num /= idx
#     else:
#         idx += 1


a = int(input())
b = a
j = []
for h in range(2, a+1):
    for _ in range(a):
        if b % h == 0:
            j.append(h)
            b = b//h
        else:
            break
    if b == 1:
        break

for ui in range(len(j)):
    print(j[ui])

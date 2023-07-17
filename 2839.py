n = int(input())

res = 0

while n >= 0:
    if n % 5 == 0:
        res += n // 5
        print(res)
        break
    n -= 3
    res += 1
else:
    print(-1)
# #


# kg = int(input())
# if int((kg % 5)/3) == (kg % 5)/3:
#     print(int(int(kg/5)+kg % 5/3))
# elif int((kg % 5)/3) != (kg % 5)/3:
#     if kg % 3 == 0:
#         print(int(kg/3))
#     elif int((kg % 3+3) / 5) == ((kg % 3+3) / 5):
#         print(int(1+(kg-5)/3))
#     else:
#         print(-1)

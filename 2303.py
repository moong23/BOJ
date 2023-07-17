a = int(input())
num_list = []
for i in range(a):
    b = list(map(int, input().split()))
    num_list.append(b)


per_num = 0
ans_list = []


# print(num_list)
for n in num_list:
    cnt = -1
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                num = (n[i] + n[j] + n[k]) % 10
                if num >= cnt:
                    cnt = num
    ans_list.append(cnt)

max = -1

for x in range(len(ans_list)):
    if ans_list[x] >= max:
        max = ans_list[x]
        ans = x+1
print(ans)

# from itertools import combinations
# num = int(input())

# arr_a = list(map(int, input().split()))
# arr_b = list(map(int, input().split()))
# arr_c = list(map(int, input().split()))

# max_a = -1
# for x in list(combinations(arr_a, 3)):
#     tmp = (x[0] + x[1] + x[2]) % 10
#     if(max_a < tmp):
#         max_a = tmp

# max_b = -1
# for x in list(combinations(arr_b, 3)):
#     tmp = (x[0] + x[1] + x[2]) % 10
#     if(max_b < tmp):
#         max_b = tmp

# max_c = -1
# for x in list(combinations(arr_c, 3)):
#     tmp = (x[0] + x[1] + x[2]) % 10
#     if(max_c < tmp):
#         max_c = tmp

# answer = []

# answer.append(max_a)
# answer.append(max_b)
# answer.append(max_c)

# if answer[0] == answer[1]:
#     if answer[0] > answer[2]:
#         if max(arr_a) > max(arr_b):
#             print(1)
#         else:
#             print(2)
# elif answer[1] == answer[2]:
#     if answer[1] > answer[0]:
#         if max(arr_b) > max(arr_c):
#             print(2)
#         else:
#             print(3)
# elif answer[0] == answer[2]:
#     if answer[0] > answer[2]:
#         if max(arr_a) > max(arr_c):
#             print(1)
#         else:
#             print(3)
# else:
#     print(answer.index(max(answer))+1)

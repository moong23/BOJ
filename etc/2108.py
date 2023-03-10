import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))


print(round(sum(li)/n))


li.sort()
print(li[n//2])


print(Counter(li).most_common())
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:  # 최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])


print(max(li)-min(li))
# import sys
# a = int(input())
# b = []
# for i in range(a):
#     c = int(sys.stdin.readline())
#     b.append(c)
# b.sort()

# #########


# print(round(sum(b)/a))
# #########
# middle_len = int(len(b)/2)
# print(b[middle_len])
# #########
# dic = dict()

# for x in b:
#     if x not in dic:
#         dic[x] = 1
#     else:
#         dic[x] += 1

# max_int = max(list(dic.values()))

# ans_list = []

# for x, y in dic.items():
#     if y == max_int:
#         ans_list.append(x)
# ans_list.sort()
# if len(ans_list) == 1:
#     print(ans_list[0])
# else:
#     print(ans_list[1])

# print(b[a-1]-b[0])

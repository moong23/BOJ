# from string import ascii_lowercase

# num = int(input())
# cnt = 0
# for _ in range(num):
#     alpha = list(ascii_lowercase)
#     a = input()
#     tmp = a[0]
#     for i in a:  # happy i = a
#         if i == tmp:
#             continue
#         else:
#             if i in alpha:
#                 alpha.remove(tmp)
#                 tmp = i
#             else:
#                 break
#     else:
#         cnt += 1

# print(cnt)


# # from string import ascii_lowercase
# # alphabet = ascii_lowercase

# # for _ in range(int(input())):
# #     wrd = list(input())
# #     double = 0
# #     wrdcnt = 0
# #     for i in range(len(wrd)):
# #         for n in (alphabet):
# #             cnt = wrd.count(n)

# #             if n == wrd[i]:
# #                 double += 1
# #             else:
# #                 break
# #                 if double == cnt:
# #                     if double == wrdcnt:
# #                         wrdcnt += 1

# # print(wrdcnt)


N = int(input())
count = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break
print(count)

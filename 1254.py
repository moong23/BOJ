def palindrom_bf(word):
    for i in range(len(word)):
        if word[i:] == word[i:][::-1]:
            return i+len(word), word[::-1][len(word)-i:]


'abdfhdyrbdbsdfghjkllkjhgfds'


# def pal_check(word):
#     if word[:] == word[::-1]:
#         return 1
#     else:
#         return 0


# def palindrom_bf(word):
#     for i in range(len(word)):
#         # print(word[i:])
#         if pal_check(word[i:]) == 1:
#             break
#     # print(word[0:i],i)
#     return i, word[::-1][len(word)-i:]


arr = input()

print(palindrom_bf(arr))

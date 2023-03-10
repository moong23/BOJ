word = input().upper()  # 'aaabbbc'
word_list = list(set(word))  # ['a','b','c']

cnt = []  # [3,2,1]
for i in word_list:
    cnt.append(word.count(i))  # [3,3,1]

if cnt.count(max(cnt)) > 1:  # cnt.count(max(cnt)) = 2
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))])

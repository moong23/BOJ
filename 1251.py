word = input()
ans = []
for i in range(1, len(word) - 1):
    for j in range(i+1, len(word)):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]
        ans.append(a+b+c)
ans.sort()
print(ans[0])

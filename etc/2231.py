a = int(input())
b = []
dupli_num = 0
ans_num = 0

for i in range(a):
    dupli_num = i
    ans_num += dupli_num
    j = str(i)
    for n in j:
        n = int(n)
        ans_num += n
    if ans_num == a:
        b.append(j)
    ans_num = 0

print(min(b))

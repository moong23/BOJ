from string import ascii_lowercase


num = int(input())
cnt = 0
while num:
    alpha = list(ascii_lowercase)
    a = input()
    tmp = a[0]
    for i in a:
        if i == tmp:
            continue
        else:
            if i in alpha:
                alpha.remove(tmp)
                tmp = i
            else:
                break
    else:
        cnt += 1

    num -= 1
print(cnt)

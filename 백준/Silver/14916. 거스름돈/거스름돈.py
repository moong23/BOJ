# https://www.acmicpc.net/problem/14916

money = int(input())

cnt = 0
while money > 0:
    if money % 5 == 0 :
        cnt += money // 5
        break
    money -= 2
    cnt += 1
if money < 0:
    cnt = -1

print(cnt)
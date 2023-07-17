a = '고무오리 디버깅 시작'
b = '고무오리'
c = '문제'
d = '고무오리 디버깅 끝'
e = '고무오리야 사랑해'
f = '힝구'
cnt = 0

while(1):
    tmp = input()
    if(tmp == a):
        continue
    if(tmp == b):
        cnt -= 1
        if(cnt < 0):
            cnt += 3
    if(tmp == c):
        cnt += 1
    if(tmp == d):
        break
if(cnt == 0):
    print(e)
else:
    print(f)

# https://www.acmicpc.net/problem/1343

in_str = input()

cont_cnt = 0
result = ''
res = ''
for x in in_str:
    if x == '.':
        # 2의 배수 아니면 배열 불가능 -> -1 return
        # 4로 나누었을때 몫만큼 A 덮기
        # 나머지 B 덮기
        if cont_cnt % 2 == 1 :
            result = -1
            break
        while cont_cnt >= 4 :
            res += 'AAAA'
            cont_cnt -=4
        if cont_cnt == 2 :
            res += 'BB'
        cont_cnt = 0
        res += x
    else:
        cont_cnt += 1
else:
    # 끝까지 다 가면 정상임
    if cont_cnt % 2 == 1 :
        res = -1
    else :    
        while cont_cnt >= 4 :
            res += 'AAAA'
            cont_cnt -=4
        if cont_cnt == 2 :
            res += 'BB'
    result = res

print(result)
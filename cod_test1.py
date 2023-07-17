def solution(lottos, win_nums):
    cnt_zero = 0
    cnt_match = 0
    answer = []
    for i in lottos:
        if(i == 0):
            cnt_zero += 1
    for i in win_nums:
        for j in lottos:
            if(i == j):
                cnt_match += 1
                break
    if(cnt_zero + cnt_match < 2):
        answer.append(6)
    else:
        answer.append(7-(cnt_zero+cnt_match))
    tmp = 7 - cnt_match
    if(tmp >= 6):
        tmp = 6
    answer.append(tmp)
    return answer


lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]


print(solution(lottos, win_nums))

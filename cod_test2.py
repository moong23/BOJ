def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if(signs[i] == 1):
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    print(answer)
    return answer


absolutes = [1, 4, 7]
signs = [1, 0, 1]
print(solution(absolutes, signs))

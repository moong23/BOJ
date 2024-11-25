def generate_discounts(current, idx, n, discount, cand):
    if idx == n:
        cand.append(current[:])
        return
    
    for d in discount:
        current[idx] = d
        generate_discounts(current, idx + 1, n, discount, cand)

def solution(users, emoticons):
    n = len(emoticons)
    discount = [10, 20, 30, 40]
    cand = []
    answer = [0, 0]
    
    generate_discounts([0] * n, 0, n, discount, cand)
    
    for disc in cand: 
        cnt = 0
        get = 0
        for i in users:
            pay = 0
            for j in range(len(disc)):
                if i[0] <= disc[j]:
                    pay += emoticons[j] * (100 - disc[j])/100
                if pay >= i[1]:
                    break
            if pay >= i[1]:
                pay = 0
                cnt += 1
            get += pay
        if cnt >= answer[0]: 
            if cnt == answer[0]:
                answer[1] = max(answer[1], get)
            else:
                answer[1] = get
            answer[0] = cnt

    return answer

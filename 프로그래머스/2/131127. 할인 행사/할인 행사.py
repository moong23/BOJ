from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    d1 = {w: n for w, n in zip(want, number)}
    d2 = defaultdict(int)
    
    for i in range(10):
        d2[discount[i]] += 1

    answer = 0
    right = 10

    for product in discount:
        if d1 == d2:
            answer += 1
        if right < len(discount):
            d2[product] -= 1
            d2[discount[right]] += 1
            if d2[product] == 0:
                del d2[product]
        else:
            return answer
        right += 1
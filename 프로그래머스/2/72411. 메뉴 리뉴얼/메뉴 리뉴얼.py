from itertools import combinations

def solution(orders, course):
    answer = []
    answerDict = {i: 0 for i in course}
    
    
    for order in orders:
        for cNum in course:
            print(order, cNum)
            for combo in list(combinations(order, cNum)):
                print(combo)
            
        
    return answer
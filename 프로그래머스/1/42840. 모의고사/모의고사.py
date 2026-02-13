def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    point_a = 0
    point_b = 0
    point_c = 0
    answer = []
    
#     for i, x in enumerate(answers):
#         # i+1, x
#         if (i+1)%5 == x:
#             point_a += 1
#         if(answers[i] == b[i%8]):
#             point_b +=1
#         if(answers[i] == c[i%10]):
#             point_c +=1
            
#     tmp = max(point_a, point_b, point_c)
#     if(tmp == point_a):
#         answer.append(1)
#     if(tmp == point_b):
#         answer.append(2)
#     if(tmp == point_c):
#         answer.append(3)
    

#     return answer
    
    
    for i in range(len(answers)):
        if(answers[i] == a[i%5]):
            point_a +=1
        if(answers[i] == b[i%8]):
            point_b +=1
        if(answers[i] == c[i%10]):
            point_c +=1
            
    tmp = max(point_a, point_b, point_c)
    if(tmp == point_a):
        answer.append(1)
    if(tmp == point_b):
        answer.append(2)
    if(tmp == point_c):
        answer.append(3)
    

    return answer
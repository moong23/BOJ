def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    
    merged = queue1 + queue2
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    
    if (q1_sum + q2_sum) % 2 != 0:
        return -1
    
    target = (q1_sum + q2_sum) // 2
    
    l1, r1 = 0, n - 1
    l2, r2 = n, 2 * n - 1
    
    while answer < 4 * n:
        if q1_sum < target:
            r1 = (r1 + 1) % len(merged)
            l2 = (l2 + 1) % len(merged)
            
            q1_sum += merged[r1]
            q2_sum -= merged[r1]
            
            answer += 1
        
        elif q2_sum < target:
            r2 = (r2 + 1) % len(merged)
            l1 = (l1 + 1) % len(merged)
            
            q2_sum += merged[r2]
            q1_sum -= merged[r2]
            
            answer += 1
        
        if q1_sum == target and q2_sum == target:
            break
    
    return answer if q1_sum == q2_sum else -1

def solution(diffs, times, limit):
    answer = 1
    left = 1
    right = max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        total_time = 0
        time_prev = 0
        for i in range(len(diffs)):
            time_cur = times[i]
            if diffs[i] > mid:
                total_time += (diffs[i] - mid) * (time_cur + time_prev) + time_cur
            else:
                total_time += time_cur
            time_prev = times[i]
        
        if total_time <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
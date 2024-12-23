def solution(fees, records):
    cars = {}
    result = {}
    for record in records:
        temp = record.split(" ")
        if temp[2] == "IN":
            cars[temp[1]] = temp[0]
        else:
            timeIn = cars[temp[1]].split(":")
            del cars[temp[1]]
            timeOut = temp[0].split(":")
            min = (int(timeOut[0]) - int(timeIn[0])) * 60 + int(timeOut[1]) - int(timeIn[1])
            if temp[1] in result:
                result[temp[1]] += min
            else:
                result[temp[1]] = min

    for s in cars:
        timeIn = cars[s].split(":")
        min = (23 - int(timeIn[0])) * 60 + 59 - int(timeIn[1])
        if s in result:
            result[s] += min
        else:
            result[s] = min

    sortKey = sorted(result.keys())
    answer = []
    for key in sortKey:
        totalMin = result[key]
        fee = 0
        if totalMin >= fees[0]:
            totalMin -= fees[0]
            fee = fees[1]
        else:
            totalMin = 0
            fee = fees[1]
        if totalMin > 0:
            if totalMin % fees[2] == 0:
                fee += totalMin // fees[2] * fees[3]
            else:
                fee += (totalMin // fees[2] + 1) * fees[3]
        answer.append(fee)
    return answer

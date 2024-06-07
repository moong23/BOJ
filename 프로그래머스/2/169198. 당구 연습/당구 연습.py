import math 
def solution(m, n, startX, startY, balls):
    answer = []

    def squaredDist(c, d):
        return pow(c-startX, 2) + pow(d-startY, 2)

    def getDist(c, d):
        # print(startX, startY, c, d)
        up = squaredDist(c, -d) if not (startX ==
                                        c and d < startY) else math.inf
        right = squaredDist(2*m-c, d) if not (d ==
                                              startY and c > startX) else math.inf
        down = squaredDist(c, 2*n-d) if not (c ==
                                             startX and d > startY) else math.inf
        left = squaredDist(-c, d) if not (d ==
                                          startY and c < startX) else math.inf
        # print(up, right, down, left)
        return min(up, right, down, left)

    for ball in balls:
        answer.append(getDist(ball[0], ball[1]))

    return answer

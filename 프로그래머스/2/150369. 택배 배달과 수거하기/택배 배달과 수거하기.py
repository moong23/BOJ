def solution(cap, n, deliveries, pickups):
    answer = 0
    target = [n, n]
    while not (target[0] == 0 and target[1] == 0):
        while target[0] >= 1 and deliveries[target[0] - 1] == 0:
            target[0] -= 1
        while target[1] >= 1 and pickups[target[1] - 1] == 0:
            target[1] -= 1

        answer += max(target) * 2

        innerCap = cap
        while innerCap > 0 and target[0] >= 1:
            tmp = min(innerCap, deliveries[target[0] - 1])
            deliveries[target[0] - 1] -= tmp
            innerCap -= tmp
            if deliveries[target[0] - 1] == 0:
                target[0] -= 1

        innerCap = cap
        while innerCap > 0 and target[1] >= 1:
            tmp = min(innerCap, pickups[target[1] - 1])
            pickups[target[1] - 1] -= tmp
            innerCap -= tmp
            if pickups[target[1] - 1] == 0:
                target[1] -= 1

    return answer
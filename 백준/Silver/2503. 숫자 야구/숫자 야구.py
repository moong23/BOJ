# https://www.acmicpc.net/problem/2503
def detect_ball(current, target, strike, ball):
    target = str(target)
    cnt_ball = 0
    cnt_strike = 0

    for i in range(3):
        if current[i] in target:
            cnt_ball += 1
        if current[i] == target[i]:
            cnt_ball -= 1
            cnt_strike += 1

    if strike == cnt_strike and ball == cnt_ball :
        # print(current, cnt_ball, cnt_strike)
        return 1
    return 0



all_ball = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if (i == j or i == k or j == k):
                continue
            tmp = str(100*i + 10*j + k)
            all_ball.append(tmp)
# print(all_ball)
N = int(input())
for _ in range(N):
    num, s, b = map(int, input().split())
    no_list = []
    for cur_ball in all_ball:
        if detect_ball(cur_ball, num, s, b) == 0 :
            no_list.append(cur_ball)
    for x in no_list:
        all_ball.remove(x)

print(len(all_ball))

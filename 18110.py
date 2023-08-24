import sys
input = sys.stdin.readline


def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


N = int(input())

score = []
for _ in range(N):
    score.append(int(input()))


cutCnt = round2(N * 0.15)

score.sort()
score = score[cutCnt: N - cutCnt]
if len(score) == 0:
    print(0)
else:
    print(round2(sum(score)/len(score)))

# https://www.acmicpc.net/problem/1715

N = int(input())
A = dict()
for _ in range(N):
    tmp = int(input())
    if tmp in A:
        A[tmp] += 1
    else:
        A[tmp] = 1
res = 0
prev = 0
for card, _ in sorted(A.items()):
    while A[card] > 1:
        A[card] -= 1
        tmp = card * 2
        res += (card + card)

        print(card, A[card], res)
    if A[card] == 1:
        tmp = prev + card
        
        prev = card
        A[card] -= 1
    elif A[card] == 0:
        prev = 0
        pass
print(res)
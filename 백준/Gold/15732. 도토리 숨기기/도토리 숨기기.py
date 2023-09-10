def box(mid):
    dotori = 0
    for i in range(K):
        A, B, C = ACORN[i][0],ACORN[i][1], ACORN[i][2]
        if A <= mid < B:
            dotori += (mid - A) // C + 1
        elif B <= mid:
            dotori += (B - A) // C + 1
    if dotori >= D:
        return True
    else:
        return False

def check():
    s, e = 1, 10**9
    ans = 0
    while s <= e:
        mid = (s+e)//2
        if box(mid):
            e = mid - 1
            ans = mid
        else:
            s = mid + 1
    return ans


N, K, D = map(int, input().split())
ACORN = []
for _ in range(K):
    ACORN.append((list(map(int, input().split()))))
print(check())
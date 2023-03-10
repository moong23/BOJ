import sys
n, m = map(int, input().split())

s = list(map(int, sys.stdin.readline().split()))

q = [i for i in range(1, n+1)]
cnt = 0

for i in range(m):
    if 2 * q.index(s[i]) < len(q):
        while True:
            if q[0] == s[i]:
                del(q[0])
                break
            else:
                q.append(q[0])
                del(q[0])
                cnt += 1
    else:
        while True:
            if q[0] == s[i]:
                del(q[0])
                break
            else:
                q.insert(0, q[-1])
                del(q[-1])
                cnt += 1
print(cnt)

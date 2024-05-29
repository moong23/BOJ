import sys
input = sys.stdin.readline

X_A, X_B = input().split()

X, A, B = 0, 0, 0
cnt = 0

for i in range(2, 37):
    try:
        aTry = int(X_A, i)
    except ValueError:
        continue
    for j in range(2, 37):
        try:
            bTry = int(X_B, j)
            if aTry == bTry:
                cnt += 1
                if cnt >= 2:
                    print("Multiple")
                    sys.exit(0)
                X = aTry
                A = i
                B = j
        except ValueError:
            continue
if cnt == 0:
    print("Impossible")
print(X, A, B)

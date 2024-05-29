import sys
input = sys.stdin.readline

# import string
# alphaIdx = list(map(str, range(10)))
# alphaIdx.extend(list(string.ascii_lowercase))

X_A, X_B = input().split()

X, A, B = 0, 0, 0
cnt = 0

for i in range(2, 37):
    try:
        aTry = int(X_A, i)
    except ValueError:
        continue
    for j in range(2, 37):
        if i == j:
            continue
        try:
            bTry = int(X_B, j)
            if aTry == bTry:
                cnt += 1
                # print(aTry, i, j)
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
    exit(0)
print(X, A, B)

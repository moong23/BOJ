# https://www.acmicpc.net/problem/17615

N = int(input())

in_str = list(input())
red = in_str.count('R')
blue = N - red
contL, contR = 1, 1
if N == 1:
    print(0)
    exit()

for x in in_str[1:]:
    if x == in_str[0]:
        contL += 1
    else:
        break
for y in in_str[N-2::-1]:
    if y == in_str[N-1]:
        contR += 1
    else:
        break
valL = red - contL if in_str[0] == 'R' else blue - contL
valR = red - contR if in_str[N-1] == 'R' else blue - contR
res = min(red, blue, valL, valR)
print(res)
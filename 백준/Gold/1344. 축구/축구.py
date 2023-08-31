import sys
import math
input = sys.stdin.readline

def prep(num, tp):
    return math.comb(18,num) * ((tp/100)**num)*((1-tp/100)**(18-num))

a=int(input())
b=int(input())
pL = [2,3,5,7,11,13,17]
A,B=0,0
for p in pL:
    A += prep(p, a)
    B += prep(p, b)
print(A+B-A*B)
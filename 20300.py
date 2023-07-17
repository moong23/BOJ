# https://www.acmicpc.net/problem/20300

Num = int(input())

strength = list(map(int, input().split(' ')))

strength.sort()

max_str = -1
# 짝수개면 맨앞 맨뒤
if Num % 2 == 1:
    max_str = strength[-1]
    strength = strength[0:-1]
    

for i in range(len(strength)):
    max_str = max(strength[i] + strength[-1-i], max_str)

print(max_str);
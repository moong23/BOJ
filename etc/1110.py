a = int(input())  # 26
new = a//10 + a % 10
cycle = 1
org = int(a)
a = int(a)
tmp = -1
while org != tmp:
    new = a//10 + a % 10
    tmp = a % 10*10+new % 10
    a = tmp
    cycle += 1
print(cycle-1)

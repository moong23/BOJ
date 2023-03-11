total = int(input())
num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    total -= a * b
if total == 0:
    print('Yes')
else:
    print('No')

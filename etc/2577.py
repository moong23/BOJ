a = int(input())
b = int(input())
c = int(input())
a = list(str(a*b*c))  # a = ['1','7','0','3','7','3','0','0']
for i in range(10):   # [0,1,2,3,4,5,6,7,8,9]
    print(a.count(str(i)))  # print(a.count('0'))


a = int(input())
b = int(input())
c = int(input())
a = list(str(a*b*c))

ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ans = [3, 1, 0, 2, 0, 0, 0, 2, 0, 0]
for i in a:  # a = ['1','7','0','3','7','3','0','0']
    ans[int(i)] += 1

for i in ans:
    print(i)

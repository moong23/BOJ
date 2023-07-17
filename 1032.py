num = int(input())

org_str = list(input())

for _ in range(num-1):
    tmp = input()
    for i in range(len(org_str)):
        if org_str[i] != tmp[i]:
            org_str[i] = '?'

for i in org_str:
    print(i, end='')
print('')

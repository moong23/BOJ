from itertools import combinations

L, C = map(int, input().split())
arr = [i for i in range(C)]
brr = input().split()
brr.sort()
check_list = 'aeiou'
# print(list(combinations(arr, L)))
for x in list(combinations(arr, L)):
    tmp = ''
    cnt = 0
    for j in x:
        tmp += brr[j]
    for char in check_list:
        cnt += tmp.count(char)
    if cnt == 0 or L-cnt < 2:
        # print('here', tmp)
        continue
    else:
        print(tmp)

# print(brr)

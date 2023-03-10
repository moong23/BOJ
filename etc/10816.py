_ = input()
arr = map(int, input().split())
_ = input()
brr = map(int, input().split())

hashmap = {}

for n in arr:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

# print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in brr))
for m in brr:
    if m in hashmap:
        print(hashmap[m], end = ' ')
    else:
        print('0', end = ' ')
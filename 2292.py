# num = int(input())

# plus_idx = 6
# tmp = 1
# ans = []
# while tmp <= 1000000000:
#     ans.append(tmp)
#     tmp += plus_idx
#     plus_idx += 6

# for i in ans:
#     if i >= num:
#         print(ans.index(i)+1)
#         break

num = int(input())

plus_idx = 6
tmp = 1
idx = 1
while tmp <= 1000000000:
    if num <= tmp:
        print(idx)
        break
    else:
        tmp += plus_idx
        idx += 1
        plus_idx += 6


# arr = []

# num = 1
# cnt = 1
# while num < 10000000000:
#     arr.append(num)  # 19
#     num += 6 * cnt  # 37
#     cnt += 1  # 4
# print(arr)

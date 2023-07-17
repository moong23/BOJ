# n, k = map(int, input().split())
# measures = list(map(int, input().split()))

# max_v = -99999999
# for i in range(n - k + 1):
#     sum_v = 0
#     for j in range(k):
#         sum_v += measures[i + j]
#     max_v = max(sum_v, max_v)
# print(max_v)


from collections import deque

d = deque()

for i in range(5):
    d.append(i)

print(d)

d.extend([0, 0, 0])
print(d)

d.extendleft([0, 0])
print(d)

print(d.pop())
print(d)

print(d.popleft())
print(d)

d = list(d)
print(d)

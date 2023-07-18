# https://www.acmicpc.net/problem/13164

N, K = map(int, input().split())
in_list = list(map(int, input().split()))
# print(N, K)
# print(in_list)
diff_list = []
for i in range(1, N):
    diff_list.append(in_list[i] - in_list[i-1])
diff_list.sort(reverse=True)
print(sum(diff_list[K-1:]))

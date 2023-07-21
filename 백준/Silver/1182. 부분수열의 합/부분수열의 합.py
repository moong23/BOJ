import itertools;

N, target = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    # print(list(itertools.combinations(range(N), i+1)))
    for testcse in list(itertools.combinations(range(N), i+1)):
        sum = 0
        for i in testcse:
            # print(i)
            sum += arr[i]

        if sum == target:
            cnt += 1
        # print('----')
print(cnt)

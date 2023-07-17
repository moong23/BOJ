# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7

#arr = [0,2,2,2,1,2,0,1,0,0,0,...]

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

num = int(input())
arr = [0] * 10001
for _ in range(num):
    arr[int(input())] += 1

for i in range(10001):  # i =1  / arr[i] = 2
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

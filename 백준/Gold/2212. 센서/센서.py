N = int(input())
K = int(input())

sensor = list(map(int, input().split()))

sensor.sort()

diff = []
for i in range(N-1):
    diff.append(sensor[i+1] - sensor[i])
diff.sort(reverse=True)
# print(diff)
print(sum(diff[K-1:]))
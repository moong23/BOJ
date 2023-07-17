# https://www.acmicpc.net/problem/2309

tall = []
for _ in range(9):
    tall.append(int(input()))

total = sum(tall)
target = total - 100
# print(total, target)

for i in range(8):
    for j in range(i+1, 9):
        # print(tall[i], tall[j])
        if tall[i] + tall[j] == target:
            tall.remove(tall[i])
            tall.remove(tall[j-1])
            tall.sort()
            # print(sum(tall))
            for i in tall:
                print(i)
            exit()
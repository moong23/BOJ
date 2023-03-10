num = int(input())

points = [map(int, input().split()) for _ in range(num)]

for x in points:
    print(list(x))

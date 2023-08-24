N = int(input())

points = []

for _ in range(N):
    points.append(list(map(int, input().split())))


def ccw(p1, p2, p3):
    return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1]) > 0


points.sort(key=lambda x: (x[0], x[1]))


def convex_hull(points):
    convex = []
    for p3 in points:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
    return len(convex)


print(convex_hull(points) + convex_hull(points[::-1]) - 2)

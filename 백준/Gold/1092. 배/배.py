import sys
input = sys.stdin.readline

N = int(input())

cranes = list(map(int, input().split()))
cranes.sort(reverse=True)
M = int(input())

boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if cranes[0] < boxes[0] :
    print(-1)
    exit()

# print(cranes)
# print(boxes)

cnt = 0;
while boxes:
    if not boxes:
        break
    cnt += 1
    for crane in cranes:
        for box in boxes:
            if box <= crane:
                boxes.remove(box)
                # print(boxes, crane, cnt)
                break

print(cnt)
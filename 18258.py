import sys
input = sys.stdin.readline

testCase = int(input())
queue = []
cnt = 0
for i in range(testCase):
    comm = input().strip()
    if comm.split()[0] == 'push':
        queue.append(int(comm.split()[1]))
    elif comm.split()[0] == 'pop':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1

    elif comm.split()[0] == 'size':
        print(len(queue)-cnt)
    elif comm.split()[0] == 'empty':
        if len(queue)-cnt == 0:
            print(1)
        else:
            print(0)
    elif comm.split()[0] == 'front':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
    elif comm.split()[0] == 'back':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[-1])

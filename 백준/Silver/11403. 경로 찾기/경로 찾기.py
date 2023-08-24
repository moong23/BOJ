N = int(input())

graph = {key: [] for key in range(N)}

for i in range(N):
    for j, x in enumerate(list(map(int, input().split()))):
        if x == 1:
            if graph.get(i):
                graph[i].append(j)
            else:
                graph[i] = [j]

comp = dict()

while graph != comp:
    comp = graph
    for idx, targets in graph.items():
        for target in targets:
            tmp = graph[target]
            for x in tmp:
                if x not in graph[idx]:
                    graph[idx].append(x)

for key in graph.keys():
    for i in range(N):
        if i in graph[key]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print('')

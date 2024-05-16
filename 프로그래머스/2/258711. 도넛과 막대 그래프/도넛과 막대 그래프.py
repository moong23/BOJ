def solution(edges):
    def count_edges(edges):
        graph = {}
        for a, b in edges:
            if not graph.get(a):
                graph[a] = [0, 0]
            if not graph.get(b):
                graph[b] = [0, 0]

            graph[a][0] += 1
            graph[b][1] += 1
        return graph

    graph = count_edges(edges)
    answer = [0, 0, 0, 0]
    for key, counts in graph.items():
        if counts[0] >= 2 and counts[1] == 0:
            answer[0] = key
        elif counts[0] == 0 and counts[1] > 0:
            answer[2] += 1
        elif counts[0] >= 2 and counts[1] >= 2:
            answer[3] += 1
    answer[1] = (graph[answer[0]][0] - answer[2] - answer[3])

    return answer
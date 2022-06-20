def dfs(node, res, graph, color):

    if color[node] == 'BLACK':
        return res

    neighbors = graph[node]
    for n in neighbors:
        res = dfs(n, res, graph, color)

    color[node] = 'BLACK'
    res.append(node)

    return res


def topological_sort(graph):

    color = {}
    for node in graph:
        color[node] = 'WHITE'

    res = []
    for node in graph:
        res = dfs(node, res, graph, color)

    return res


d_graph = {
    1: [2, 8],
    2: [3, 8],
    3: [6],
    4: [3, 5],
    5: [6],
    6: [],
    7: [8],
    8: [],
    9: []
}

res = topological_sort(d_graph)
print(res)

def dfs_graph(node, res: list, graph: dict, color: dict) -> list:

    if color[node] == 'BLACK':
        return res

    neighbors = graph[node]
    for n in neighbors:
        res = dfs_graph(n, res, graph, color)

    color[node] = 'BLACK'
    res.append(node)

    return res


def topological_sort(graph: dict) -> list:

    color = {}
    for node in graph:
        color[node] = 'WHITE'

    res = []
    for node in graph:
        res = dfs_graph(node, res, graph, color)

    return res


graph = {
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

res = topological_sort(graph)
print(res)

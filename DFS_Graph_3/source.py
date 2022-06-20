def dfs_visit(node, graph: dict, color: dict):

    if color[node] == 'BLACK':
        return

    neighbors = graph[node]
    for n in neighbors:
        dfs_visit(n, graph, color)

    color[node] = 'BLACK'
    print(node)

    return


def dfs(graph: dict):

    color = {}
    for node in graph:
        color[node] = 'WHITE'

    for node in graph:
        dfs_visit(node, graph, color)

    return


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

dfs(graph)

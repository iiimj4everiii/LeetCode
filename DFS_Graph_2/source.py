def dfs_graph(graph):

    def dfs_visit(node, res, graph, color):

        if color[node] == 'BLACK':
            return res

        neighbors = graph[node]
        for n in neighbors:
            dfs_visit(n, res, graph, color)

        color[node] = 'BLACK'
        res.append(node)

        return res

    # Initialize all the graph nodes to WHITE color (not processed)
    color = {}
    for node in graph:
        color[node] = 'WHITE'

    res = []
    for node in graph:
        res = dfs_visit(node, res, graph, color)

    return res


graph_adj_list = {
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

res = dfs_graph(graph_adj_list)
print(res)

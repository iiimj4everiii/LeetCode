def dfs_graph(graph_adj_list):

    def dfs_visit(graph_adj_list, color, node):

        # BLACK = 2
        if color[node] == 2:
            return

        neighbors = graph_adj_list[node]
        for n in neighbors:
            dfs_visit(graph_adj_list, color, n)

        # Color the node BLACK
        color[node] = 2
        print(node)
        
        pass

    color = {}
    # Initialize the color of all the nodes to WHITE = 0
    for node in graph_adj_list:
        color[node] = 0

    for node in graph_adj_list:
        dfs_visit(graph_adj_list, color, node)

    pass


graph_adj_list = {
    1:  [2,8],
    2:  [3,8],
    3:  [6],
    4:  [3,5],
    5:  [6],
    6:  [],
    7:  [8],
    8:  [],
    9:  []
}

print(dfs_graph(graph_adj_list))

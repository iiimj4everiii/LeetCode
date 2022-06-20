def topological_sort(d_graph, graph_color):

    # DFS on a graph (recursive):
    # 1) Check termination condition: If node is has been visited, just
    #    return the current res:list
    # 2) Otherwise, recursively visit each neighbor (if any) using dfs.
    # 3) When all the neighbors (dependencies) are visited, we can mark
    #    off the current node as visited as well. Append it to the result.

    def dfs(node, res, d_graph, graph_color):

        color = graph_color[node]
        # Check if the color is black = visited.
        # If it is, just return the current result.
        if color == 2:
            return res

        # At this point, we know that node is unvisited. Get its' neighbors
        # and use dfs to visit each neighbor.

        # If there are no neighbors, we skip this step and go straight to
        # coloring the node as visited and append it to the result.
        neighbors = d_graph[node]
        for n in neighbors:
            res = dfs(n, res, d_graph, graph_color)

        # At this point, all the neighbors of node has been visited. Color it
        # black and append it to res. Then return the updated res.
        graph_color[node] = 2
        res.append(node)

        return res

    # For topological sort on a graph, we need to go through all the
    # nodes in the graph and do dfs on them.
    res = []
    for node in d_graph:
        res = dfs(node, res, d_graph, graph_color)

    return res


d_graph = {
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

# In order to keep track of the nodes visited during dfs, we have
# a memo to keep track of the "color" of the graph nodes. If a node
# is white, it is unvisited. If it is black, it has been visited.

# Initialize all the graph nodes to white.
# 0 = White, 1 = Gray, 2 = Black
graph_color = {
    0:  0,
    1:  0,
    2:  0,
    3:  0,
    4:  0,
    5:  0,
    6:  0,
    7:  0,
    8:  0,
    9:  0
}

result = topological_sort(d_graph, graph_color)
print(result)

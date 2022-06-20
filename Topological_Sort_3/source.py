class GNode:
    def __init__(self, val, color='WHITE'):
        self.val = val
        self.color = color


def dfs_graph(node: GNode, res: list, graph: dict):

    if node.color == 'BLACK':
        return res

    neighbors = graph[node]
    for n in neighbors:
        res = dfs_graph(n, res, graph)

    node.color = 'BLACK'
    res.append(node.val)

    return res


def topological_sort(graph: dict):

    res = []
    for node in graph:
        res = dfs_graph(node, res, graph)

    return res


node1 = GNode(1)
node2 = GNode(2)
node3 = GNode(3)
node4 = GNode(4)
node5 = GNode(5)
node6 = GNode(6)
node7 = GNode(7)
node8 = GNode(8)
node9 = GNode(9)

d_graph = {
    node1: [node2, node8],
    node2: [node3, node8],
    node3: [node6],
    node4: [node3, node5],
    node5: [node6],
    node6: [],
    node7: [node8],
    node8: [],
    node9: []
}

res = topological_sort(d_graph)
print(res)

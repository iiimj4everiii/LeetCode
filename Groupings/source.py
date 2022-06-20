def intersects(set_a:set, set_b:set):
    if len(set_a.intersection(set_b)) > 0:
        return True
    return False

d = {
    'pretty':       {1},
    'beautiful':    {2, 4},
    'gorgeous':     {1, 4},
    'great':        {3},
    'stunning':     {2, 3}
}

# Adjacency List
# 1: 4
# 2: 3, 4
# 3: 2
# 4: 1, 2

# Get all the graph nodes {1, 2, 3, 4} from dictionary d
s = set()
for key in d:
    for x in d[key]:
        s.add(x)

# Create an adjacency list template using those graph nodes
graph = dict()
for element in s:
    graph[element] = set()

# Create adjacency list. Notice that we have each node has itself as an element of its own adjacency list.
# We will clean those up in the next step
for key in d:
    nodes = d[key]
    for n in nodes:
        graph[n] = graph[n].union(nodes)

# Cleaning up the adjacency list by removing the node from the adjacency list that is the node itself.
for n in graph:
    graph[n].remove(n)

# Now we have an adjacency list


# DFS to find if 2 nodes belong to the same set.
def dfs(graph, current_node, visited:set, node_a, node_b):

    if current_node in visited:
        return False

    visited.add(current_node)
    if node_a in visited and node_b in visited:
        return True

    adj_list = graph[current_node]
    for adj in adj_list:
        if dfs(graph, adj, visited, node_a, node_b):
            return True

    return False


visited = set()
print(dfs(graph, 1, visited, 1, 3))

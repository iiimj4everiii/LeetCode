class GraphNode:
    def __init__(self, val):
        self.edges = []
        self.color = 0  # 0 = white, 1 = gray, 2 = black
        self.val = val


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list) -> list:

        # CLS algorithm for dfs_visit, modified for this problem.
        # res, initially empty, contains the latest topologically
        # sorted sub_graph.
        def dfs_visit(u, res):

            # Dye the current node u gray.
            u.color = 1

            # Expand and explore the direct neighbors of u.
            for v in u.edges:

                # We will either encounter an unexplored white node, a
                # in-path gray node, or a previously explored black node.

                # 1) If the neighbor is dyed white,
                if v.color == 0:

                    # recursively explore it.
                    dfs_visit(v, res)

                    # We expect at least 1 node in res after exploration.
                    # If res is empty, that means we encountered a cycle
                    # somewhere deeper in the graph. In that case, we
                    # return.
                    if len(res) == 0:
                        return

                # 2) If the neighbor is dyed gray, that means we have
                #    found a node that we encountered before in the same
                #    path. This means we detected a cycle in the graph.
                elif v.color == 1:

                    # Clear res. This is a flag to the caller that there
                    # exists a cycle in the graph. Then return.
                    res.clear()
                    return

                # 3) If the neighbor is dyed black, this node has been
                #    explored in-depth before. No need to explore it.
                #    Therefore, we simply ignore it.

            # At this point, we finished exploring all the direct neighbors
            # of u. We finish u by dying it black and append it to res
            u.color = 2
            res.append(u.val)

        # CLS algorithm for Topological sort (a modified dfs)
        # Topological sort. Since we know there is at least 1 node, we
        # can use an empty list as a flag for cycle detection.
        def topological_sort(Graph) -> list:

            # Initialize res to an empty list.
            res = []

            # Explore all the vertices in Graph.
            for g in Graph:

                # Only explore the unexplored nodes in Graph.
                if g.color == 0:

                    # We will use dfs_visit to explore Graph.
                    dfs_visit(g, res)

                    # We expect at least 1 node in res after dfs_visit.
                    # If res is empty, that means we encountered a cycle
                    # somewhere deeper in the graph. In that case, we
                    # return an empty list [].
                    if len(res) == 0:
                        return res

            return res

        # Create numCourse number of vertices each initialized with
        # GraphNodes.
        Graph = [GraphNode(c) for c in range(numCourses)]

        # Create a graph by making appropriate connections:
        # by making a pointer from course to its' prereqs.
        for pr in prerequisites:
            parent = pr[1]
            child = pr[0]

            p_node = Graph[parent]
            c_node = Graph[child]
            c_node.edges.append(p_node)

        # Do topographical sort.
        return topological_sort(Graph)


pr = [[1,0],[2,0],[3,1],[3,2]]
sol = Solution().findOrder(4, pr)
print(sol)
pr = [[1, 0]]
sol = Solution().findOrder(2, pr)
print(sol)
pr = [[1, 0], [0, 1]]
sol = Solution().findOrder(2, pr)
print(sol)
pr = [[0,2],[1,2],[2,0]]
sol = Solution().findOrder(3, pr)
print(sol)

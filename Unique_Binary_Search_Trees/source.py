class Solution:
    def numTrees(self, n: int) -> int:

        # Strategy:
        # This problem can be solved using dynamic programming. The number of
        # different trees that can be created with n number of nodes is the sum of:
        #   the number of different trees that can be created if we choose the first
        #   node as the root node +
        #   the number of different trees that can be created if we choose the second
        #   node as the root node + ... +
        #   the number of different trees that can be created if we choose the nth/last
        #   node as the root node.
        # Notice that the number of different trees that can be created if we choose
        # the kth node as the root node is the product of the number of different trees
        # that can be created with (k-1) nodes and the number of different trees that
        # can be created with (n-k) nodes: numTrees[k] = numTrees[k-1] * numTrees[n-k]
        # for all k from 1 to n.

        # Initialize our dynamic programming table to (n + 1) size of 1's.
        table = [1] * (n + 1)

        # Generate the our dynamic programming table from 0 to n.
        for node_count in range(2, n + 1):
            number_of_trees = 0
            for root_pos in range(1, node_count + 1):
                l_subtree_node_ct = root_pos - 1
                r_subtree_node_ct = node_count - root_pos
                number_of_trees += table[l_subtree_node_ct] * table[r_subtree_node_ct]

            table[node_count] = number_of_trees

        return table[n]


sol = Solution().numTrees(5)
print(sol)

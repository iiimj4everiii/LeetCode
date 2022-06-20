class Solution:
    def diffWaysToCompute(self, expression: str) -> list:

        # Parse the string expression into a list of numbers and
        # a list of operators.
        nums, ops = self.str_exp_to_lists(expression)

        # Call the dfs method to get the result: ways to "add
        # parentheses" and calculate the resulting expression.
        return self.dfs(nums, ops, 0, len(ops)-1)

    # Method to convert string expression s to a linked list of
    # alternating number nodes and operator nodes.
    @staticmethod
    def str_exp_to_lists(s):

        nums = [0]
        ops = []

        is_prev_num = True
        for si in s:

            if is_prev_num:
                if si.isnumeric():
                    nums[-1] = nums[-1] * 10 + int(si)
                else:
                    ops.append(si)
                    is_prev_num = False
            else:
                nums.append(int(si))
                is_prev_num = True

        return nums, ops

    # This is our main method to get the result based on various
    # parentheses placement. The structure of this algorithm is
    # similar to the problem: Unique_Binary_Search_Trees_2. This
    # is because we can think about different placement of
    # parentheses or giving different priority to different parts
    # of the expression as different heights in a binary tree.
    #                              -
    #                             / \
    #                            *   5
    #                           / \
    # (2 * (3 + 4)) - 5   =>   2   +
    #                             / \
    #                            3   4
    def dfs(self, nums, ops, start, stop):

        # Base case 1: if the starting index is to the right of
        # the stopping index, we return the value in the starting
        # index.
        if start > stop:
            return [nums[start]]

        # Base case 2: if the starting index is the same as the
        # stopping index. We return the result of operation on:
        # nums[start] <ops[start]> nums[start+1].
        if start == stop:
            num1 = nums[start]
            num2 = nums[start+1]
            operator = ops[start]
            return [self.calculate(num1, num2, operator)]

        # Create a list to hold all the possible results from placing
        # parentheses in different locations. We will call our list
        # tree to refer to the same variable name in the problem:
        # Unique_Binary_Search_Trees_2.
        trees = []

        # Go through all the operators in ops and these operators
        # are the root node at this level. Notice that the operations
        # at the root node is done last, while the operations toward
        # the bottom of the tree are done first.
        for root_pos in range(start, stop+1):

            # Get the left_subtree = all the possible results on the
            # left hand side.
            left_subtrees = self.dfs(nums, ops, start, root_pos-1)

            # Get the right_subtree = all the possible results on the
            # right hand side.
            right_subtrees = self.dfs(nums, ops, root_pos+1, stop)

            # For each possible result from the left_subtree and for
            # each possible result from the right_subtree,
            for left in left_subtrees:
                for right in right_subtrees:

                    # perform the root's operator on them.
                    root = self.calculate(left, right, ops[root_pos])

                    # Add that result to trees (at this level)
                    trees.append(root)

        return trees

    # Do math on num1 and num2 based on the operator.
    @staticmethod
    def calculate(num1, num2, operator):

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        else:
            return num1 * num2


sol = Solution().diffWaysToCompute("2-1-1")
print(sol)


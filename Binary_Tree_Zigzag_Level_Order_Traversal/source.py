# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root) -> list:

        # Strategy:
        # A slightly modified version of solution to the previous problem:
        # Binary_Tree_Level_Order_Traversal. The only extra step we need
        # to take is:
        # 1) If we are currently on an even level, append sol_at_level
        #    directly to solution
        # 2) Otherwise, append the inverted sol_at_Level to solution. We
        #    can speed it up if we can get around inverting the lists as
        #    they are time consuming operations. We may be able to speed
        #    things up if we can use a stack and queue to hold our
        #    sol_at_level for zig zagging.

        # Homemade Queue data structure.
        class Queue:

            # Using a linked list as our the backbone of our queue
            # data structure.
            class ListNode:
                def __init__(self, val=0, next=None):
                    self.val = val
                    self.next = next

            head = None
            tail = None

            def __init__(self):
                self.head = None
                self.tail = None

            # Enqueue entails to chaining the new node to the back
            # of the linked list. We will keep a point tail to point
            # to the last node in the linked list.
            def enqueue(self, val):

                new_node = self.ListNode(val)
                if self.head is None:
                    self.head = new_node
                    self.tail = self.head
                else:
                    self.tail.next = new_node
                    self.tail = self.tail.next

                return None

            # Dequeue entails returning the head node and move the
            # head node down the linked list once.
            def dequeue(self):
                if self.head is not None:
                    return_head = self.head
                    self.head = self.head.next
                    return return_head.val

            # If head node is None, then the linked list and our queue
            # will be empty
            def empty(self):
                if self.head is None:
                    return True
                return False

        # Handling the corner cases.
        if root is None:
            return []

        # Initialize solution to an empty list. This will be the
        # solution to our problem.
        solution = []

        # Initialize our queue data structure and enqueue the root node.
        q = Queue()
        q.enqueue(root)

        # At this point, we have at least 1 node to process. We will
        # increase this number by a factor of 2 after processing all
        # the nodes at the current level. num_nodes represent the max
        # number of nodes that can exist at the current level in a
        # binary tree.
        num_nodes = 1

        # We will use less_nodes to offset any nodes that cannot have
        # left and right children (NoneType/leaf nodes) in the next
        # tree level.
        less_nodes = 0

        # Level-order tree traversal: pop front of the queue and push
        # the children of the node to the back of the queue. We keep
        # doing this as long as our queue is not empty.
        while not q.empty():

            # Create an empty list to hold all the node values in a
            # a particular level.
            sol_at_level = []

            # Maximum possible nodes in this level less the number of
            # missing children belonging to NoneType parents.
            num_nodes -= less_nodes

            # Reset less_nodes to 0.
            less_nodes = 0

            # Process all the nodes in the current tree level.
            i = 0
            while i < num_nodes:

                # Pop front of the queue.
                curr_node = q.dequeue()

                # If curr_node is NoneType, increase the missing
                # children count by 2 for the next tree level.
                if curr_node is None:
                    less_nodes += 2

                # Otherwise, we push curr_node's children to our queue
                # and append curr_node's value to sol_at_level.
                else:
                    q.enqueue(curr_node.left)
                    q.enqueue(curr_node.right)
                    sol_at_level.append(curr_node.val)

                # Go to the next node in the queue.
                i += 1

            # Only add to solution list if sol_at_level is nonempty.
            # If sol_at_level is empty, then we are at the deepest
            # leaf nodes level.
            if len(sol_at_level) > 0:
                if len(solution) % 2 == 0:
                    solution.append(sol_at_level)
                else:
                    solution.append(sol_at_level[::-1])

            # Increase the maximum possible nodes in the next tree
            # level by a factor of 2.
            num_nodes *= 2

        return solution


r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)
# r = TreeNode(1)
# r.left = TreeNode(2)
# r.right = TreeNode(3)
# r.left.left = TreeNode(4)
# r.right.right = TreeNode(5)

sol = Solution().zigzagLevelOrder(r)
print(sol)

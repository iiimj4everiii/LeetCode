# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    # def connect(self, root):
    #
    #     def populate_next_right_pointer(l_root, r_root):
    #
    #         if l_root is None:
    #             return
    #
    #         l_root.next = r_root
    #
    #         populate_next_right_pointer(l_root.left, l_root.right)
    #
    #         populate_next_right_pointer(l_root.right, r_root.left)
    #
    #         populate_next_right_pointer(r_root.left, r_root.right)
    #
    #         return None
    #
    #     if root is not None:
    #         populate_next_right_pointer(root.left, root.right)
    #
    #     return root

    def connect(self, root):

        # Problem:
        # You are given a perfect binary tree where all leaves are on the
        # same level, and every parent has two children. The binary tree has
        # the following definition:

        # Strategy:
        # Since we are making connections across the entire level but not
        # in-between levels, it will be advantageous for us to group the
        # connection making process one level at a time. One way to process
        # a level at a time will be level-order traversal. We commonly use
        # a queue to help us accomplish this traversal pattern. We grab the
        # first node from each level and make a connection to the second
        # node. And from second node to the third node and etc. After we are
        # done making all these connections at the current level, we move onto
        # the next level, grab the first node from that level, make connections
        # across this level, move onto the next level and etc.

        class Queue:

            head = None
            tail = None

            class ListNode:
                def __init__(self, val=0, next=None):
                    self.val = val
                    self.next = next

            def __init__(self, val=None):
                self.head = self.ListNode(val)
                self.tail = self.head

            def enqueue(self, val):
                if self.head is None:
                    self.__init__(val)
                else:
                    self.tail.next = self.ListNode(val)
                    self.tail = self.tail.next

            def dequeue(self):
                val = self.head.val
                self.head = self.head.next

                if self.head is None:
                    self.tail = None

                return val

            def empty(self):
                return self.head is None

        # Handling the corner cases.
        if root is None:
            return None

        # Initialize Queue with root.
        q = Queue(root)

        # Take the first node out of the queue.
        left_node = q.dequeue()

        # Initialize max number of nodes at the first level to 1.
        level_max_nodes = 1

        # We keep on processing until we get to a nullptr. Since our binary
        # tree is perfectly balanced, reaching a nullptr means we processed
        # all the nodes in the last level.
        while left_node is not None:

            # Enqueue the children of left_node to the queue.
            q.enqueue(left_node.left)
            q.enqueue(left_node.right)

            # Since we know the tree is perfectly balanced, we know that the
            # number of nodes at each level is level_max_nodes = 2^level.
            # Since we know that we need to make level_max_nodes-1 connections,
            # we only need to loop level_max_connections-1 times.
            for _ in range(level_max_nodes-1):

                # Dequeue the right node that will be pointed to from left_node.
                right_node = q.dequeue()

                # Immediately enqueue its children to the queue.
                q.enqueue(right_node.left)
                q.enqueue(right_node.right)

                # Point left_node.next to right_node.
                left_node.next = right_node

                # right_node becomes the new left_node.
                left_node = right_node

            # Increase level_max_nodes by a factor of 2 because we are going to
            # the next leve below.
            level_max_nodes *= 2

            # Extract the first node on the next level below.
            left_node = q.dequeue()

        return root


r = Node(1)

r.left = Node(2)
r.right = Node(3)

r.left.left = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)
r.right.right = Node(7)

r.left.left.left = Node(8)
r.left.left.right = Node(9)
r.left.right.left = Node(10)
r.left.right.right = Node(11)
r.right.left.left = Node(12)
r.right.left.right = Node(13)
r.right.right.left = Node(14)
r.right.right.right = Node(15)

sol = Solution().connect(r)
print()

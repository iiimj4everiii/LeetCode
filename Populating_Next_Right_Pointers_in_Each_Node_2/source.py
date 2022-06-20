# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):

        # Problem:
        # Given a binary tree, populate each next pointer to point to its
        # next right node. If there is no next right node, the next pointer
        # should be set to NULL.

        # Strategy: (Similar to previous problem:
        # Populating_Next_Right_Pointers_in_Each_Node plus some modifications)
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

        # Initialize next level's node count to 1.
        next_level_node_count = 1

        # We keep on processing until our queue is empty. A common way
        # to do level-order traversal.
        while not q.empty():

            # Get the node count at this level is equal the number of nodes
            # non-NoneType nodes queued from the previous level.
            node_count = next_level_node_count

            # Reset the next level node count to 0.
            next_level_node_count = 0

            # Take the first node out of the queue.
            left_node = q.dequeue()

            # Enqueue the children of left_node to the queue if they are not
            # nullptr and add 1 to next_level_node_count for every child
            # enqueued onto q.
            if left_node.left is not None:
                q.enqueue(left_node.left)
                next_level_node_count += 1

            if left_node.right is not None:
                q.enqueue(left_node.right)
                next_level_node_count += 1

            # We will make node_count-1 connections at this level.
            for _ in range(node_count-1):

                # Dequeue the right node that will be pointed to from left_node.
                right_node = q.dequeue()

                # Similar to left_node, we immediately enqueue its children to
                # the queue if they are not nullptr. Then add 1 to
                # next_level_node_count for every child enqueued onto q.
                if right_node.left is not None:
                    q.enqueue(right_node.left)
                    next_level_node_count += 1

                if right_node.right is not None:
                    q.enqueue(right_node.right)
                    next_level_node_count += 1

                # Point left_node.next to right_node.
                left_node.next = right_node

                # right_node becomes the new left_node.
                left_node = right_node

        return root


r = Node(1)

r.left = Node(2)
r.right = Node(3)

r.left.left = Node(4)
r.left.right = Node(5)
r.right.right = Node(7)

# r = Node(1)
# r.left = Node(2)
# r.left.left = Node(3)
# r.left.left.left = Node(4)
# r.left.left.left.left = Node(5)

sol = Solution().connect(r)

print()

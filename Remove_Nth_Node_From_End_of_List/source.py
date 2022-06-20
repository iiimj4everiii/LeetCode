# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Strategy:
        # Use a FIFO queue to keep track of the linked list traversal history.
        # The size of the queue needs to be big enough to keep track of the
        # node that is to be deleted (nth node from the end in our case).
        # Keep on traversing until we get to nullptr. At that point, we delete
        # the node that can be found in our queue. If we set the queue size to be n,
        # then the first element of the queue holds our to-be-deleted node.
        # We will also keep track of this node's parent in order to stitch
        # the linked list together after removing the node.

        # Create a stack that holds the traversal history up to the nth node from the end.
        n_node_queue = [ListNode(0)] * n

        # Fill n_node_queue with the first n nodes of the linked list.
        curr_node = head
        for i in range(n):
            n_node_queue[i] = curr_node
            curr_node = curr_node.next

        # If the current node happens to be nullptr, then we know that n == number of nodes in the linked list.
        # Remove the head node by returning head.next
        if curr_node is None:
            return head.next

        # Otherwise, traverse through the linked list until we are at nullptr.
        # At this point, the first element in n_node_queue holds the node to be deleted
        # The prev_node is the parent of the to-be-deleted node.
        prev_node = head
        while curr_node is not None:
            prev_node = n_node_queue.pop(0)
            n_node_queue.append(curr_node)
            curr_node = curr_node.next

        # Therefore, we point prev_node.next to the child of the to-be-deleted node.
        prev_node.next = n_node_queue[0].next

        return head


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

h = Solution().removeNthFromEnd(h, 1)

print()
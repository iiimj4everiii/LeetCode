# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode):

        # Strategy:
        # Use a pointer to hold the previous node for stitching purpose.
        # Use a temp point to hold the curr_node (1st position).
        # Set curr_node to its next node. curr_node is in the (2nd position).
        # Point from the (1st position) to the (3rd position)
        # Point from the (2nd position) to the (1st position)
        # At this point, we should have (2nd pos) -> (1st pos) -> (3rd pos)
        # If there is a valid prev_node, point from that to the (2nd pos)
        # Then we have (0th pos) -> (2nd pos) -> (1st pos) -> (3rd pos).
        # 1st and 2nd pos swaps while 0th and 3rd pos stays the same.
        # The craw to the next set of pairs.

        # Handling corner case 1: when head is a nullptr
        if head is None:
            return head

        # Handling corner case 2: when head is the only node in the linked list
        if head.next is None:
            return head

        # Use curr_node to craw through the linked list
        curr_node = head

        # Initialize prev_node to something random
        prev_node = None

        # Save the pointer to the head of the pair swapped list. At this point, we know
        # that we have at least 2 nodes in the linked list. Therefore, the node after the head node
        # will become the new head node.
        head = head.next

        while curr_node is not None and curr_node.next is not None:
            # Swapping curr_node and curr_node.next.
            temp = curr_node
            curr_node = curr_node.next
            temp.next = curr_node.next
            curr_node.next = temp

            # Then stitch the prev_node to the newly swapped curr_node. Since there is nothing
            # before the head node, we only do this when curr_node is not the head node.
            if curr_node is not head:
                prev_node.next = curr_node

            # Craw down to the next pair
            prev_node = curr_node.next
            curr_node = curr_node.next.next

        return head


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
h.next.next.next.next.next = ListNode(6)

head2 = Solution().swapPairs(h)

print()

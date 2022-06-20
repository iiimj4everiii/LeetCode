# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # Handling corner cases 1: if head is nullptr, then simple
        # return nullptr back.
        if head is None:
            return None

        # Count number of nodes in the linked list.
        list_len = 1
        curr_node = head
        while curr_node.next is not None:
            list_len += 1
            curr_node = curr_node.next

        # Save the last node for future use.
        last_node = curr_node

        # Simplify the rotation count by taking the mod of the linked
        # list length.
        k = k % list_len

        # Handling corner cases 2: if the simplified k is 0, then we
        # don't need to do any rotation. Simply return head back.
        if k == 0:
            return head

        # Otherwise, we find the node right before the new head node.
        # Notice that this is (list_len-k-1) nodes away from the
        # beginning. We will use curr_node as a traversal node.
        curr_node = head
        for _ in range(list_len - k - 1):
            curr_node = curr_node.next

        # Once we get there, assign curr_node.next to our new_head node.
        # And curr_node.next should be redirected to point to None since
        # it is now the new last node of the linked list.
        new_head = curr_node.next
        curr_node.next = None

        # Finally, we redirect the next node from the original last node
        # last_node to point to the original head. Thus, we result in a
        # rotation of the original linked list k times to the right.
        last_node.next = head

        return new_head


h = ListNode(1)
h.next = ListNode(2)

sol = Solution().rotateRight(h, 1)
print()

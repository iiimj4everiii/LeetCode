# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int):

        # Removing the preceding nodes with ListNode.val == val by pushing the head node
        # down the linked list
        while head is not None and head.val == val:
            head = head.next

        # Handling the corner cases: If head is None, we will return it.
        if head is not None:

            # At this point, the head node's val is not equal to val
            # We will start keeping track of the previous node prev_node so that we can remove
            # current node curr_node from the list by pointing prev_node.next to curr_node.next
            prev_node = head
            curr_node = head.next
            while curr_node is not None:

                # If we encounter curr_node.val == val,
                # we remove it by pointing prev_node.next to head.next
                if curr_node.val == val:
                    prev_node.next = curr_node.next

                # Otherwise, we keep traversing down until we reach None
                # while updating the prev_node
                else:
                    prev_node = curr_node

                # Continue to traverse down the linked list
                curr_node = curr_node.next

        return head


root = ListNode(6)
root.next = ListNode(6)
root.next.next = ListNode(6)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(4)
root.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next = ListNode(6)
new_root = Solution().removeElements(root, 6)

print()

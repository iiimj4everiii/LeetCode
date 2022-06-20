# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Strategy:
        # curr_node is the node we are currently looking at
        # Save the future node: next_node = curr_node.next
        # Save the past node: prev_node
        # Flip the node curr_node.next points to (next_node)
        # and flip it around to point to prev_node
        # Advance both prev_node to curr_node
        # and curr_node to next_node

        # Initialize prev_node and curr_node
        prev_node = None
        curr_node = head

        while curr_node is not None:
            # next_node will hold the future node
            next_node = curr_node.next

            # Now, curr_node.next can point towards the opposite direction: prev_node
            curr_node.next = prev_node

            # Progress forward:
            # prev_node advances to curr_node
            prev_node = curr_node

            # curr_node advances to the future node (next_node)
            curr_node = next_node

        # At this point, curr_node is None
        # and prev_node is the head of the reversed linked list
        return prev_node


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
new_head = Solution().reverseList(head)

print()
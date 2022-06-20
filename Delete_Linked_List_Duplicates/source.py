# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):

        # Handling the corner cases
        if not head:
            return None

        previous = head
        current = head.next
        while current is not None:

            # If duplicate found, redirect previously pointed node to its following node (or current.next)
            if current.val == previous.val:
                previous.next = current.next

            # Otherwise, previous node will take on the current node position
            else:
                previous = current

            # We move current node onward regardless
            current = current.next

        return head


# l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(2)
# l.next.next.next = ListNode(3)
# l.next.next.next.next = ListNode(3)
# l.next.next.next.next.next = ListNode(4)

l = []

print(Solution().deleteDuplicates(l))
print()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # Strategy:
        # We will use a fast and slow node to traverse down the
        # linked list until they meet up. This will take us to
        # a node somewhere in the cycle. We restart slow node's
        # position to the beginning of the linked list: head. Then
        # let it and fast node traverse through the linked list
        # again. However, this time, both nodes will traverse in
        # slow pace. The node where they meet up again will be the
        # first node of the cycle. This can be proven mathematically.

        # Use a slow and fast nodes to traverse down the linked
        # list. If slow and fast node meets up, that means there
        # is a cycle in the linked list. Otherwise, fast node will
        # reach nullptr first. In that case, we return None for
        # no loop.
        slow = head
        fast = head

        # Handling the corner cases.
        if fast is None or fast.next is None:
            return None

        # Keep searching until either fast or fast.next reaches
        # nullptr or fast meet up with slow after going around the
        # cycle at least once.
        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break

        # If fast met up with slow, then we find the first node of
        # cycle.
        if slow is fast:

            # To find the first node of the cycle, we put slow node
            # back to the beginning while leaving fast node where it
            # is: node where fast and slow node met up. We traverse
            # both fast and slow node at a slow pace until they meet
            # up. The node where they meet up again is the first node
            # of the cycle. This can be proven mathematically.
            slow = head
            while slow is not fast:

                # Both fast and slow node traverses at a slow pace.
                slow = slow.next
                fast = fast.next

        # Otherwise, no cycle found. Return None
        else:
            return None

        return slow


h = ListNode(0)
# h.next = ListNode(1)
# h.next.next = ListNode(2)
# h.next.next.next = ListNode(3)
# h.next.next.next.next = ListNode(4)
# h.next.next.next.next.next = ListNode(5)
# h.next.next.next.next.next.next = ListNode(6)
# h.next.next.next.next.next.next.next = ListNode(7)
# h.next.next.next.next.next.next.next.next = ListNode(8)
# h.next.next.next.next.next.next.next.next.next = h.next.next.next
sol = Solution().detectCycle(h)
print()

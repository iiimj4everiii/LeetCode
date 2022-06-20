# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Handling the corner case
        if l1 is None and l2 is None:
            return None

        # The algorithm is analogous to the merge part of a merge sort.
        l3 = ListNode()
        currentNode = l3
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                currentNode.val = l1.val
                l1 = l1.next
            else:
                currentNode.val = l2.val
                l2 = l2.next

            currentNode.next = ListNode()
            currentNode = currentNode.next

        # Copy the rest of the elements over from l1 to l3
        while l1 is not None:
            currentNode.val = l1.val
            l1 = l1.next

            if l1 is not None:
                currentNode.next = ListNode()
                currentNode = currentNode.next

        # Copy the rest of the elements over from l2 to l3
        while l2 is not None:
            currentNode.val = l2.val
            l2 = l2.next

            if l2 is not None:
                currentNode.next = ListNode()
                currentNode = currentNode.next

        return l3


l1 = ListNode(-9)
l1.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(7)

l3 = Solution().mergeTwoLists(l1, l2)

while l3 is not None:
    print(l3.val)
    l3 = l3.next
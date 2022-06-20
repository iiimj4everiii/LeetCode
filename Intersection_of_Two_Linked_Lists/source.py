# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # Keep a history of traversed nodes in headA
        traversed_node_set_A = set()

        # Traverse headA and record the traversed nodes
        while headA is not None:
            traversed_node_set_A.add(headA)
            headA = headA.next

        # Traverse headB and see if these nodes existed in headA's traversal history
        while headB not in traversed_node_set_A and headB is not None:
            headB = headB.next

        return headB


head1 = ListNode(4)
head1.next = ListNode(1)
head1.next.next = ListNode(8)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(1)
head2.next.next.next = head1.next.next

print(Solution().getIntersectionNode(head1, head2).val)

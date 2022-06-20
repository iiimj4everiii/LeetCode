# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        lst = []

        # Copy all the linked list items to a normal python list lst
        while head is not None:
            lst.append(head.val)
            head = head.next

        # Reverse the lst
        lst_reversed = lst[::-1]

        # Check to see if the forward list is the same as the reversed list
        return lst == lst_reversed


h = ListNode(0)
h.next = ListNode(1)
h.next.next = ListNode(1)
print(Solution().isPalindrome(h))

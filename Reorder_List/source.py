# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Initialize stack to an empty list.
        stack = []

        # Initialize traversal node: curr_node to head.
        curr_node = head

        # Push all the nodes to stack as we traverse down the
        # linked list.
        while curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.next

        # Reinitialize curr_node back to head and pop off the
        # top of stack: the last node in the linked list.
        curr_node = head
        top = stack.pop(-1)

        # While curr_node or its next is not top, keep rearranging
        # linked list.
        while curr_node is not top and curr_node.next is not top:

            # Use temp to hold onto curr_node.next node.
            temp = curr_node.next

            # Point curr_node.next to top: the end of linked list.
            curr_node.next = top

            # Point top.next to temp. Effectively squeezing top
            # between curr_node and curr_node.next.
            top.next = temp

            # Move curr_node to temp's position.
            curr_node = temp

            # Pop off stack for the next iteration and point its
            # next node to None.
            top = stack.pop(-1)
            top.next = None

        return


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
Solution().reorderList(h)
print()

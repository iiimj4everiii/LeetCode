# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # Keep a set of all the visited nodes
    list_set = set()

    def hasCycle(self, head: ListNode) -> bool:

        # If we come across a visited node,
        # then we have a cycle in the linked list
        if head in self.list_set:
            return True

        # If we encountered None, then we are at the end of the linked list
        # This means that there are no cycles in the list
        elif head is None:
            return False

        # Otherwise, add the current node to the set
        # and proceed onto the next node down the linked list.
        else:
            self.list_set.add(head)
            return self.hasCycle(head.next)


root = ListNode(0)
root.next = ListNode(1)
root.next.next = ListNode(2)
root.next.next.next = ListNode(3)
root.next.next.next.next = root.next
print(Solution().hasCycle(root))

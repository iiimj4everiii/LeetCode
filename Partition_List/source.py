# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        # Strategy:
        # We will keep track of 2 linked lists:
        # 1) head_list will link all the nodes whose values are less than x.
        # 2) tail_list will link all the other nodes.
        # At the end, we will attach tail_list to the end of head_list. If
        # there are no nodes in head_list, that means all the nodes have
        # equal or larger value than x. In that case, we just return whatever
        # that is in tail_list. We will use curr_head_node and curr_tail_node
        # as our traversal node for head_list and tail list respectively.

        # Initialize the head of head_list and head of tail_list to None.
        head_list = None
        tail_list = None

        # Also initialize their traversal nodes to None as well.
        head_list_trav = None
        tail_list_trav = None

        # Keep traversing down the head list until we are at None.
        while head is not None:

            # If the current head value is less than x,
            if head.val < x:

                # see if there is a node on head_list already. If not, then:
                # 1) Point both head_list and head_list_trav to the current
                #    head node.
                # 2) Advance the current head node to its next node.
                # 3) Disconnect the newly added node from the rest of the head
                #    list by assigning head_list.next to None.
                if head_list is None:
                    head_list = head
                    head_list_trav = head
                    head = head.next
                    head_list.next = None

                # If there is already a node in head_list:
                # 1) Point head_list_trav's next to the current head node.
                # 2) Advance the current head node to its next node.
                # 3) Advance head_list_trav to its next node.
                # 4) Disconnect the newly added node from the rest of the head
                #    list by assigning head_list_trav.next to None.
                else:
                    head_list_trav.next = head
                    head = head.next
                    head_list_trav = head_list_trav.next
                    head_list_trav.next = None

            # If the current head value is equal to or greater than x,
            else:
                # see if there is a node on tail_list already. If not, then:
                # 1) Point both head_list and tail_list_trav to the current
                #    head node.
                # 2) Advance the current head node to its next node.
                # 3) Disconnect the previous head node (assigned to tail_list)
                #    from the rest of the head list by assigning tail_list.next
                #    to None.
                if tail_list is None:
                    tail_list = head
                    tail_list_trav = head
                    head = head.next
                    tail_list.next = None

                # If there is already a node in tail_list:
                # 1) Point tail_list_trav's next to the current head node.
                # 2) Advance the current head node to its next node.
                # 3) Advance tail_list_trav to its next node.
                # 4) Disconnect the newly added node from the rest of the head
                #    list by assigning tail_list_trav.next to None.
                else:
                    tail_list_trav.next = head
                    head = head.next
                    tail_list_trav = tail_list_trav.next
                    tail_list_trav.next = None

        # At the end, we will attach tail_list to the end of head_list. Then
        # head_list is the head of the entire partitioned list.
        if head_list is not None:
            head_list_trav.next = tail_list
            return head_list

        # However, if there are no nodes in head_list, that means all the nodes
        # have equal or larger value than x.In that case, we just return whatever
        # that is in tail_list.
        else:
            return tail_list


h = ListNode(4)
# h.next = ListNode(4)
# h.next.next = ListNode(3)
# h.next.next.next = ListNode(2)
# h.next.next.next.next = ListNode(5)
# h.next.next.next.next.next = ListNode(2)

sol = Solution().partition(h, 3)

print()

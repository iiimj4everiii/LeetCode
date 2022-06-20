# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeWrapper:

    head = None

    def fill(self, lst):

        if len(lst) == 0:
            return None

        self.head = ListNode(lst[0])
        curr_node = self.head
        for l in lst[1:]:
            curr_node.next = ListNode(l)
            curr_node = curr_node.next

        return self.head

    def show(self):

        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val)
            curr_node = curr_node.next


class Solution:
    def insertionSortList(self, head):

        # Handling the corner cases.
        if head is None:
            return

        # Initialize prev_working_node to head and working_node to the
        # second node.
        prev_working_node = head
        working_node = head.next

        # We walk working_node through the linked list until we get to
        # the end of list.
        while working_node is not None:

            # For each working_node, we want to insert it to the proper
            # position in the link list from head up to working_node. We
            # initialize traversal nodes: prev_curr_node to None and
            # curr_node to head.
            prev_curr_node = None
            curr_node = head

            # We keep traversing through the linked list up to working_node.
            # If curr_node's value is greater or equal to working_node's
            # value, we break out of the inner while loop and get ready to
            # move some nodes around.
            while True:

                if curr_node.val >= working_node.val:
                    break

                prev_curr_node = curr_node
                curr_node = curr_node.next

            # We need to move working_node around unless working_node is
            # already in the correct position. In that case, we just move
            # both prev_working_node and working_node down the list by one.
            if curr_node is working_node:

                prev_working_node = working_node
                working_node = working_node.next

            # Otherwise,
            else:
                # we need to pop off working_node from the linked list by
                # pointing prev_working_node.next to working_node.next.
                prev_working_node.next = working_node.next

                # Corner case: if we are inserting working_node to the front
                # of the linked list, we point working_node.next to head and
                # update head to working_node.
                if curr_node is head:
                    working_node.next = head
                    head = working_node

                # Otherwise, we squeeze working_node between prev_curr_node
                # and curr_node. We do this by pointing prev_curr_node.next
                # to working_node and working_node.next to curr_node.
                else:
                    prev_curr_node.next = working_node
                    working_node.next = curr_node

                # Since an insertion happens here, prev_working_node will not
                # change. So we just need to update working_node to
                # prev_working_node.next
                working_node = prev_working_node.next

        return head


wrapper = ListNodeWrapper()
h = wrapper.fill([-1,5,3,4,0])
Solution().insertionSortList(h)
wrapper.show()

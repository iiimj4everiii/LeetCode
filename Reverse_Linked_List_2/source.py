# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        # Strategy:
        # Section the linked list into 3 different segments:
        # 1) From the head node to (left-1)th node.
        # 2) From the (left)th node to the (right)th node.
        # 3) From the (right+1)th node to the end of the linked list.
        # We will reverse segment 2 while leaving segment 1 and 3 alone.
        # However, there is a special case where (left)th node is the head
        # node. In this case, we will not have the first segment.

        # If left == right, then we will not change anything. Just return head.
        if left == right:
            return head

        # Initialize the end of segment 1, head_end, to head.
        head_end = head

        # Special case: if (left)th node is the head node.
        if left == 1:
            # Then, we don't have segment 1. So segment 2 starts at head_end.
            mid_start = head_end

        # Otherwise,
        else:
            # we find the end of segment 1
            for _ in range(1, left-1):
                head_end = head_end.next

            # The start of segment 2 is the end-of-segment-1's next node.
            mid_start = head_end.next

            # For a cleaner separation of segments, we will point the end
            # of segment 1 to None.
            head_end.next = None

        # Since we know left =/= right at this point, we can initialize the
        # end of segment 2 to mid_start's next node. mid_end will traverse
        # down the linked list (right-1) - left times.
        mid_end = mid_start.next
        for _ in range(left, right-1):
            mid_end = mid_end.next

        # We initialize the start of segment 3 to mid_end's next node. Since
        # we will leave segment 3 alone, we do not need to find the end of
        # segment 3. We need the start of segment 3 because we will chain
        # the end of reversed segment 2 to it at the end.
        tail = mid_end.next

        # For a cleaner separation of segments, we will point the end of
        # segment 2 to None.
        mid_end.next = None

        # At this point, we have a clean separation of 3 segments (or 2
        # segments if we are dealing with the special case). We can start
        # reversing the pointers of segment 2.
        # Initialize our traversal trios: prev_node, curr_node, and next_node.
        # We initialize prev_node to the start of segment 2, curr_node to the
        # second node next to mid_start, and next_node to the third node
        # from mid_start.
        prev_node = mid_start
        curr_node = prev_node.next
        next_node = curr_node.next

        # While curr_node is not None, we
        # 1) point curr_node's next to prev_node (reversing the pointer)
        # 2) move the traversal trio down one node. If curr_node reaches
        # None (clean separation of segment 2 from segment 3), we break
        # out of the loop. At this point, segment 2 is properly reversed.
        while True:
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node

            if curr_node is None:
                break

            next_node = next_node.next

        # Since segment 2 has been reversed, the start of segment 2,
        # mid_start will become the new mid_end. So point mid_start.next
        # to the beginning of segment 3.
        mid_start.next = tail

        # For the special case, we don't have segment 1. So the end of
        # the reversed segment 2 becomes the new head.
        if left == 1:
            head = mid_end

        # Otherwise, we point the end of segment 1 to the new mid_head.
        else:
            head_end.next = mid_end

        # At this point, all the segments are stitched back together.
        # Return head.
        return head


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

sol = Solution().reverseBetween(h, 1, 5)
print()

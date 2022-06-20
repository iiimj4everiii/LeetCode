# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # Strategy:
        # There are a few things to keep in mind.
        # 1) Since we are removing all the occurrences of a duplicate, we
        #    may need to keep track of 3 nodes at the same time. The first
        #    node should be a reference node where it is in the correct
        #    state. We need this node to help us remove nodes by pointing
        #    its next to a different node. The second and the third node
        #    traverses down the linked list. If they are the same, then we
        #    have duplicates. This is when we start removing curr_node(s)
        #    until we get to a pair of non-equal adjacent nodes. We remove
        #    curr_node one more time since we have to remove ALL OCCURRENCES
        #    of a duplicate.
        # 2) There are 3 different cases at any time. One: NO duplicates
        #    found just prior and we are currently sitting on a pair of
        #    non-equal (distinct-valued) nodes. Two: We are currently sitting
        #    on a pair of duplicates. Three: YES duplicates found just prior
        #    and we are currently sitting on a pair of distinct-value nodes.
        #    Case two will immediately transition into case three.
        # 3) If we are doing this without creating another linked list, we
        #    have to take care of leading duplicates separately since we will
        #    be returning the head node. Then we work on the body and use head
        #    as our initial reference node.
        # 4) There is a chance that we have trailing duplicates. This is
        #    handled by case two and then we take care of the last occurrence
        #    of the trailing duplicates outside of our main while loop.

        # Handling the corner cases.
        # 1) If head is None, then it is already in the right state.
        # 2) If head node is the only node, then there is nothing to remove.
        #    Therefore, head is also already in the right state.
        if head is None or head.next is None:
            return head

        # At this point, we know our linked list has at least 2 nodes.
        # This while loop will take care of ALL the leading duplicate nodes.
        while head is not None and head.next is not None:

            # If the current head node and its next node are the same value,
            # we need all the leading nodes that has the same value as the
            # current head node PLUS one extra node.
            if head.val == head.next.val:

                # This while loop will take care of the current leading
                # duplicate nodes. We keep removing nodes if head.next is not
                # None and
                while head.next is not None:

                    # if the next node has the same value as head.
                    if head.val == head.next.val:
                        head = head.next

                    # Otherwise, we break out of the node removing loop and
                    else:
                        break

                # remove the one extra node.
                head = head.next

            # If the current head node and its next node do not have the
            # same value, we can skip removing the leading duplicates.
            else:
                break

        # After possibly removing some of the duplicate leading nodes, check
        # for corner cases again.
        if head is None or head.next is None:
            return head

        # At this point, the head node is clear. We will start working on the
        # nodes in the middle. Initialize previous node prev_node to the head
        # node, current node curr_node to the following node. No duplicate yet
        # and so we initialize delete_curr_node to False.
        prev_node = head
        curr_node = prev_node.next
        delete_curr_node = False

        # We keep traverse down the linked list until we get to the last node.
        while curr_node.next is not None:

            # Set the next node to current node's next node. At this point, we
            # have prev_node -> curr_node -> next_node. prev_node is always
            # going to be in the part of the final linked list. So it is always
            # a good node.
            next_node = curr_node.next

            # curr_node traverses down the linked linked list along with
            # next_node. If the values of these two are the same, then we need
            # to remove curr_node and all the nodes that has the same value.
            # To do this, we remove curr_node first and traverse down the linked
            # list to see if there are other nodes with the same value. We set
            # delete_curr_node flag to True because eventually curr_node will
            # take the spot of the last node of the same value. We need to
            # remove curr_node one extra time.
            if curr_node.val == next_node.val:
                delete_curr_node = True
                prev_node.next = next_node
                curr_node = next_node

            # At this point, we are at a node with a different value. We either
            # came from a state that is:
            else:

                # 1) just removing some duplicates. In this case, we need to remove
                #    curr_node one more time. Set delete_curr_node flag to False.
                if delete_curr_node:
                    delete_curr_node = False
                    prev_node.next = next_node
                    curr_node = next_node

                # 2) already in a correct state. In which case we just move on.
                else:
                    prev_node = prev_node.next
                    curr_node = curr_node.next

        # We have may exited from the while loop prematurely. If there are
        # trailing duplicates, we need to remove curr_node one extra time.
        if delete_curr_node:
            next_node = curr_node.next
            prev_node.next = next_node

        return head


h = ListNode(1)
h.next = ListNode(1)
h.next.next = ListNode(2)

sol = Solution().deleteDuplicates(h)

print()

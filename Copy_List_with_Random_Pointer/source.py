# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        # Strategy:
        # 1) Traverse through the original head list and make a deep copy
        #    of all the nodes.
        # 2) Create a mapping between the nodes in the original head list
        #    to the nodes in new_head list.
        # 3) Go through both original head list and new_head list, get the
        #    random node from the original head list, use the mapping to
        #    map that to a node in new_head list. Point the random node in
        #    the corresponding new_head list to the mapped random node.

        # Handling corner cases.
        if head is None:
            return None

        # Initialize a mapping between nodes in the original head list to
        # the nodes in the new head list.
        mapping = {}

        # Initialize new_head to the value of original head.
        new_head = Node(head.val)

        # Add the first mapping: original head pointer to new head pointer.
        mapping[head] = new_head

        # Initialize traversal nodes: curr_node to original head and
        # new_curr_node to new_head.
        curr_node = head
        new_curr_node = new_head

        # Perform deep copy of the original head list and also create a
        # mapping between nodes in the original head list to the nodes in
        # the new_head list.
        while curr_node.next is not None:

            # Traverse and make a deep copy.
            curr_node = curr_node.next
            new_curr_node.next = Node(curr_node.val)
            new_curr_node = new_curr_node.next

            # Create a mapping.
            mapping[curr_node] = new_curr_node

        # Re-initialize traversal nodes back to head and new_head.
        curr_node = head
        new_curr_node = new_head

        # Go through the nodes in new_head list and point the random
        # pointer to another node in new_list that corresponds to the
        # node in the original head list. We do this by traversing
        # down the head list and look at what each node's random is
        # pointed to. We use the mapping we created earlier to translate
        # that random node to the corresponding random node in new_head
        # list. Then go to the corresponding node in new_head and point
        # its random to the said corresponding random node.
        while curr_node is not None:

            # Get the node pointed by random in the node in head list.
            curr_node_random = curr_node.random

            # If the node pointed by random in the node in head list is
            # nullptr, then we just point the random node in new_head to
            # nullptr. Otherwise, we get the mapping of the random node
            # in new_head and point that node's random to the mapped node.
            if curr_node_random is None:
                new_curr_node.random = None
            else:
                new_curr_node.random = mapping[curr_node_random]

            # Traverse down the lists.
            curr_node = curr_node.next
            new_curr_node = new_curr_node.next

        return new_head


h = Node(7)
h.next = Node(13)
h.next.next = Node(11)
h.next.next.next = Node(10)
h.next.next.next.next = Node(1)

h.random = None
h.next.random = h
h.next.next.random = h.next.next.next.next
h.next.next.next.random = h.next.next
h.next.next.next.next.random = h

sol = Solution().copyRandomList(h)
print()

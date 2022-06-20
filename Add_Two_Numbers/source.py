# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Strategy:
        # Convert the linked list format to the reversed integer format
        # Add the two numbers in integer format
        # Convert the integer format to a python list
        # Then convert the python list representation of sum to linked list

        # Convert number in linked list format, l1 and l2, to the reversed integer format
        n1 = self.linked_list_to_int(l1)
        n2 = self.linked_list_to_int(l2)

        # Add the converted linked list numbers, n1 and n2, together.
        # Then convert that to a python list with least significant digit in the front.
        sum_digit = n1 + n2
        sum_digit_list = self.int_to_list(sum_digit)

        # Convert the python list of sum back to the reversed linked list format and return it.
        return self.list_to_linked_list(sum_digit_list)

    def linked_list_to_int(self, head) -> int:

        # Start with 0, keep shifting num to the right and adding the latest val to the ones digit

        num = 0
        power = 0
        while head is not None:
            num += head.val * 10 ** power
            head = head.next
            power += 1

        return num

    def int_to_list(self, num):

        # Starting with an empty list, append the ones digit of num to the list
        # Then divide num by 10 (shifting num to the right by 1 position)
        # Keep going until num reduces to 0

        int_in_list = []
        while num > 0:
            int_in_list.append(num % 10)
            num //= 10

        return int_in_list

    def list_to_linked_list(self, lst) -> ListNode:

        # Initialize the return list to be 0
        return_list_node = ListNode(0)

        if len(lst) > 0:
            # If lst is nonempty, re-initialize the return list to the first element of the lst list
            return_list_node = ListNode(lst[0])

            # Keep on adding linked list nodes to the return list until we get to None
            curr_node = return_list_node
            for l in lst[1:]:
                curr_node.next = ListNode(l)
                curr_node = curr_node.next

        return return_list_node


head1 = ListNode(0)
# head1.next = ListNode(4)
# head1.next.next = ListNode(3)

head2 = ListNode(0)
# head2.next = ListNode(6)
# head2.next.next = ListNode(4)

new_head = Solution().addTwoNumbers(head1, head2)

print()
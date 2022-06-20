class Solution:

    class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def calculate(self, s: str) -> int:

        # Strategy:

        # Faster implementation using stack instead of a
        # linked list. Refer to solution Approach 1.

        # We will first convert the mathematical expression in
        # string s to a linked list that separates numbers and
        # operators. We want a linked list that has the form:
        # num -> op -> num -> op -> num -> ...

        # Then we will take care of all multiplications and
        # divisions first - storing the result in the node on the
        # lhs: lhs_num = lhs_num * rhs_num. Finally, we remove
        # the operator node and the rhs node afterward.

        # We will take care of all the additions and subtractions
        # the same as multiplications and divisions.
        # At the end, we will only have 1 node left as the rest
        # of them are removed after each operation.

        # Method to convert string expression s to a linked list
        # of alternating number nodes and operator nodes.
        head = self.str_exp_to_link_list(s)

        # Method to process all the multiplications and divisions
        # first. This method skips the additions and subtractions.
        self.multiply_and_divide(head)

        # Method to process all the additions and subtractions.
        self.add_and_subtract(head)

        # At this point, there is only 1 node left in the linked
        # list: head node. Return the value stored in this node.
        return head.val

    # Method to convert string expression s to a linked list of
    # alternating number nodes and operator nodes.
    def str_exp_to_link_list(self, s):

        # Skips leading whitespaces.
        head = None
        idx = 0
        while idx < len(s):
            if s[idx].isnumeric():
                head = self.ListNode(int(s[idx]))
                break

            idx += 1

        curr = head
        is_prev_num = True
        for si in s[idx+1:]:

            # Skips whitespaces.
            if si.isspace():
                continue

            if is_prev_num:
                if si.isnumeric():
                    curr.val = curr.val * 10 + int(si)
                else:
                    curr.next = self.ListNode(si)
                    curr = curr.next
                    is_prev_num = False
            else:
                curr.next = self.ListNode(int(si))
                curr = curr.next
                is_prev_num = True

        return head

    # Method to process all the multiplications and divisions.
    # This method skips the additions and subtractions.
    @staticmethod
    def multiply_and_divide(head):

        curr = head
        while curr.next is not None:

            operator = curr.next.val
            num2 = curr.next.next.val

            if operator == '*':
                curr.val *= num2
                curr.next = curr.next.next.next

            elif operator == '/':
                curr.val //= num2
                curr.next = curr.next.next.next

            else:
                curr = curr.next.next

        return None

    # Method to process all the additions and subtractions.
    @staticmethod
    def add_and_subtract(head):

        curr = head
        while curr.next is not None:

            operator = curr.next.val
            num2 = curr.next.next.val

            if operator == '+':
                curr.val += num2

            else:
                curr.val -= num2

            curr.next = curr.next.next.next

        return None


sol = Solution().calculate("1*2-3/4+5*6-7*8+9/10")
print(sol)

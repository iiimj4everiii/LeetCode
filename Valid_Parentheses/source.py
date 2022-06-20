class Solution:
    def isValid(self, s: str) -> bool:

        # Handling special cases
        if len(s) % 2 == 1:
            return False

        i = 1
        while len(s) > 0 and i < len(s):

            # If we detect a right parentheses, we need a matching left parentheses.
            if s[i] in [')', ']', '}']:

                if i == 0:
                    return False

                # Get the left parentheses
                left_paren = self.get_left_paren(s[i])

                # If the left parentheses and the right parentheses does not match,
                # s is an invalid string of parentheses
                if not left_paren == s[i-1]:
                    return False

                # A valid pair of parentheses found. Slice them out of s
                s = s[:(i-1)] + s[(i+1):]

                # Move the current index back 2 units.
                i = i - 2

            i = i + 1

        if len(s) > 0:
            return False

        return True

    def isValid2(self, s: str) -> bool:

        # Handling special cases
        if len(s) % 2 == 1:
            return False

        stack = []
        for si in s:
            # If we detect a right parentheses, we need a matching left parentheses.
            if si in [')', ']', '}']:
                # If there is nothing in the stack to match si, pop() will return IndexError
                try:
                    top = stack.pop()
                except IndexError:
                    return False

                # If the right paren and the left paren doesn't match,
                # then we have an invalid string of parentheses
                if top == self.get_left_paren(si):
                    return False
            else:   # If we detect a right parentheses, then we append
                stack.append(si)

        if len(stack) > 0:
            return False

        return True

    def get_left_paren(self, right_paren):
        if right_paren == ')':
            return '('
        elif right_paren == ']':
            return '['
        else:
            return '{'


s = "(){[())(()]}"

print(Solution().isValid2(s))

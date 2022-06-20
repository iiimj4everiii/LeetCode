class Solution:
    def evalRPN(self, tokens) -> int:

        # Strategy:
        # Push all the numbers onto a stack as we go through
        # the tokens list. If we see an math operator, pop
        # the top 2 numbers off the stack and do math on them
        # based on the operator.

        # Simple function that takes num1, math operator,
        # and num2 as input. Compute the result based on
        # the operator passed.
        def do_math(num1, operator, num2):

            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            else:
                if num1 > 0 and num2 < 0:
                    return -(num1 // -num2)
                elif num1 < 0 and num2 > 0:
                    return -(-num1 // num2)
                else:
                    return num1 // num2

        # We will use a list to act as a stack for integers.
        stack = []

        # Initialize res to the first token. The first token
        # has to be an integer.
        res = int(tokens[0])

        # Go through each token t in tokens list.
        for t in tokens:

            # If t is an integer, push it to stack.
            if t.lstrip("-").isnumeric():
                stack.append(int(t))

            # Otherwise, pop the last 2 integers pushed to
            # stack and do math with them.
            else:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                res = do_math(num1, t, num2)
                stack.append(res)

        return res


t = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution().evalRPN(t)
print(sol)

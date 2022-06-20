class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        # Initialize empty stack list and min number to be 2^64 - 1
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:

        # ATTENTION: if self.min is None test must come first in the conditional test,
        # otherwise will will get a NoneType error from the second conditional test
        # If self.min is None or the current number is smaller than self.min,
        # then reassign self.min to val
        if self.min is None or val < self.min:
            self.min = val

        # Append val to the stack list
        self.stack.append(val)

        return

    def pop(self) -> None:

        # Get the last element in the stack list and remove it
        last_element = self.stack.pop(-1)

        # If the last element popped happens to be self.min,
        # we need to find the next minimum number in the stack list
        if last_element == self.min:
            if len(self.stack) > 0:
                self.min = min(self.stack)
            else:
                self.min = None

        return

    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:

        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

stack = MinStack()
stack.push(0)
stack.push(1)
stack.push(2)
print(stack.top())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
stack.push(3)
print(stack.top())
print(stack.getMin())
stack.push(4)
print(stack.top())
print(stack.getMin())
stack.pop()
print(stack.getMin())

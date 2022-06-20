# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#         self.nums = nums
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """

        # Copy all the numbers stored in the iterator object to PeekingIterator.
        # We store all these numbers internally in self.nums:list. We will also
        # keep a pointer to the current index in the self.nums:list.
        self.nums = []
        self.curr_idx = 0
        while iterator.hasNext():
            self.nums.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # For peeking, just return the value stored in curr_idx of nums if we
        # are still within bound.
        if self.hasNext():
            return self.nums[self.curr_idx]

        return None

    def next(self):
        """
        :rtype: int
        """

        # For next, we peek at the next value in self.nums. If the value is
        # valid, then we increment self.curr_idx. Finally, return res =
        # the peek value.
        res = self.peek()

        if res is not None:
            self.curr_idx += 1

        return res

    def hasNext(self):
        """
        :rtype: bool
        """

        # Test if self.curr_idx is still within bound.
        return self.curr_idx < len(self.nums)

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
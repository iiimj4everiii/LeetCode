class Solution:
    def getRow(self, rowIndex: int):

        # Seed
        pascal = [1]

        # Iterative approach: generate pascal triangle one row at a time.
        for i in range(1, rowIndex+1):

            # Create array of 1's of size (i+1)
            new_pascal = [1] * (i+1)

            # For the inner arrays starting from index = 1 to index = end-1,
            # We take the sum current and previous indexed elements.
            for j in range(1, i):
                new_pascal[j] = pascal[j-1] + pascal[j]

            # Overwrite the old pascal with the new_pascal
            pascal = new_pascal

        return pascal


print(Solution().getRow(3))

class Solution:
    def generate(self, numRows: int):

        # Seed
        pascal = [[1]]

        # Iterative approach: generate pascal triangle one row at a time.
        for i in range(1, numRows):

            # Create array of 1's of size (i+1)
            new_pascal = [1] * (i+1)

            # For the inner arrays starting from index = 1 to index = end-1,
            # We take the sum current and previous indexed elements.
            for j in range(1, i):
                new_pascal[j] = pascal[i-1][j-1] + pascal[i-1][j]

            # Overwrite the old pascal with the new_pascal
            pascal.append(new_pascal)

        return pascal


print(Solution().generate(5))

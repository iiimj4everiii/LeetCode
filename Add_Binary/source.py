class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Determine the padding size of each binary string
        pad_size_a = max(len(b)-len(a), 0)
        pad_size_b = max(len(a)-len(b), 0)

        # Pad the shorter binary string with 0's to the front
        # Note: + is for string concatenation here
        a = "0" * pad_size_a + a
        b = "0" * pad_size_b + b

        # c stores the binary sum of a and b
        c = ""

        # carry_one carries over to the next column
        carry_one = "0"
        for i in reversed(range(len(a))):
            # s contains the sum of a, b, and carry_one
            s, carry_one1 = self.binary_sum(a[i], b[i])
            s, carry_one2 = self.binary_sum(s, carry_one)

            c = s + c

            carry_one, _ = self.binary_sum(carry_one1, carry_one2)

        # If carry_one is not 0, that means you have an overflow
        # Add 1 to the front of c
        if carry_one == "1":
            c = "1" + c

        return c

    def binary_sum(self, a, b):

        if a == "1" and b == "1":
            return ["0", "1"]
        elif a == "0" and b == "0":
            return ["0", "0"]
        else:
            return ["1", "0"]

a = "11111"
b = "10011"
print(Solution().addBinary(a, b))

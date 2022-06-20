class Solution:
    def mySqrt(self, x: int) -> int:

        # Handling the corner cases
        if x == 0 or x == 1:
            return x

        i = 2
        j = 2
        # Let i grow exponentially to quick get to a ball park number
        # j keeps track of the previous value of i before (i * i) ** 2 grows beyond x
        while i**2 <= x:
            j = i
            i = i * i

        # Let j grow linearly to get to a finer ball park number
        while j**2 <= x:
            j = j * 2

        # Let k grow constantly to get to our number
        k = j // 2
        while k**2 <= x:
            k = k + 1

        return k-1


print(Solution().mySqrt(9999))

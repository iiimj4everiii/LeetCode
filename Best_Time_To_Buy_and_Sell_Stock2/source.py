class Solution:
    def maxProfit(self, prices) -> int:

        # INSIGHT:
        # Keep track of the current price as we iterate through the prices list
        # Add to profit only if the current price is higher than the previous price

        # Initializing profit so far
        profit = 0
        previous_price = prices[0]

        for i in range(1, len(prices)):

            # If the current price is higher than previous price, we buy at previous_price,
            # and sell it at current price, prices[i]
            if prices[i] > previous_price:
                profit += prices[i] - previous_price

            # Keep track of the current price.
            previous_price = prices[i]

        return profit


prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))

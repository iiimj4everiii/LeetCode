# Problem: max difference towards the right direction.

class Solution:
    def maxProfit(self, prices) -> int:

        # INSIGHT:
        # We should iterate backwards in order to "see the future"
        # Keeping the max future price and max profit at any present
        # time as we move backwards

        # Number of elements in the prices list
        n = len(prices)

        # Initialize max stock price and max profit to 0
        max_price = 0
        max_profit = 0

        # Iterating backwards and keeping track of
        # the maximum future price and max profit.
        for i in reversed(range(n)):

            # Keep tracking the max stock price as we move backwards
            if prices[i] > max_price:
                max_price = prices[i]
                continue

            # Knowing the max future price, we can keep track of max profit at
            # any present time. Update max_profit if we find a better day to sell
            if max_profit < max_price - prices[i]:
                max_profit = max_price - prices[i]

        return max_profit


prices = [7,1,5,3,6,4]

print(Solution().maxProfit([]))

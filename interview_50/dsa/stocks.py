# Best Time to Buy and Sell Stock

# You are given an array prices.

# prices[i] represents the stock price on day i.

# You want to maximize your profit by choosing:

# one day to buy
# a later day to sell

# Return the maximum profit possible.

# If no profit is possible, return 0.

class Solutions:
    def maxProfit(self, prices: list[int]) -> int:
        l ,r = 0, 1
        self.maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]

                self.maxProfit = max(self.maxProfit, profit)
            else:
                l = r
            r += 1
        
        return self.maxProfit
            

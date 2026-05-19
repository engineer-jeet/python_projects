class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0,1 # l = buy day, r = sell day
        max_Profit = 0
        while r < len(prices):
            #profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_Profit = max(max_Profit, profit)
            else:
                l = r
            r+=1
        return max_Profit


prices = [7,1,5,3,6,4]
sol = Solution()
result = sol.maxProfit(prices)

print(result)































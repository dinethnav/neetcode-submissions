class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l =0
        r = 1
        profit = 0

        while r<len(prices):
            if prices[r]<=prices[l]:
                l=r
                r+=1
            else:
                profit_tmp = prices[r] - prices[l]
                profit = max(profit,profit_tmp)
                r+=1

        return profit
        
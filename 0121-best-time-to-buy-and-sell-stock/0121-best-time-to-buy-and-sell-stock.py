class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        lowest = prices[l]
        while r < len(prices):
            
            if prices[r] < lowest:
                lowest = prices[r]
                
            res = max(res, prices[r] - lowest)
            r = r + 1
        return res
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy = prices[0]
        profit = 0
        for cur in prices:
            if cur <= buy:
                buy = cur
            elif cur > buy:
                profit += cur - buy
                buy = cur
        return profit
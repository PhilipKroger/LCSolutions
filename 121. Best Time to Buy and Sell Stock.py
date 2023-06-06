class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right, max_profit = 0, 1, 0
        while right < len(prices):
            c = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(max_profit, c)
            else:
                left = right
            right += 1
        return max_profit

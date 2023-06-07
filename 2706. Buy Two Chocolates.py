class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        min1 = min(prices)
        min1_ind = prices.index(min1)
        prices.pop(min1_ind)
        min2 = min(prices)
        min2_ind = prices.index(min2)
        prices.pop(min2_ind)
        if min1 + min2 <= money:
            return money-min1-min2
        else:
            return money

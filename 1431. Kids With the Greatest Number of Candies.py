class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        rez = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                rez.append(True)
            else:
                rez.append(False)
        return rez
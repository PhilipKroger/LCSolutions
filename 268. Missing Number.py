class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = 0
        for i in range(n+1):
            k += i
        return k - sum(nums)

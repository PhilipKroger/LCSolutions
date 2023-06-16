class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sorted(nums)[-2]-1)*(sorted(nums)[-1]-1)
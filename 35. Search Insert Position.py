class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            else:
                nums = [-10**8] + nums + [10**8]
                for i in range(len(nums)):
                    if nums[i] < target < nums[i+1]:
                        return i
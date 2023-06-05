class Solution(object):
    def binary_search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r, m = 0, len(nums) - 1, 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        else:
            return -1


arr, x = [-1, 0, 3, 5, 9, 12], 2
rez = Solution()
print(rez.binary_search(arr, x))
print(rez.binary_search([2, 3, 4, 10, 40], 10))

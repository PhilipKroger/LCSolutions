class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        k = 1
        for i in range(len(arr) - 2):
            if arr[i + 1] - arr[i] == arr[i + 2] - arr[i + 1]:
                k += 1
        if k == len(arr) - 1:
            return True
        else: 
            return False

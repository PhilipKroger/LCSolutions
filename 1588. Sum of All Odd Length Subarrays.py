class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sm = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if len(arr[i:j+1])%2!=0:
                    sm += sum(arr[i:j+1])
        return sm


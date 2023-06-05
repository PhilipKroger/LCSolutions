class Solution(object):
    def checkStraightLine(self, c):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        k = 1
        for i in range(0, len(c) - 2):
            c0, c3, c1 = c[i - 1], c[i], c[i + 1]
            if (c1[0] - c0[0]) * (c3[1] - c1[1]) == (c3[0] - c1[0]) * (c1[1] - c0[1]):
                k += 1
        if k == len(c) - 1:
            return True
        else:
            return False

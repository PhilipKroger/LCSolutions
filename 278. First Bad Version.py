# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        v = 0
        while l <= h:
            m = (l+h)//2
            bv = isBadVersion(m)
            if bv ==True:
                v = m
                h = m-1
            elif bv == False:
                l = m+1
        return v

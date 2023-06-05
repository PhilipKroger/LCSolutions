class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = []
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                l.append(i)
        if len(l) == 0:
            return -1
        else:
            return min(l)

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        l = [''] * len(s)
        for i in range(len(indices)):
            l[indices[i]] = s[i]
        l = ''.join(l)
        return l
